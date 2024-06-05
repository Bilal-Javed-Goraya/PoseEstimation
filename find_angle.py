import cv2
import PoseModule as pm
import csv
import time

# Initialize video capture and pose detector
cap = cv2.VideoCapture("Zohaib.mp4")
detector = pm.poseDetector()

# CSV file setup
csv_file = "angles.csv"
fields = ['Frame', 'Timestamp', 'left_elbow','right_elbow', 'left_knee', 'right_knee', 'left_shoulder','right_shoulder','left_hip','right_hip']
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    resized = cv2.resize(frame, (400, 600))
    resized1 = detector.findPose(resized)
    lmList = detector.findPosition(resized, draw=False)
    
    if len(lmList) != 0:
        try:
            left_elbow = detector.findAngle(resized1, 11, 13, 15)
            right_elbow = detector.findAngle(resized1, 12, 14, 16)
            left_knee = detector.findAngle(resized1, 23, 25, 27)
            right_knee = detector.findAngle(resized1, 24, 26, 28)
            left_shoulder = detector.findAngle(resized1, 12, 11, 13)
            right_shoulder = detector.findAngle(resized1, 11, 12, 14)
            left_hip = detector.findAngle(resized1, 11, 23, 25)
            right_hip = detector.findAngle(resized1, 12,24,26)


            # Print angles for debugging
            print(f"Frame {frame_count}: Angles: {left_elbow}, {right_elbow}, {left_knee}, {right_knee},{left_shoulder},{right_shoulder},{left_hip},{right_hip}")
            
            # Check if angles are valid numbers before writing to CSV
            if all(isinstance(angle, (int, float)) for angle in [left_elbow,right_elbow, left_knee, right_knee, left_shoulder,right_shoulder,left_hip,right_hip]):
                current_time = time.time()
                
                # Save angles to CSV for each frame
                with open(csv_file, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([frame_count, current_time, left_elbow,right_elbow, left_knee, right_knee, left_shoulder,right_shoulder,left_hip,right_hip])
            else:
                print("Invalid angle detected, skipping this frame.")

        except Exception as e:
            print(f"Error calculating angles: {e}")

    else:
        print(f"No landmarks detected for frame {frame_count}.")
    
    cv2.imshow("biceps", resized1)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    frame_count += 1

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
