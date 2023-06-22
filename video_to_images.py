import cv2
import os

video_path = "C:\Users\yvans\Desktop\PICSPROD\Code\Syngenta_lets_go_and_grow_ADS_Facebook_video_3_1080x1350.mp4"

video = cv2.VideoCapture(video_path)

try:
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print("Couldn't create data directory")

current_frame = 0

while True:
    ret, frame = video.read()

    if ret: #if video still left continue, create images
        name = './data/frame' + current_frame + '.jpg'
        print('Creating ', frame)

        cv2.imwrite(name, frame)
        current_frame+=1
    else:
        break