# 💤 Driver Drowsiness Detection System

> Real-time drowsiness alerting system using computer vision and speech synthesis to enhance road safety.



## 📌 Features
- Real-time eye aspect ratio (EAR) analysis
- Detects drowsiness using facial landmarks
- Visual alerts on screen
- Audio alerts using text-to-speech engine

---

## 🧠 How It Works
- Uses **Dlib**'s 68-point facial landmark predictor.
- Calculates **Eye Aspect Ratio (EAR)** for both eyes.
- Triggers alert when EAR < `0.25` for a sustained time.

---

## 🛠️ Requirements

Install all dependencies with:
```bash
pip install 
opencv-python
dlib
pyttsx3
scipy
imutils
```


---
## 🗂️ Project Structure
```bash
Drowsiness-Detection/


├── main.py   # Main detection script
│
├── requirements.txt # List of dependencies
│
├── shape_predictor_68_face_landmarks.dat # Dlib 68-point facial landmark model
│
├── dataset/ # Optional: Test images or video samples
│
├── utils/ # Helper functions (EAR calculation, etc.)
│
├── resources/ # Alert sounds, icons, and assets
│
└── README.md # Project documentation
```

---
## ▶️ Usage
Clone the repository:

git clone [https://github.com/yourusername/drowsiness-detection](https://github.com/Hariss22H/Driver-Drowsiness-Detection)

Download the dlib shape predictor from here, extract it and place in the project directory.

Run the detection:
python main.py

Press q to exit the program.

---

## 📈 Metrics
EAR Threshold: 0.25

Real-time feedback speed: ~30 FPS (depends on webcam)

Accuracy: High in good lighting conditions

---

## 🔮 Future Improvements
Adaptive threshold tuning using ML

Night vision support

Yawning detection via mouth aspect ratio

Mobile deployment

---

## 👨‍💻 Author

**Shaik Harriss Razvi**  
Student @ Alliance University  
Machine Learning & OpenCV Enthusiast  

🔗 [LinkedIn](https://www.linkedin.com/in/hariss-razvi-shaik-31b037333/) 
