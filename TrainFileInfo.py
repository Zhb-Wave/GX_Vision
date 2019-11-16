import os
import numpy as np
import shutil

class TrainInfo:
    img_path = None
    __train_info = {}
    
    def __init__(self, train_path):
        self.setTrainPath(train_path)
        self.generateTrainInfo(self.img_path)

    def setTrainPath(self, train_path):
        """
        设置训练图片路径
        """
        self.img_path = train_path
        print("Train image path: " , self.img_path)

    def generateTrainInfo(self, train_path):
        """
        遍历文件夹找出文件夹中png jpeg jpg文件，返回一个列表
        """
        labes = []
        self.__train_info.clear()
        
        if self.img_path is None:
            print("Train image path is None")
            return

        for root, dirs, files in os.walk(self.img_path):
            if dirs == []:
                print("Train image path No folder")
            else:
                labes = dirs
            break

        for ldir in labes:
            for root, dirs, files in os.walk(self.img_path + '/' + ldir):
                img_files = []
                
                for filename in files:
                    if os.path.splitext(filename)[1] == ".png" \
                    or os.path.splitext(filename)[1] == ".jpeg" \
                    or os.path.splitext(filename)[1] == ".jpg":
                        apath = os.path.join(root, filename)
                        img_files.append(apath)
                self.__train_info.update({ldir:img_files})
                
    def getTrainInfo(self):
        return self.__train_info.items()
    
    def getTrainLabels(self):
        return self.__train_info.keys()

    def getTrainImgPaths(self):
        return self.__train_info.values()

def saveInfo(path, train_data, train_labels):
    """
    保存训练后的结果
    """
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    np.savez(path + "/knn_data.npz",
             train_data = train_data,
             train_labels = train_labels)
    
        

