from mseg.utils.mask_utils_detectron2 import VisImage,Visualizer
import mseg.utils.names_utils as names_utils
import os
import cv2
rgb_path = "/home/xzhan2/NYUDatasets/images/val/" 
gray_path = "/home/xzhan2/mseg/mseg-semantic/temp_files/mseg-3m_val_universal_ss/354/gray/"
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
    
#    filename_ind = filename.split("_")[1]
#    print(i,filename,filename_ind)
    cv2.imwrite("./visualizations/nyud/"+filename,output)
#    print("frame ",filename,"has been visualized into rgb with segmentation mask")
