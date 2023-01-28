# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import matplotlib.pyplot as plt
import math

#pip install cmake
#pip install dlib

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


def rect_to_bb(rect):
    # take a bounding predicted by dlib and convert it
    # to the format (x, y, w, h) as we would normally do
    # with OpenCV
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    # return a tuple of (x, y, w, h)
    return (x, y, w, h)

def shape_to_np(shape, dtype="int"):
    # initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=dtype)
    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    # return the list of (x, y)-coordinates
    return coords



def middle(x,y):
    a=int((x[0]+y[0])/2)
    b=int((x[1]+y[1])/2)
    return(np.array([a,b]))



def triangle(x,y,z,image,c):
    cv2.line(image, (x), (y),c , lineType=8)
    cv2.line(image, (x), (z), c, lineType=8)
    cv2.line(image, (y), (z),c, lineType=8)
    


def facial_symmetry(x,y,z,t,image):
    triangle(x,y,z,image,(0, 255, 0))
    triangle(x,y,t,image,(255, 0, 0))
    cv2.line(image, middle(x,y), t,(0, 0, 255), lineType=8)
    



def diseu(p1,p2):
    return(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ))

def extend_line ( p1 , p2 , distance = 10000 ) :
    diff = np.arctan2 ( p1[1] - p2[1] , p1[ 0] - p2[0] )
    p3_x = int ( p1[0]+ distance * np.cos ( diff ) )
    p3_y = int ( p1[1] + distance * np.sin ( diff ) )
    p4_x = int ( p1[0] - distance * np.cos ( diff ) )
    p4_y = int ( p1[1] - distance * np.sin ( diff ) )
    return ( ( p3_x , p3_y ) , ( p4_x , p4_y ) )

def samedist(x,y,z,eps):
    
    if(int(diseu(x,z)) + int(diseu(z,x))- eps <=int(diseu(x,y)) and  int(diseu(x,y))<= int(diseu(x,z)) + int(diseu(z,x))+ eps ):
        return(1)
    else:
        return(0)

def samesidt2(ss,aa,zz,mm,nn,dd,eps):
    if(diseu(ss,dd)-eps<=diseu(ss,aa)+diseu(aa,zz)+diseu(zz,mm)+diseu(mm,nn)+diseu(nn,dd) and diseu(ss,aa)+diseu(aa,zz)+diseu(zz,mm)+diseu(mm,nn)+diseu(nn,dd) <=diseu(ss,dd)+eps):
        return(1)
    else:
        return(0)


def smile(x,y,z,t,zz,tt,image):
    x,y=extend_line (x ,y , distance = 10000)
    z,t=extend_line (z,t , distance = 10000)
    zz,tt=extend_line (zz,tt , distance = 10000 )
    cv2.line(image, x,y,(255, 255, 0), lineType=8)
    cv2.line(image, z,t,(255, 255, 0), lineType=8)
    cv2.line(image, zz,tt,(255, 255, 0), lineType=8)
    
# loop over the face detections
def detection(image,gray,rects):
    for (i, rect) in enumerate(rects):
    # determine the facial landmarks for the face region, then
    # convert the facial landmark (x, y)-coordinates to a NumPy
    # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
        for (x, y) in shape:
            cv2.circle(image, (x, y), 1, (0,0 , 255), -1)
        # show the output image with the face detections + facial landmarks
        #cv2.imshow("Output", image)
    #cv2.waitKey(0)
    return(shape)
   
def filenameinfo(z,t,eps):
    if z[0] - eps <= z[0] and z[0]<= z[0]+eps and  z[0] - eps <= t[0] and t[0] <= z[0]+eps:
        return(1)
    else:
        return(0)

def filenameinfo2(z,zz,x,eps):
    if samedist(z,zz,x,eps)== 1 :
        return(1)
    else:
        return(0)

def filenameinfo3(ss,aa,zz,mm,nn,dd,eps):
    if(samesidt2(ss,aa,zz,mm,nn,dd,eps)== 1):
        return(1)
    else:
        return(0)

def filenameinfo4(xx,yy,eps):
    if(xx[1]-eps<=yy[1] and yy[1]<=xx[1]+eps):
        return(1)
    else:
        return(0)
  

