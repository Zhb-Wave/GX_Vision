import cv2
import time
import os

def take(index, out_path):
    """
    @brief
    @param index: 
    @param out_path:
    """

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    cap = cv2.VideoCapture(index)
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow("frame", frame)
        
        out_name = time.strftime("%Y%m%d%H%M%S", time.localtime())
        cv2.imwrite(out_path + '/' + out_name+'.jpg', frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()


take(0, "./images")
