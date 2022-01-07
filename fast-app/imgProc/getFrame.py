import cv2
from imgProc.imgProc import convertToASCII
from multiprocessing import Process, Manager

outFiles = []


def save_all_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    print(video_path)

    if not cap.isOpened():
        print('cannot open')
        return

    n = 0
    with Manager() as manager:
        L = manager.list()
        processes = []
        while True:
            ret, frame = cap.read()
            if ret and n % 5 == 0:
                p = Process(target = convertToASCII, args=(L,frame,n))
                p.start()
                processes.append(p)
            elif not ret:
                for p in processes:
                    p.join()
                L = list(L)
                sorted(L, key = lambda x:x[0])
                L = [ret for _, ret in L]
                return L
            n += 1
