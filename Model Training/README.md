# YOLOv11 Segmentation Model Training

This repository contains the scripts and configuration files for training a YOLOv11 segmentation model on a custom dataset.
The training was conducted using the **Ultralytics YOLOv11** framework.

---

## 📂 Folder Contents

| File | Description |
|------|--------------|
| `train.py` | Main script to start the training process. |
| `train.yaml` | Dataset configuration file (defines paths to training/validation data). |
| `yolo11n-seg.pt` | Pretrained YOLOv11 segmentation model used as the starting checkpoint. |
| `thick2.pt` | Trained model weights obtained after running `train.py`. |

---

## ⚙️ Requirements

Before running the training script, make sure the following dependencies are installed:

```bash
numpy>=1.24
scipy>=1.10
matplotlib>=3.7
opencv-python>=4.10
torch>=2.4
ultralytics>=8.3
```

---

## 🚀 Usage

1. Prepare the dataset  
    Ensure your dataset is structured according to the YOLO segmentation format and that paths are correctly set in train.yaml.

2. Run training  
```python
python train.py
```
The script will automatically:  
- Load the pretrained model yolo11n-seg.pt  
- Train on the dataset defined in train.yaml   
- Save the resulting model weights (thick2.pt)

3. For evaluation or inference:  
```python
model=YOLO(/path/to/thick2.pt)
results=model(/path/to/images)
```

