from mseg.utils.mask_utils_detectron2 import VisImage,Visualizer
import mseg.utils.names_utils as names_utils
import os
import cv2
rgb_path = "./data_from_airsim/" 
gray_path = "./temp_files/mseg-3m_480p_data_from_airsim_universal_ss/354/gray/"
rgb_img_dir = os.listdir(rgb_path)
gray_img_dir = os.listdir(gray_path)

for i,filename in enumerate(rgb_img_dir):
    
    rgb_img = cv2.imread(rgb_path+filename)

    gray_img = cv2.imread(gray_path+gray_img_dir[i],cv2.IMREAD_GRAYSCALE)
    vis = Visualizer(rgb_img,None)
    output = vis.overlay_instances(
        label_map = gray_img,
        id_to_class_name_map = 
        {i: classname for i,classname in enumerate(names_utils.get_universal_class_names())}
        )
    
    filename_ind = filename.split("_")[1]
    print(i,filename,filename_ind)
    cv2.imwrite("./visualizations/frame_"+filename_ind+".png",output)
    print("frame ",filename_ind,"has been visualized into rgb with segmentation mask")
