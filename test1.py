import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


cap = cv2.VideoCapture("Man Skipping.mp4")

while True:
    # It contains a boolean indicating if it was sucessful (ret)
    # It also contains the images collected from the webcam (frame)
    ret, resized = cap.read()
    # resized = cv2.resize(frame,(1280,720))
     
    frameRGB = cv2.cvtColor(resized,cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(resized, results.pose_landmarks, mpPose.POSE_CONNECTIONS) 


    
    cv2.imshow("walking_man", resized)
    
    if cv2.waitKey(1) == ord('q'): #13 is the Enter Key
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows() 



