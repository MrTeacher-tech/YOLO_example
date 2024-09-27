from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Load a pretrained model
results = model.train(data="config.yaml", epochs=50)