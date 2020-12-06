# yolo face mask detection
<a href='https://www.kaggle.com/andrewmvd/face-mask-detection' target="_blank">dataset link</a>

1. Download the data, save images and annotations folders to dataset folder.
2. Run dataset_transformation.py --img <image_size>, by default image size will be 400x400 pixels.

This file will resize all images to specific dimensions and change initial xml annotations so they match new images

3. Run yolo_format_annotations.py

This script will parce xml annotations and transform them into txt files - standart yolo format annotations
