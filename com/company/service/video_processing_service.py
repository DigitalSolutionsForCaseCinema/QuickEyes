import math
import os

import cv2
from com.company.repository import video_processing_repository

frame_size = (1920, 1080)
path_to_root_folder = "/home/user/videoEditor"


def process_video(file_name_with_format, time_from_in_seconds, time_to_in_seconds):
    video_processing_id = video_processing_repository\
        .insert(file_name_with_format, time_from_in_seconds, time_to_in_seconds)
    count_of_frames, frame_rate = cut_video_by_frame(file_name_with_format, time_from_in_seconds,
                                                     time_to_in_seconds, video_processing_id)
    save_video_from_frames(file_name_with_format, video_processing_id, count_of_frames, frame_rate)


def cut_video_by_frame(file_name_with_format, time_from_in_seconds, time_to_in_seconds, video_processing_id):
    video_processing_repository.set_status(video_processing_id, 'in_process')

    path_to_save_folder = get_path_to_save_folder(file_name_with_format, video_processing_id)
    create_folder(path_to_save_folder)

    video_capture = get_video_capture(file_name_with_format)

    frame_rate = get_frame_rate(video_capture)

    frame_from = get_frame(time_from_in_seconds, frame_rate)
    frame_to = get_frame(time_to_in_seconds, frame_rate)

    count_of_frames = frame_to - frame_from + 1

    for i in range(frame_from - 1):
        video_capture.read()

    for i in range(count_of_frames):
        ret, frame = video_capture.read()
        cv2.imwrite(f"{path_to_save_folder}/{i}.png", frame)

    return count_of_frames, frame_rate


def get_path_to_save_folder(file_name_with_format, video_processing_id):
    file_name = get_filename_by_filename_with_format(file_name_with_format)
    return path_to_root_folder + "/" + file_name + "/" + video_processing_id


def get_filename_by_filename_with_format(file_name_with_format):
    splitting_by_dots = file_name_with_format.split(".")
    return splitting_by_dots[0]


def create_folder(path_to_folder):
    if not os.path.exists(path_to_folder):
        os.makedirs(path_to_folder)


def get_video_capture(file_name_with_format):
    path_to_video = get_path_to_video(file_name_with_format)
    return cv2.VideoCapture(path_to_video)


def get_path_to_video(file_name_with_format):
    file_name = get_filename_by_filename_with_format(file_name_with_format)
    return path_to_root_folder + "/" + file_name + "/" + file_name_with_format


def get_frame_rate(video_capture):
    return video_capture.get(5)


def get_frame(time_in_seconds, frame_rate):
    return math.floor(time_in_seconds * frame_rate)


def save_video_from_frames(file_name_with_format, video_processing_id, count_of_frames, frame_rate):
    out_file_name_with_format = get_out_filename_with_format(file_name_with_format)
    path_to_save_folder = get_path_to_save_folder(file_name_with_format, video_processing_id)

    out = cv2.VideoWriter(out_file_name_with_format, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, frame_size)

    for i in range(count_of_frames + 1):
        filename = path_to_save_folder + '/' + str(i) + ".png"
        img = cv2.imread(filename)
        out.write(img)

    out.release()
    video_processing_repository.set_status(video_processing_id, 'processed')


def get_out_filename_with_format(file_name_with_format):
    file_name = get_filename_by_filename_with_format(file_name_with_format)
    file_format = get_format_by_filename_with_format(file_name_with_format)
    return file_name + '_edit.' + file_format


def get_format_by_filename_with_format(file_name_with_format):
    splitting_by_dots = file_name_with_format.split(".")
    return splitting_by_dots[1]


def get_all_with_status(status):
    return video_processing_repository.select_all_with_status(status)
