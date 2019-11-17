###### 程序包文件及函数说明

- main.py <font color=red>测试程序，可执行程序</font>，调用训练好 knn_data.npz 进行识别
- train_main.py <font color=red>训练程序，可执行程序</font>，导出训练文件到 data 文件夹
- TrainFileInfo.py 训练素材的读取与数据保存
- image_processing.py 图片的预处理
- image 训练素材，每个识别的类保存在独立文件夹中
- video 测试用视频
- data 训练后文件导出到此文件夹
- doc 说明文档
- TakePicture.py <font color=red>拍照程序，可执行程序</font>， 10ms一张，图片保存在images文件夹下



可执行程序都是可以在终端中运行的

先放出demo测试算法，因为具体识别场景的不同训练素材要重新录制，训练素材一般在400～500左右，一般不要太多会影响算法速度

素材较大放到了百度网盘 链接:https://pan.baidu.com/s/1Zlea3eieESmQH_wS00BMMQ  密码:diqk

素材下载后直接放入程序文件夹进行测试