from flask import Flask, render_template, request, send_file
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import uuid

app = Flask(__name__)

# Set max file upload (e.g., 100MB)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "video" not in request.files or "audio" not in request.files:
            return render_template("index.html")

        video_file = request.files["video"]
        audio_file = request.files["audio"]

        if video_file.filename == "" or audio_file.filename == "":
            return render_template("index.html")

        try:
            # Save temporary files
            video_path = f"static/{uuid.uuid4()}.mp4"
            audio_path = f"static/{uuid.uuid4()}.mp3"
            output_path = f"static/merged/{uuid.uuid4()}_merged.mp4"

            video_file.save(video_path)
            audio_file.save(audio_path)

            # Merge using moviepy
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)

            final_clip = video_clip.set_audio(audio_clip)
            final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

            final_clip.close()
            video_clip.close()
            audio_clip.close()

            # Cleanup source files
            os.remove(video_path)
            os.remove(audio_path)

            return send_file(output_path, as_attachment=True)
        except Exception:
            for path in [locals().get('video_path'), locals().get('audio_path')]:
                if path and os.path.exists(path):
                    os.remove(path)
            return render_template("index.html")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
