# for image
# import cv2
# # car image
# img_file = 'cars2.jpg'
# # //our pre trained classifier 
# classifier_file = 'cars.xml'
# # create opencv image
# img = cv2.imread(img_file)

# # convert black and white
# blk_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # Create car classsifier
# car_tracker= cv2.CascadeClassifier(classifier_file)
# # detect multiscale cars
# cars = car_tracker.detectMultiScale(blk_n_white)
# # drawing box around cars
# for (x,y,w,h) in cars:
#         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

# # //showing image
# # cv2.imshow('car detector',img)
# cv2.imshow('car detector',img)
# # dont autoclose
# cv2.waitKey()
# print("code completed")

# for video
import cv2
# car image
# img_file = 'cars2.jpg'
# now capturing real time face detection from webcam
webcam = cv2.VideoCapture(0)
# iterate foreevr over frames 
while True:
    # read the current frame
    successful_frame_read, img=webcam.read()
# //our pre trained classifier 
    classifier_file = 'cars.xml'
    # create opencv image
    # img = cv2.imread(img_file)

    # convert black and white
    blk_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Create car classsifier
    car_tracker= cv2.CascadeClassifier(classifier_file)
    # detect multiscale cars
    cars = car_tracker.detectMultiScale(blk_n_white)
# drawing box around cars
    for (x,y,w,h) in cars:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    cv2.imshow('car detector' , img)
    key=cv2.waitKey(1)
        # now pressing key to break through loop instead of force quiting
    if key == 13: # here key i set is enter as ascii code for enter is 13
        break

# //showing image
# cv2.imshow('car detector',img)
# cv2.imshow('car detector',img)
# dont autoclose
# cv2.waitKey()
print("code completed  it will start tracking now")
