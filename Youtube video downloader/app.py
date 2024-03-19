from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

def download_video(url):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download()
        return True
    except Exception as e:
        return False, str(e)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        return render_template('download.html', video=yt)     
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    #video_url = request.args.get('url')
    try:
        download_video(video_url)
        return render_template('download.html', video=YouTube(video_url))
    
    except Exception as e:
        return render_template('download.html', error=str(e))



if __name__ == '__main__':
    app.run(debug=True)

