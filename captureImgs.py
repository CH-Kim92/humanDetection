import cv2
import os
import uuid
import time

PATH = os.path.join('Resources', 'image')
num_pics = 15

cap = cv2.VideoCapture(1)
# 20 secs later webcam is open 
time.sleep(20)

for k in range(3):

    for i in range(num_pics):

        ret, frame = cap.read()

        # Naming out image path
        imgname = os.path.join(PATH, 'person'+'.'+str(uuid.uuid1())+'.jpg')

        # Save the Image into the directory
        cv2.imwrite(imgname, frame)

        cv2.imshow('Image Collection', frame)

        #capture image every 0.5 secs
        time.sleep(0.5)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    # Waiting for 10sec to capture next object
    time.sleep(10)

cap.release()
cv2.destroyAllWindows()
