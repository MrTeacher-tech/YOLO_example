# YOLO_example
a demo of YOLO Ultralytics

I couldn't fit the videos I used for training on github but I was able to add my model so you can test it out. I also added my data folder so you can see the file structure needed to train a yolo model. I included one image and one annotation (exported as YOLO1.1 from cvat.ai). Of course, my real images/train has all my training images and my real labels/train has all my training data.

When making annotations, watch out for crazy filenames of images you annotate cause that can cause problems. If I were to do this for real, I would add a script that takes out all special characters and whitespace from training image names. Also make sure you don't have files with the same name but different extension.


TLDR:
You can add your own video to videos and test the the model on your video by running predict_vid.py.
Just change the filename in predict_vid.py to the name of the file you add to videos.
