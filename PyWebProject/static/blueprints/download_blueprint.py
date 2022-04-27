from flask import send_file, Blueprint
from pytube import YouTube
import os

blueprint = Blueprint('download', __name__, template_folder='templates')


@blueprint.route('/download/<string:formate>/<string:video_id>')
def dwn(formate, video_id):
    video = YouTube(f"https://youtu.be/{video_id}")
    stream = video.streams
    if formate == 'video':
        dwn_video = stream.filter(only_video=False, mime_type='video/mp4').get_highest_resolution()
        dwn_video.download(output_path='/video_and_music_files', filename='dwn_song.webm')
        send = send_file('/video_and_music_files/dwn_song.webm', mimetype='video/webm')
        # os.remove('/dwn_song.webm')
        return send
    elif formate == 'audio':
        dwn_video = stream.filter(only_audio=True).first()
        dwn_video.download(output_path='/video_and_music_files', filename='dwn_song.mp4')
        send = send_file('/video_and_music_files/dwn_song.mp4', mimetype='audio/mp4')
        # os.remove(os.path.abspath("mydir/myfile.txt"))
        return send