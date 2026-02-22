# 🧠 AI Camera Object Detection

This project uses Python, OpenCV, and YOLO (Ultralytics) to detect objects in real time using your webcam.

It will:
- Open your webcam
- Detect objects (person, phone, laptop, chair, etc.)
- Draw boxes around detected objects
- Print detection data to the terminal

---

# 📦 Requirements

You need:

- Python 3.9 – 3.11
- A working webcam
- Internet connection (first run downloads the model)

---

# 📁 Project Structure

```
ai-camera/
│
├── camera_ai.py
├── requirements.txt
└── README.md
```

---

# 🛠 Setup Instructions (Follow Exactly)

## 1️⃣ Install Python

Go to:

https://www.python.org/downloads/

Download Python.

IMPORTANT:
During installation, check the box:

☑ Add Python to PATH

Then click Install.

---

## 2️⃣ Download This Project

Download the project folder and extract it somewhere simple like your Desktop.

Example:

```
Desktop/ai-camera
```

---

## 3️⃣ Open Terminal / Command Prompt

### On Windows:
- Press Windows Key
- Type: `cmd`
- Press Enter

### On Mac:
- Press Command + Space
- Type: `Terminal`
- Press Enter

---

## 4️⃣ Go Into The Project Folder

If it’s on Desktop:

Windows:
```
cd Desktop
cd ai-camera
```

Mac:
```
cd Desktop/ai-camera
```

---

## 5️⃣ Install Dependencies

Run:

```
pip install -r requirements.txt
```

Wait until installation finishes.

---

## 6️⃣ Run The AI Camera

Run:

```
python camera_ai.py
```

Your webcam should open.

Press:

```
Q
```

to quit.

---

# 🧪 What It Detects

YOLO can detect many objects including:

- Person
- Phone
- Laptop
- Bottle
- Chair
- Car
- Dog
- And many more

Detection results are also stored in a variable inside the script.

---

# ⚡ Improve Accuracy

Inside `camera_ai.py`, you can change the model:

```
model = YOLO("yolov8n.pt")  # Fastest
model = YOLO("yolov8m.pt")  # Balanced
model = YOLO("yolov8x.pt")  # Most accurate (slower)
```

You can also increase resolution:

```
results = model(frame, imgsz=1280, conf=0.6)
```

Higher resolution improves small-object detection.

---

# ❌ Troubleshooting

## "python not recognized"
You did not check "Add Python to PATH".
Reinstall Python and check the box.

## Webcam does not open
- Make sure no other app is using the camera
- Check camera permissions in system settings

## Slow performance
- Use `yolov8n.pt` for faster speed
- Close other heavy programs

---

# 🚀 Optional Improvements

You can upgrade this project by adding:

- Object tracking
- Voice output (text-to-speech)
- Detection logging to file
- Custom object filtering
- Training your own custom model

---

# ✅ Done

If everything worked, your AI camera is now running.
Press Q anytime to close it.
