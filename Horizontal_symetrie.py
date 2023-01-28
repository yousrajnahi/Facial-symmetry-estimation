from function import *
eps=2
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip camera vertically
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 1)
        shape=detection(frame,gray,rects) 
        frame_2=result_image('2',rects,shape,eps,frame)
        smile(shape[33],np.array([shape[33][0]+0.01,shape[33][1]]),shape[8],np.array([shape[8][0]+0.01,shape[8][1]]), middle(shape[21],shape[22]), np.array([ middle(shape[21],shape[22])[0]+0.01, middle(shape[21],shape[22])[1]]),frame_2)
        cv2.imshow('frame2', frame_2)  
    except:
        print("No face detected")
    if cv2.waitKey(33) & 0xFF == 27:
        break 
cap.release()
cv2.destroyWindow()  