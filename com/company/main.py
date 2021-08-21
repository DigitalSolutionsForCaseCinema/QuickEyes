from flask import Flask, request

from com.company.service import video_service

app = Flask(__name__)

@app.route('/download_video')
def download_video(text):
    return text


@app.route('/process_video')
def process_video():
    file_name_with_format = request.args.get('file_name_with_format')
    time_from_in_milliseconds = request.args.get('time_from_in_milliseconds', type=int)
    time_to_in_milliseconds = request.args.get('time_to_in_milliseconds', type=int)

    video_service.process_video(file_name_with_format, time_from_in_milliseconds, time_to_in_milliseconds)

    return "The operation was ended"

if __name__ == "__main__":
    app.run()
