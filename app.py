import os

from flask import Flask, render_template, request, url_for
from pytube import YouTube

app = Flask(__name__)
DOWNLOAD = os.path.join("\\static\downloads")


def getexect(url):
    exact_url = "https://youtu.be/" + url
    return exact_url;


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/download", methods=["post"])
def getvideo():
    """
    this gets the users requested
    :return:
    """
    video = request.form["videoid"]
    myVIdeo = getexect(video)
    target = YouTube(myVIdeo).streams.first().download(DOWNLOAD)
    videDownload = "".join(target)
    return url_for("index")


@app.route("/downloads")
def showDownload():
    import os
    downloadlist = os.walk(DOWNLOAD)
    return  render_template("downloads.html", filename="static", downloadlist=downloadlist)



if __name__ == '__main__':
    app.run()
