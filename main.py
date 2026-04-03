from moviepy import VideoFileClip, AudioFileClip

VIDEO_FORMATS = ["mp4", "avi", "mkv"]
AUDIO_FORMATS = ["mp3", "wav"]


def get_format(filename):
    return filename.split(".")[-1].lower()


def get_type(file_format):
    if file_format in VIDEO_FORMATS:
        return "video"
    elif file_format in AUDIO_FORMATS:
        return "audio"
    else:
        return "unsupported"


# 🎬 Video → Audio OR Video → Video
def handle_video(input_file, output_format):
    video = VideoFileClip(input_file)
    output_file = "output." + output_format

    if output_format in AUDIO_FORMATS:
        audio = video.audio
        audio.write_audiofile(output_file)

    elif output_format in VIDEO_FORMATS:
        video.write_videofile(output_file)

    else:
        print("❌ Invalid output format for video")

    print("✅ Saved as:", output_file)


# 🎧 Audio → Audio
def handle_audio(input_file, output_format):
    audio = AudioFileClip(input_file)
    output_file = "output." + output_format

    if output_format in AUDIO_FORMATS:
        audio.write_audiofile(output_file)
    else:
        print("❌ Cannot convert audio to that format")

    print("✅ Saved as:", output_file)


def convert_media(input_file, output_format):
    input_format = get_format(input_file)
    file_type = get_type(input_format)

    if file_type == "unsupported":
        print("❌ Unsupported input format")
        return

    if input_format == output_format:
        print("⚠️ Input and output formats are same")
        return

    if file_type == "video":
        handle_video(input_file, output_format)

    elif file_type == "audio":
        handle_audio(input_file, output_format)


def main():
    input_file = input("Enter input file (example: video.mp4): ")
    output_format = input("Enter output format (mp3/wav/avi...): ").lower()

    convert_media(input_file, output_format)


if __name__ == "__main__":
    main()