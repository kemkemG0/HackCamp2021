import cv2
from imgProc.imgProc import convertToASCII
import time
outFiles = []


def save_all_frames(video_path, dir_path='Output', ext='jpg'):
    start_time = time.perf_counter()
    out = []
    cap = cv2.VideoCapture(video_path)
    print(video_path)

    if not cap.isOpened():
        print('cannot open')
        return

    n = 0
    while True:
        ret, frame = cap.read()
        if ret and n % 5 == 0:
            out.append(convertToASCII(frame, n))
        elif not ret:
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(elapsed_time)
            return out
        n += 1
