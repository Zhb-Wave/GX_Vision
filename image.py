import cv2

width = 32      # 图片大小
height = 32

def preprocess(image):
    """
    图片的预处理，训练和识别时需要对图片进行相同处理，特意将这段操作单独拿出来
    """
    gray_img = cv2.cvtColor(cv2.resize(image, (width, height),
                                       interpolation=cv2.INTER_AREA),
                            cv2.COLOR_BGR2GRAY)
#    thresh_img = cv2.threshold(gray_img, 120, 255, cv2.THRESH_OTSU)
    
    out_img = gray_img
    return out_img
