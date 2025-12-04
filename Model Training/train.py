import torch
from ultralytics import YOLO

model=YOLO("yolo11n-seg.pt")

search_space = {
    "lr0": (1e-5, 1e-1),         # initial learning rate
    "momentum": (0.6, 0.98),     # SGD momentum
    "weight_decay": (0.0, 0.001),
    "degrees": (0, 10),          # image rotation
    "scale": (0.5, 1.5),         # image scale
    "shear": (0, 2.0),           # image shear
    "translate": (0, 0.2),       # image translation
    "flipud": (0.0, 1.0),        # vertical flip probability
    "fliplr": (0.0, 1.0),        # horizontal flip probability
}


results=model.train(
    data="train.yaml",
    pretrained=False,
    epochs=100,
    lr0=0.01,
    momentum=0.937,
    weight_decay=0.0005,
    degrees=0,
    scale=0.5,
    shear=0,
    translate=0.1,
    flipud=0,
    fliplr=0.5,
    imgsz=1004
    
)

