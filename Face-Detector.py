import cv2
# importing some trained data models 
cardetector = cv2.CascadeClassifier('cardetection.xml')
pedestrian_tracker = cv2.CascadeClassifier('harcascadefullbody.xml')

# chooose image to detect faces
# img= cv2.imread('boy-image.jpg')
# img= cv2.imread('IMG20211102152059.jpg')

# now capturing real time face detection from webcam
webcam = cv2.VideoCapture(0)
# //ager koi video padre to ''aise kerke video chalalo
# iterate foreevr over frames 
while True:
    # read the current frame
    successful_frame_read, frame=webcam.read()
# must convert to gray scale format
# bgr is blue green red channel
    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # detect cars
    face_coordinates = cardetector.detectMultiScale(grayscaled_image)
    # detect pedestrians
    pedestrians_coordinates = pedestrian_tracker.detectMultiScale(grayscaled_image)
   
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)

    for (x,y,w,h) in pedestrians_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),5)    
    
    cv2.imshow('cars and pedestrian tracker' ,frame)
    key=cv2.waitKey(1)
# now pressing key to break through loop instead of force quiting
    if key == 13: # here key i set is enter as ascii code for enter is 13
        break
# detect faces
# print(face_coordinates)
# draw rectangle around the faces

# cv2.rectangle(img,(359,301),(359+525,301+525),(0,255,0),2)
# img ke badd (img,(359,301),(525,525),(0,255,0),2) pehla bracket x aur y axis hain aur dusra x+w aur y+h hai tesra bgr color code hai aur "2" last main thickess bgtara hai 
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("output", 400, 300)  
# cv2.imshow('souvik face detector', img)
# it waits and helps to diplay image and let it exit
# print("code complete")
