# 🎬 Dynamic Media Converter

A simple yet powerful **media conversion tool** built using Python.
This application allows users to convert video and audio files into different formats using a clean CLI and Streamlit interface.

---

## 🚀 Features

* 🎥 Convert video → audio (mp4 → mp3, wav)
* 🔊 Convert audio → audio (wav → mp3)
* 🔄 Convert video → video (mp4 → avi, mkv)
* 📁 Upload and download files via Streamlit UI
* ⚡ Dynamic format detection
* 🧠 Intelligent conversion logic (type-based decision engine)

---

## 🛠️ Tech Stack

* Python
* MoviePy
* Streamlit
* FFmpeg

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/shaileshgoku/dynamic-media-convertor.git
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚠️ FFmpeg Setup (Required)

MoviePy depends on FFmpeg.

* Download from: https://ffmpeg.org/download.html
* Add FFmpeg to system PATH

Verify installation:

```bash
ffmpeg -version
```

---

## ▶️ Usage

### 🔹 Run CLI version

```bash
python app.py
```

### 🔹 Run Streamlit app

```bash
streamlit run app.py
```

---

## 🧠 How It Works

The application follows a structured pipeline:

```
Input → Detect Format → Classify Type → Decide Action → Convert → Output
```

* Detects file type (video/audio)
* Applies appropriate conversion logic
* Handles unsupported formats gracefully

---

## 💡 Learnings

* Built a real-world file processing pipeline
* Implemented dynamic decision-based logic
* Learned media handling using MoviePy
* Integrated backend logic with Streamlit UI
* Improved debugging and environment setup skills

---

## 🚀 Future Improvements

* Batch file conversion
* Custom output filenames
* Progress bar indicator
* Drag-and-drop UI
* Cloud deployment (Streamlit Cloud / Hugging Face)

---

## 🤝 Contributing

Feel free to fork the repo and submit pull requests.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Shailesh S
Building in public 🚀
