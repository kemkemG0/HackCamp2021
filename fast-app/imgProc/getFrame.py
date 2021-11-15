import cv2
import os
from imgProc import convertToASCII

outFiles = []

def save_all_frames(video_path, dir_path='Output', ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    print(video_path)

    if not cap.isOpened():
        print('cannot open')
        return

    os.makedirs(dir_path, exist_ok=True)

    n = 0
    while True:
        ret, frame = cap.read()
        if ret and n % 5 == 0:
            convertToASCII(frame, n, outFiles)
        elif not ret:
            return
        n += 1


if __name__ == "__main__":
    save_all_frames('sampleVideos/sample_Trim.mp4',
                    'Output', 'sample_video_img')
