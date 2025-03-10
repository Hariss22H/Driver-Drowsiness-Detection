import cv2
import dlib
import pyttsx3
from scipy.spatial import distance

# Initialize the pyttsx3 engine for audio alerts
engine = pyttsx3.init()

# Set up camera (0 for default webcam, 1 if using external)
cap = cv2.VideoCapture(0)  # Changed from 1 to 0, adjust as needed

# Initialize face detector and shape predictor
face_detector = dlib.get_frontal_face_detector()
# Update the path to the decompressed shape predictor .dat file
dlib_facelandmark = dlib.shape_predictor(
    r"C:\Users\Asus\Desktop\NNDL_MINIPROJECT\shape_predictor_68_face_landmarks.dat\shape_predictor_68_face_landmarks.dat")

# Function to calculate Eye Aspect Ratio (EAR) for detecting drowsiness
def Detect_Eye(eye):
    poi_A = distance.euclidean(eye[1], eye[5])
    poi_B = distance.euclidean(eye[2], eye[4])
    poi_C = distance.euclidean(eye[0], eye[3])
    aspect_ratio_Eye = (poi_A + poi_B) / (2 * poi_C)
    return aspect_ratio_Eye

# Main loop for processing frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray_scale)

    for face in faces:
        face_landmarks = dlib_facelandmark(gray_scale, face)
        leftEye = []
        rightEye = []

        # Get the coordinates for the right eye (points 42-47)
        for n in range(42, 48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x, y))
            next_point = 42 if n == 47 else n + 1
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

        # Get the coordinates for the left eye (points 36-41)
        for n in range(36, 42):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x, y))
            next_point = 36 if n == 41 else n + 1
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (255, 255, 0), 1)

        # Calculate the EAR for both eyes and average them
        right_Eye = Detect_Eye(rightEye)
        left_Eye = Detect_Eye(leftEye)
        Eye_Rat = round((left_Eye + right_Eye) / 2, 2)

        # Check if EAR is below the drowsiness threshold (e.g., 0.25)
        if Eye_Rat < 0.25:
            cv2.putText(frame, "DROWSINESS DETECTED", (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
            cv2.putText(frame, "Alert!!!! WAKE UP DUDE", (50, 450),
                        cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 212), 3)

            # Trigger audio alert
            engine.say("Alert!!!! WAKE UP DUDE")
            engine.runAndWait()

    # Display the frame
    cv2.imshow("Drowsiness Detector", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(9) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
