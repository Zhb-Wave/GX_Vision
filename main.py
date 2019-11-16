import cv2
import numpy as np
import serial
import image

img_width = image.width     # 图片尺寸
img_height = image.height

# 输出用列表
output_l = ['cube', 'pentagon', 'triangle', 'N', 'cylinder', 'pentagram']

knn = cv2.ml.KNearest_create()

# 读取训练文件
with np.load("./data/knn_data.npz") as knn_data:
    print(knn_data.files)
    train_data = knn_data['train_data']
    train_labels = knn_data['train_labels']

    knn.train(train_data, cv2.ml.ROW_SAMPLE, np.array(train_labels))

# 打开测试用视频或摄像头
cap = cv2.VideoCapture("./video/blue4.mp4")

while cap.isOpened():
    image_data = []
    ret, img = cap.read()
    out_img = image.preprocess(img)
    
    image_data.append(out_img)
    x = np.array(image_data)
    test = x.reshape(-1, img_width*img_height).astype(np.float32)

    # knn预测，k值更具训练的图片数量可以修改，越多可以越大
    ret,result,neighbours,dist = knn.findNearest(test, k=5)

    print(output_l[int(ret)])
    cv2.imshow("img",img)
    cv2.waitKey(10)

