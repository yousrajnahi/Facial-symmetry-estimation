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
        frame_3=result_image('3',rects,shape,eps,frame)
        facial_symmetry_restingface(shape[39],shape[42],shape[57],np.array([shape[39][0],shape[39][1]-0.01]),shape[39],np.array([shape[42][0],shape[42][1]-0.01]),shape[42],np.array([shape[45][0],shape[45][1]-0.01]),shape[45],np.array([shape[36][0],shape[36][1]-0.01]),shape[36],np.array([shape[0][0],shape[0][1]-0.01]),shape[0],np.array([shape[16][0],shape[16][1]-0.01]),shape[16],frame_3)
        cv2.imshow('frame3', frame_3)
    except:
        print("No face detected")
    if cv2.waitKey(33) & 0xFF == 27:
        break 
cap.release()
cv2.destroyWindow()  