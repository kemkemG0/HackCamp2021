import cv2

# videoPath = input("Path: ")
videoPath = "C:\python\HackCamp2021\imgProc\sampleVideos\sample.mp4"
cap = cv2.VideoCapture(videoPath)

# width
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# height
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# number of frame
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

#get fps
fps = cap.get(cv2.CAP_PROP_FPS)

# print("width:{}, height:{}, count:{}, fps:{}".format(width,height,count,fps))

def save_frame(video_path, frame_num, result_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(os.path.dirname(result_path), exist_ok=True)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)

    ret, frame = cap.read()

    if ret:
        cv2.imwrite(result_path, frame)

save_frame('data/temp/sample_video.mp4', 100, 'C:\python\HackCamp2021\imgProc\sampleVideoOutput')