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
        frame_1=result_image('1',rects,shape,0.9,frame)
        facial_symmetry(shape[39],shape[42],shape[33],shape[57],frame_1)
        cv2.imshow('frame1', frame_1)
    except:
        print("No face detected")
    if cv2.waitKey(33) & 0xFF == 27:
        break 
cap.release()
cv2.destroyWindow()  