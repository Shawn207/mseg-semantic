#!/bin/bash
model_name=mseg-3m_480p
model_path=~/mseg/largeFiles/mseg-3m_480p.pth
config=~/mseg/mseg-semantic/mseg_semantic/config/test/480/default_config_batched_ss.yaml
#input_file=~/mseg-semantic/construction_video_trim.mp4
#input_file=/home/xzhan2/mseg/mseg-semantic/construction_video_tiny2.mp4
#input_file =/home/xzhan2/mseg/mseg-semantic/input_dir
input_file=~/mseg/mseg-semantic/data_from_airsim
python -u ./mseg_semantic/tool/universal_demo_batched.py \
  --config=${config} native_img_h 480 native_img_w 640 model_name ${model_name} model_path ${model_path} input_file ${input_file}
