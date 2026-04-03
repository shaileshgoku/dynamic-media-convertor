import streamlit as st
from moviepy import VideoFileClip, AudioFileClip
import os

# Supported formats
VIDEO_FORMATS = ["mp4", "avi", "mkv"]
AUDIO_FORMATS = ["mp3", "wav"]


# Extract format
def get_format(filename):
    return filename.split(".")[-1].lower()


# Classify type
def get_type(file_format):
    if file_format in VIDEO_FORMATS:
        return "video"
    elif file_format in AUDIO_FORMATS:
        return "audio"
    else:
        return "unsupported"


# Conversion logic
def convert_media(input_path, output_format):
    input_format = get_format(input_path)
    file_type = get_type(input_format)

    output_file = f"output.{output_format}"

    if file_type == "unsupported":
        return None, "❌ Unsupported input format"

    if input_format == output_format:
        return None, "⚠️ Input and output formats are same"

    try:
        # 🎬 VIDEO
        if file_type == "video":
            video = VideoFileClip(input_path)

            if output_format in AUDIO_FORMATS:
                audio = video.audio
                audio.write_audiofile(output_file)

            elif output_format in VIDEO_FORMATS:
                video.write_videofile(output_file)

            else:
                return None, "❌ Invalid output format"

        # 🎧 AUDIO
        elif file_type == "audio":
            audio = AudioFileClip(input_path)

            if output_format in AUDIO_FORMATS:
                audio.write_audiofile(output_file)
            else:
                return None, "❌ Cannot convert audio to that format"

        return output_file, "✅ Conversion successful"

    except Exception as e:
        return None, f"❌ Error: {str(e)}"


# 🎯 UI
st.set_page_config(page_title="Media Converter", layout="centered")

st.title("🎬 Dynamic Media Converter")
st.write("Convert video ↔ audio formats easily")

uploaded_file = st.file_uploader(
    "Upload your file",
    type=["mp4", "avi", "mkv", "mp3", "wav"]
)

output_format = st.selectbox(
    "Select output format",
    ["mp3", "wav", "mp4", "avi"]
)

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    # Save file locally
    input_path = f"temp_{uploaded_file.name}"

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    # Convert button
    if st.button("🚀 Convert"):
        with st.spinner("⏳ Converting... please wait"):
            output_file, message = convert_media(input_path, output_format)

        st.info(message)

        # Download result
        if output_file and os.path.exists(output_file):
            with open(output_file, "rb") as f:
                st.download_button(
                    label="⬇️ Download Converted File",
                    data=f,
                    file_name=output_file
                )
