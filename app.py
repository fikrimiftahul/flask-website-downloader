from flask import Flask, render_template, request, flash, send_file
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = "Paste secret key"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/download", methods=["POST"])
def download():
    # get video URL from form data
    url = request.form.get("url")
    if not url:
        flash("Please enter a URL.")
        return render_template("index.html")

    # extract video information using yt_dlp
    with yt_dlp.YoutubeDL() as ydl:
        video_info = ydl.extract_info(url, download=False)
        video_filename = video_info["title"] + "." + video_info["ext"]

    # set options for yt_dlp to download video and save it to default download folder
    ydl_opts = {
        "outtmpl": os.path.join(
            os.path.expanduser("~"), "Downloads", video_filename
        )
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # check if video file was successfully downloaded and saved to default download folder
    if not os.path.exists(
        os.path.join(os.path.expanduser("~"), "Downloads", video_filename)
    ):
        flash("Error: Could not download video.")
        return render_template("index.html")

    # send video file as attachment to user
    flash("You have successfully downloaded the video!")
    return send_file(
        os.path.join(os.path.expanduser("~"), "Downloads", video_filename),
        as_attachment=True,
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
