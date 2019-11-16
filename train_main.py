import cv2
import TrainFileInfo
import numpy as np
import image

img_width = image.width     # 图片尺寸
img_height = image.height

file_info = TrainFileInfo.TrainInfo("./images")     # 训练对象，选择训练图片的文件夹

knn = cv2.ml.KNearest_create()  # 创建KNN训练器

def main():
    image_data = []     # 保存图片数据
    image_labels = []   # 保存图片的标签，文件夹的名字
    train_labels = []   # 保存训练标签 [0,1,2,...]
    
    class_sum = 0
    
    for label, paths in file_info.getTrainInfo():   # 遍历文件夹，获取图片
        for path in paths:
            img = cv2.imread(path)
            out_img = image.preprocess(img)
            
            image_data.append(out_img)
            train_labels.append([class_sum])
            
        image_labels.append(label)
        class_sum += 1

    x = np.array(image_data)    # 将数据转化为numpy的数组
    train = x.reshape(-1, img_width*img_height).astype(np.float32)

    knn.train(train, cv2.ml.ROW_SAMPLE, np.array(train_labels)) # 使用KNN训练器训练

    TrainFileInfo.saveInfo("./data", train, train_labels)   # 保存训练数据

    print("图片的标签 ", image_labels)

if __name__ == '__main__':
    main()