def filename_nb(input,shape,eps):
    if(input=='1'):
        return(filenameinfo(shape[33],shape[57],eps))
    elif(input=='2'):
        return(filenameinfo2(shape[8], middle(shape[21],shape[22]),shape[33],eps))
    elif(input=='3'):
        return(filenameinfo3(shape[0],shape[36],shape[39],shape[42],shape[45],shape[16],eps))
    elif(input=='4'):
        return(filenameinfo4(shape[21],shape[22],eps))
    elif(input=='5'):
        return(filenameinfo4(shape[21],shape[22],eps))
    elif(input=='6'):
        return(filenameinfo4(shape[1],shape[15],eps))
    elif(input=='7'):
        return(filenameinfo4(shape[48],shape[54],eps))
    
  

def result_image(input,rects,shape,eps,image):
    for (i,rect) in enumerate(rects):
    
        #pred=filenameinfo(shape[33],shape[57],eps)
        #pred=filenameinfo2(shape[8], middle(shape[21],shape[22]),shape[33],eps)
        pred=filename_nb(input,shape,eps)
        if(pred==1):
            clr=(0, 255, 0)
            watermark = cv2.imread('SYM.png')
        else:
            clr=(0, 0, 255)
            watermark = cv2.imread('ASYM.png')
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(image, (x, y), (x + w, y + h), clr, 2)
        # Open image with OpenCV
        large_img = image
        small_img = cv2.resize(watermark,(40,30))
        x_offset = x-1
        y_offset = y-29
        x_end = x_offset + small_img.shape[1]
        y_end = y_offset + small_img.shape[0]
        large_img[y_offset:y_end,x_offset:x_end] = small_img
        #large_img
        image= large_img
        return(image)

def facial_symmetry_restingface(x,y,t,z,zz,m,mm,n,nn,a,aa,s,ss,d,dd,image):
    temp=middle(x,y)
    temp,t=extend_line (middle(x,y) ,t , distance = 10000 )
    cv2.line(image, temp, t,(0, 0, 255), lineType=8)
    z,zz=extend_line ( z ,zz , distance = 10000 )
    m,mm=extend_line ( m ,mm , distance = 10000 )
    a,aa=extend_line ( a ,aa , distance = 10000 )
    n,nn=extend_line ( n ,nn , distance = 10000 )
    s,ss=extend_line ( s ,ss , distance = 10000 )
    d,dd=extend_line ( d ,dd , distance = 10000 )
    cv2.line(image,z,zz,(0, 255, 255), lineType=8)
    cv2.line(image,m,mm,(0, 255, 255), lineType=8)
    cv2.line(image,n,nn,(0, 255, 255), lineType=8)
    cv2.line(image,a,aa,(0, 255, 255), lineType=8)
    cv2.line(image,d,dd,(0, 255, 255), lineType=8)
    cv2.line(image,s,ss,(0, 255, 255), lineType=8)

def facial_symmetry_smilingface(x,y,t,image):
    temp=middle(x,y)
    temp,t=extend_line (middle(x,y) ,t , distance = 10000 )
    cv2.line(image, temp, t,(0, 0, 255), lineType=8)


def coupl_sour_symetrie(x,y,t,image):
    o,t=extend_line (x,t , distance = 10000 )
    x,y=extend_line (x,y , distance = 10000 )
    cv2.line(image, o,t,(25, 52, 72), lineType=8)
    cv2.line(image, x,y,(0, 255, 255), lineType=8)
   

def coupl_yeu_symetrie(x,y,t,image):
    o,t=extend_line (x,t , distance = 10000 )
    x,y=extend_line (x,y , distance = 10000 )
    cv2.line(image, o,t,(25, 52, 72), lineType=8)
    cv2.line(image, x,y,(0, 255, 255), lineType=8)
    

def coupl_joue_symetrie(x,y,t,image):
    o,t=extend_line (x,t , distance = 10000 )
    x,y=extend_line (x,y , distance = 10000 )
    cv2.line(image, o,t,(25, 52, 72), lineType=8)
    cv2.line(image, x,y,(0, 255, 255), lineType=8)
   


def coupl_smile_symetrie(x,y,t,image):
    o,t=extend_line (x,t , distance = 10000 )
    x,y=extend_line (x,y , distance = 10000 )
    cv2.line(image, o,t,(25, 52, 72), lineType=8)
    cv2.line(image, x,y,(0, 255, 255), lineType=8)
   