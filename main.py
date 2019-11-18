import cv2
import numpy as np
import serial
import image
import serial
import threading
import time

vidion_isRun = False
vision_results = -1

class visionThread(threading.Thread):
    def __init__(self, video_cap):
        threading.Thread.__init__(self)
        
        self.img_width = image.width     # 图片尺寸
        self.img_height = image.height

        self.knn = cv2.ml.KNearest_create()
        
        # 读取训练文件
        with np.load("./data/knn_data.npz") as knn_data:
            print(knn_data.files)
            train_data = knn_data['train_data']
            train_labels = knn_data['train_labels']

            self.knn.train(train_data,
                           cv2.ml.ROW_SAMPLE,
                           np.array(train_labels))
            
        # 打开测试用视频或摄像头
        self.cap = cv2.VideoCapture(video_cap)
        
    def __del__(self):
        self.cap.release()
        
    def run(self):
        global vision_results
        global vidion_isRun
        
        while self.cap.isOpened():
            image_data = []
            ret, img = self.cap.read()
            if not ret or not vidion_isRun:
                continue
            out_img = image.preprocess(img)

            image_data.append(out_img)
            x = np.array(image_data)
            test = x.reshape(-1, self.img_width*self.img_height).astype(np.float32)

            # knn预测，k值更具训练的图片数量可以修改，越多可以越大
            ret,result,neighbours,dist = self.knn.findNearest(test, k=5)
            
            vision_results = ret
#            cv2.imshow("img",img) # 不能再线程中显示
#            cv2.waitKey(10)
        print ("退出线程")

class serialThread(threading.Thread):
    def __init__(self, port, baud):
        threading.Thread.__init__(self)
        self.port = serial.Serial(port, baud, timeout=0.5)
        
    def run(self):
        while self.port.isOpen():
            count = self.port.inWaiting()
            if count > 0:
                rec_str = self.port.read(count)
                data_bytes=data_bytes+rec_str
                print('当前数据接收总字节数：'+str(len(data_bytes))+' 本次接收字节数：'+str(len(rec_str)))
                print(str(datetime.now()),':',binascii.b2a_hex(rec_str))
        print ("退出线程")
        
    def send_data(self, data):
        self.port.write(data)

#硬件串口用:/dev/ttyAMA0 USB串口用:/dev/ttyUSB0
serialPort = '/dev/ttyAMA0'  # 串口
baudRate = 9600  # 波特率

# 创建新线程
thread1 = visionThread(0)
thread2 = serialThread(serialPort, baudRate)
thread1.setDaemon(True)
thread2.setDaemon(True)

# 开启新线程
thread1.start()
thread2.start()

# 输出用列表
output_l = ['cube', 'pentagon', 'triangle', 'N', 'cylinder', 'pentagram']

while True:
    if not vidion_isRun:
        vision_results = -1
    if vision_results != -1:
        print("识别结果:", output_l[int(vision_results)])
    time.sleep(100)
    thread2.send_data("-------")

print ("退出主线程")
