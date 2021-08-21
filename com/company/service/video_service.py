import math
import cv2

path_to_root_folder = "/home/user/videoEditor"


def process_video(file_name_with_format, time_from_in_milliseconds, time_to_in_milliseconds):
    count_of_frames = cut_video_by_frame(file_name_with_format, time_from_in_milliseconds, time_to_in_milliseconds)
    save_video_from_frames(file_name_with_format, count_of_frames)


def cut_video_by_frame(file_name_with_format, time_from_in_milliseconds, time_to_in_milliseconds):
    splitting_by_dots = file_name_with_format.split(".")
    file_name = splitting_by_dots[0]

    path_to_save_folder = path_to_root_folder + "/" + file_name
    path_to_file = path_to_root_folder + "/" + file_name + "/" + file_name_with_format

    cap = cv2.VideoCapture(path_to_file)
    frames_per_second = cap.get(5)

    frame_from = math.floor(time_from_in_milliseconds / 1000 * frames_per_second)
    frame_to = math.floor(time_to_in_milliseconds / 1000 * frames_per_second)

    count_of_frames = frame_to - frame_from

    for i in range(frame_from):
        cap.read()

    for i in range(count_of_frames):
        ret, frame = cap.read()
        cv2.imwrite(f"{path_to_save_folder}/{i}.png", frame)

    return count_of_frames


def save_video_from_frames(file_name_with_format, count_of_frames):
    splitting_by_dots = file_name_with_format.split(".")
    file_name = splitting_by_dots[0]
    file_format = splitting_by_dots[1]
    out_file_name_with_format = file_name + '_edit.' + file_format
    path_to_save_folder = path_to_root_folder + "/" + file_name

    frame_size = (1920, 1080)

    out = cv2.VideoWriter(out_file_name_with_format, cv2.VideoWriter_fourcc(*'mp4v'), 24, frame_size)

    for i in range(count_of_frames + 1):
        filename = path_to_save_folder + '/' + i.__str__() + ".png"
        img = cv2.imread(filename)
        out.write(img)

    out.release()
