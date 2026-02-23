# 😊 Real-Time Face Emotion Detection

Detect human emotions in real-time using your webcam. This project uses **OpenCV** for face detection and **DeepFace** for emotion analysis, displaying the detected emotion directly on the video feed.

## 🎯 What It Does

- Opens your webcam
- Detects faces in the video feed using Haar Cascade classifier
- Analyzes the detected face for emotions (happy, sad, angry, surprise, fear, disgust, neutral)
- Displays the detected emotion and confidence percentage on screen

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.8 or higher** — [Download here](https://www.python.org/downloads/)
- **pip** — Comes bundled with Python (used to install packages)
- **A working webcam** — Built-in or external

> **Note:** This project runs on CPU. No GPU or CUDA is required.

### Verify Python is Installed

Open a terminal and run:

```bash
python3 --version
```

You should see something like `Python 3.12.x`. If not, install Python first.

## 🚀 Getting Started

Follow these steps to set up and run the project:

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd opencv_face_expression_detection
```

### Step 2: Create a Virtual Environment

A virtual environment keeps the project dependencies isolated from your system Python.

```bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

> After activation, you should see `(venv)` at the beginning of your terminal prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

> ⏳ This may take a few minutes as it downloads TensorFlow and other packages (~500MB).

### Step 5: Run the Application

```bash
python face_emotion_deepface.py
```

A window titled **"Emotion Detection - DeepFace"** will open showing your webcam feed with emotion labels.

### Step 6: Quit the Application

Press the **`q`** key on your keyboard while the webcam window is focused.

## 📁 Project Structure

```
opencv_face_expression_detection/
├── face_emotion_deepface.py          # Main application script
├── haarcascade_frontalface_default.xml # Pre-trained face detection model
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Files excluded from Git
└── README.md                          # This file
```

## 🔧 How It Works

1. **Face Detection** — OpenCV's Haar Cascade classifier scans each video frame to locate faces
2. **Emotion Analysis** — Each detected face is passed to DeepFace, which uses a deep learning model to classify the emotion
3. **Display** — A green bounding box is drawn around the face, and the detected emotion with confidence score is shown above it

```
┌─────────────────────────┐
│  happy (94.2%)          │
│  ┌───────────────────┐  │
│  │                   │  │
│  │     😊 Face       │  │
│  │                   │  │
│  └───────────────────┘  │
│                         │
└─────────────────────────┘
```

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError: No module named 'tf_keras'` | Run `pip install tf-keras` |
| `ERROR: Webcam not accessible` | Make sure your webcam is connected and not being used by another app |
| `Could not find cuda drivers` | This is just a warning, not an error. The app will use CPU instead |
| Font warnings from Qt | These are cosmetic warnings and can be safely ignored |
| Webcam window doesn't appear | Try running from a terminal with display access (not over SSH) |

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `opencv-python` | Webcam access and face detection |
| `deepface` | Emotion recognition using deep learning |
| `tensorflow` | Backend for DeepFace (installed automatically) |

## 📄 License

This project is licensed under the [MIT License](LICENSE).
