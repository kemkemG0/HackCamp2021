import cv2
from imgProc.imgProc import convertToASCII
from multiprocessing import Pool
import time


def save_all_frames(video_path):
    start_time = time.process_time()
    cap = cv2.VideoCapture(video_path)
    print(video_path)

    if not cap.isOpened():
        print('cannot open')
        return
    n = 0
    frame_list = []
    while True:
        ret, frame = cap.read()
        if ret and n % 5 == 0:
            frame_list.append(frame)
        elif not ret:
            print("elif")
            with Pool(10) as p:
                ret = p.map(convertToASCII, frame_list)
            end_time = time.process_time()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            return ret
        n += 1
