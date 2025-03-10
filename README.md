# Driver-Drowsiness-Detection

**Introduction**

The Driver Drowsiness Detection System is designed to enhance road safety by detecting signs of driver fatigue and alerting them in real time. The system leverages computer vision techniques using Python and machine learning models to analyze facial features and predict drowsiness.

**Features**

>Real-time video feed analysis.

>Detects eye closure, yawning, and head position to identify drowsiness.

>Audio alert system to notify the driver when signs of fatigue are detected.

>User-friendly interface for easy setup and control.


**Algorithm and Process**

>The system uses a Convolutional Neural Network (CNN) model for detecting facial landmarks.

>The Eye Aspect Ratio (EAR) is calculated to identify closed eyes.

>The Mouth Aspect Ratio (MAR) helps detect yawning.

>When EAR drops below a defined threshold for a set duration, the system triggers an alert.

**Key Libraries Used**

>OpenCV – For image and video processing.

>dlib – For face detection and landmark identification.

>imutils – For facial region alignment.

>pygame – For audio alerts.

**Evaluation Metrics**

>Accuracy: Measures model performance in detecting drowsiness.

>Precision/Recall: Ensures minimal false positives and negatives.

>Response Time: Ensures alerts are triggered promptly.

**Future Enhancements**

>Integration with car control systems for automatic braking or lane correction.

>Adding mobile app integration for enhanced accessibility.

>Improving accuracy under low-light conditions.
