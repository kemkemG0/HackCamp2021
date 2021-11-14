import cv2
import os
import numpy as np
from imgProc import convertToASCII

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    print(video_path)

    if not cap.isOpened():
        print('cannot open')
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret and n % 5 == 0:
            convertToASCII(frame, n)
            
            
        elif not ret:
            return
        n += 1


save_all_frames('sampleVideos/sample_Trim.mp4',
                'Output', 'sample_video_img')
