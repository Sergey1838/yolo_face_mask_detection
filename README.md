# yolo face mask detection
<a href='https://www.kaggle.com/andrewmvd/face-mask-detection' target="_blank">dataset link</a>

1. Run dataset_transformation.py --img <image_size>, by default image size will be 400x400 pixels.

This file will resize all images to specific dimensions and change initial xml annotations so they match new images

2. git clone https://github.com/ultralytics/yolov5 to root directory
3. Run yolo_format_data.py

This script will:
 - split images to train,test and validation
 - create appropriate directory structure in yolov5 directory
 - parce xml annotations and transform them into txt files - standart yolo format annotations
 - create data.yaml
