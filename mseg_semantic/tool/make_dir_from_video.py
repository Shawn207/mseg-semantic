import cv2
import os
"""run the file from mseg-semantic/ directory"""

def make_dir(video_path):
	vidcap = cv2.VideoCapture(video_path)
	ret,frame = vidcap.read()
	frame_idx = 0
	while ret:
		cv2.imwrite(f"./input_dir/frame{frame_idx}.jpg",frame)
		print(f"successfully read frame {frame_idx}")
		frame_idx += 1
		ret,frame = vidcap.read()
	# sort the images
	
print(os.getcwd())
make_dir("./construction_video_tiny2.mp4")
