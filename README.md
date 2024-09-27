# YOLO_example
a demo of YOLO Ultralytics

If you want to train the model and maybe give it more epochs or just so how training works, run main.py. You will see if you run main.py that I make a reference to config.yaml. That file gives the paths to the training images and the labels. It is important to keep the file structure like this, with an 'images' folder and a 'labels' folder and a subfolder in each of them called train with the data, YOLO needs it (on my first run I called the folder 'label' and got a major error).

When making annotations, watch out for crazy filenames of images you annotate cause that can cause problems. If I were to do this for real, I would add a script that takes out all special characters and whitespace from training image names. Also make sure you don't have files with the same name but different extension.


TLDR:
You can add your own video to videos and test the the model on your video by running predict_vid.py.
Just change the filename in predict_vid.py to the name of the file you add to videos.
