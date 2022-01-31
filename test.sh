#!/bin/bash
#model_name=mseg-3m_480p
model_name=mseg-3m_1080p
model_path=~/mseg/mseg-semantic/mseg-3m.pth
config=~/mseg/mseg-semantic/mseg_semantic/config/test/default_config_1080_ss.yaml
#input_file=~/mseg-semantic/construction_video_trim.mp4
input_file=/home/xzhan2/mseg/mseg-semantic/construction_video_tiny2.mp4
#input_file =/home/xzhan2/mseg/mseg-semantic/input_dir/
python -u ./mseg_semantic/tool/universal_demo.py \
  --config=${config} model_name ${model_name} model_path ${model_path} input_file ${input_file}



