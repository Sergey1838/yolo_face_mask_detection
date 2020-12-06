# yolo face mask detection
<a href='https://www.kaggle.com/andrewmvd/face-mask-detection' target="_blank">dataset link</a>

1. Run dataset_transformation.py --img <image_size>, by default image size will be 400x400 pixels.

This file will resize all images to specific dimensions and change initial xml annotations so they match new images

2. git clone https://github.com/ultralytics/yolov5 to root directory
3. run "pip install -r requirements.txt" from yolov5 directory
4. Run yolo_format_data.py

This script will:
 - split images to train,test and validation
 - create appropriate directory structure in yolov5 directory
 - parce xml annotations and transform them into txt files - standart yolo format annotations
 - create data.yaml

5. from yolov5 directory run: "python train.py --img <image_size>  --batch <batch_size> --epochs <numbers_of_epochs> --data face_masks_data/data.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --name <name_for_results>". 

--cfg path to yaml file for preferred model. I went with a small model, because of a small dataset

--weights are pretrained weights, you also can run it with randomly initialized --weights ''

For more details about yolov5, check out their [repository](https://github.com/ultralytics/yolov5)
