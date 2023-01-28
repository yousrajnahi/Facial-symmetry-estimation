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
        frame_7=result_image('7',rects,shape,eps,frame)
        coupl_smile_symetrie(shape[48],shape[54],np.array([shape[48][0]+0.01,shape[48][1]]),frame_7)
        cv2.imshow('frame7', frame_7)
    except:
        print("No face detected")
    if cv2.waitKey(33) & 0xFF == 27:
        break 
cap.release()
cv2.destroyWindow()  