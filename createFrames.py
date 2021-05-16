import os
import cv2


if not os.path.exists('image_frames'):
    os.makedirs('image_frames')

test_video = cv2.VideoCapture('sample_video1.mp4')

# Count for our frames
frameCnt = 0
frameRate = 100
while True:
    ret, frame = test_video.read()
    if not ret:
        break
    if frameCnt % frameRate == 0:
        # assigning name for our files
        name = './image_frames/frame'+str(int(frameCnt/frameRate))+'.png'
        print("Extracting frames .."+name)

        # Saving frame to .png file
        cv2.imwrite(name, frame)
    frameCnt += 1

test_video.release()
cv2.destroyAllWindows()
