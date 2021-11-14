# import cv2
# import os
# # videoPath = input("Path: ")
# videoPath = "C:\python\C:\python\HackCamp2021\imgProc\sampleVideos\sample.mp4"
# cap = cv2.VideoCapture(videoPath)

# # width
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# # height
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# # number of frame
# count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# #get fps
# fps = cap.get(cv2.CAP_PROP_FPS)

# # print("width:{}, height:{}, count:{}, fps:{}".format(width,height,count,fps))

# def save_frame(video_path, frame_num, result_path):
#     cap = cv2.VideoCapture(video_path)

#     if not cap.isOpened():
#         return

#     os.makedirs(os.path.dirname(result_path), exist_ok=True)

#     cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

#     ret, frame = cap.read()

#     if ret:
#         cv2.imwrite(result_path, frame)

# save_frame('C:\python\C:\python\HackCamp2021\imgProc\sampleVideos\sample.mp4', 100, 'C:\python\HackCamp2021\imgProc\sampleVideoOutput')

import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

save_all_frames('C:\python\HackCamp2021\imgProc\sampleVideos\sample_Trim.mp4', 'HackCamp2021\imgProc\sampleVideoOutput', 'sample_video_img')

save_all_frames('C:\python\HackCamp2021\imgProc\sampleVideos\sample_Trim.mp4', 'HackCamp2021\imgProc\sampleVideoOutput', 'sample_video_img', 'png')