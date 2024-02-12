import cv2
import os

fps = input('Please put the desired fps of the video (usually 24 in this case)\n')
fps = int(fps)

image_folder = input('Please put the file directory or "default" for the default directory (C:\\tmp)\n')

if image_folder == 'default':
    image_folder = (r'C:\\tmp')

video_name = input('Please put the name of the output video\n')
video_name = video_name + '.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

print (images)

video = cv2.VideoWriter(video_name, 0, fps, (width,height))

print (video)

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
    print (image)

cv2.destroyAllWindows()
video.release()