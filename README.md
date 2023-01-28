# Facial symmetry estimation 
Welcome to the Facial symmetry estimation project! This project uses a pre-trained model to detect facial landmarks and perform facial symmetry detection. It includes several functions that are used to perform different tasks, such as converting bounding boxes to a format compatible with OpenCV, 
converting facial landmarks to a numpy array, and calculating the distance between two points.

## Frontal symmetry
Four points of face components are used: left eye, right eye, and the month
<p align="center" width="100%">
    <img width="30%" src="https://user-images.githubusercontent.com/77071173/215291668-5a2c0398-8477-4338-be7f-88c8015be08c.gif"> 
    <img width="25%" src="https://user-images.githubusercontent.com/77071173/215291508-579fc106-226b-4f5f-9dd5-c9197573e770.png"> 
</p>

## Vertical skeletal symmetry
Using the vertical thirds of the face as shown below, it distinguish Long face vs short face

<p align="center" width="100%">
    <img width="30%" src="https://user-images.githubusercontent.com/77071173/215292018-644d6cc3-13a4-4d63-8e97-18dcd435cf4d.gif"> 
    <img width="20%" src="https://user-images.githubusercontent.com/77071173/215291850-f6086e2f-62e7-4436-a637-8a7d5a1204c2.png"> 
</p>


## Horizontal skeletal symmetry
Using the rule of fifths (middle fifth, medial two fifths,outer two fifths)

<p align="center" width="100%">
    <img width="30%" src="https://user-images.githubusercontent.com/77071173/215292302-35de73b9-6cb6-43bd-85ee-4f6579f252c0.gif"> 
    <img width="17%" src="https://user-images.githubusercontent.com/77071173/215292331-b37ea08f-7677-41c2-9eae-a926add52e5d.png"> 
</p>

## Component symmetry
Compare the left and the right sides in terms of eyebrows, eyes, and cheeks

### Cheeks symetrie 


<p align="center" width="100%">
    <img width="30%" src="https://user-images.githubusercontent.com/77071173/215293034-5ce65557-7b2b-4c22-acd7-0baecef79813.gif"> 
    <img width="17%" src="https://user-images.githubusercontent.com/77071173/215292910-867101e4-66f1-410b-a55f-a93c5f9eaebf.png"> 
</p>

### Eyes symetrie 


<p align="center" width="100%">
    <img width="30%" src="https://user-images.githubusercontent.com/77071173/215293211-57f859ad-dfea-48a4-9959-c9ea98745300.gif"> 
    <img width="17%" src="https://user-images.githubusercontent.com/77071173/215292910-867101e4-66f1-410b-a55f-a93c5f9eaebf.png"> 
</p>

### Eyebrows symetrie


<p align="center" width="100%">
    <img width="30%" src="https://user-images.githubusercontent.com/77071173/215293399-6d97254b-a10a-4583-af47-ea60dd55602d.gif"> 
    <img width="17%" src="https://user-images.githubusercontent.com/77071173/215292910-867101e4-66f1-410b-a55f-a93c5f9eaebf.png"> 
</p>



## Smile symmetry
Compares position of the lips



<p align="center" width="100%">
    <img width="30%" src="https://user-images.githubusercontent.com/77071173/215293737-7f071144-29cb-4cfc-bb58-5eba3dc7ee7d.gif"> 
    <img width="23%" src="https://user-images.githubusercontent.com/77071173/215294403-4b7a9ea7-b52f-4ae4-933b-5ec45d91ade8.png"> 
</p>


## Dependencies

In order to use this program, you will need to have the following packages installed:

- dlib
- CMake
- OpenCV
- imutils


## Usage



The code initializes dlib's HOG-based face detector and creates the facial landmark predictor using a pre-trained model `shape_predictor_68_face_landmarks.dat`. The project can be used to estimate the symmetry of a face in an image or a video.


## File Structure

The `function.py` file contains functions used throughout the program. The functions included in this file are:

- `rect_to_b` : converts a bounding predicted by dlib to the format (x, y, w, h)
- `shape_to_np` : converts facial landmarks to a 2-tuple of (x, y)-coordinates
- `middle` : finds the middle point between two coordinates
- `triangle` : plots a triangle on an image given three coordinates
- `facial_symmetry` : plots two triangles and a line on an image to show facial symmetry
- `diseu` : calculates the euclidean distance between two points
- `extend_line` : extends a line given two points
- `samedist` : checks if the distance between two points is within a certain range of a third point
- `samesidt2` : checks if the distance between two lines is within a certain range
- `smile` : plots a line on an image to show the curvature of a smile


