from flask import Flask, request, jsonify

from com.company.service import video_processing_service

app = Flask(__name__)


@app.route('/process-video')
def process_video():
    file_name_with_format = request.args.get('file_name_with_format')
    time_from_in_seconds = request.args.get('time_from_in_seconds', type=int)
    time_to_in_seconds = request.args.get('time_to_in_seconds', type=int)

    if time_from_in_seconds is None:
        time_from_in_seconds = 0
    if time_to_in_seconds is None:
        time_to_in_seconds = -1

    if time_to_in_seconds <= time_from_in_seconds and time_to_in_seconds != -1:
        return "time_from_in_seconds should be less than time_to_in_seconds", 400

    video_processing_service.process_video(file_name_with_format, time_from_in_seconds, time_to_in_seconds)
    return "The operation was ended"


@app.route('/video-processing')
def get_video_processing_with_status():
    status = request.args.get('status')
    return jsonify(video_processing_service.get_all_with_status(status))


if __name__ == "__main__":
    app.run()
