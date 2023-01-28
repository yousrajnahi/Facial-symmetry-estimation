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
        frame_5=result_image('5',rects,shape,eps,frame)
        coupl_yeu_symetrie(shape[39],shape[42],np.array([shape[39][0]+0.01,shape[39][1]]),frame_5)
        cv2.imshow('frame5', frame_5)
    except:
        print("No face detected")
    if cv2.waitKey(33) & 0xFF == 27:
        break 
cap.release()
cv2.destroyWindow()  