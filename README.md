# APT Ninja

**APT Ninja** is an image-based software framework designed for **automated clustering and analysis of Atom Probe Tomography (APT) data**.
The workflow leverages YOLOv11 model to transform 3D atomic point clouds into 2D image representations for segmentation, classification, and quantitative analysis.

---

## 🧩 1. Introduction

Traditional APT clustering relies on distance-based or density-based methods, which can be sensitive to parameter selection and computationally expensive for large datasets.
**APT Ninja** introduces an **image-based approach** to APT data interpretation, enabling efficient processing, intuitive visualization, and the integration of modern computer vision techniques.

The workflow consists of the following key steps:

1. **3D to 2D Slicing** – The atomic point cloud is sliced and converted into 2D scatter or density images.
2. **Model-Based Segmentation** – A segmentation network YOLOv11 identifies and isolates regions of interest (clusters).
3. **Reconstruction** – Segmented slices are reconstructed back into 3D to analyze cluster morphology, size distribution, and composition.

<p align="center">
    <img src="Images/workflow.png" alt="Image" Width="80%">
    <br>
    <em> Figure 1: Flowchart of the proposed framework. </em>
</p>

---

## 📁 2. Synthetic Data 

The **`synthetic_data/`** folder provides **simulated APT datasets** that mimic real atomic distributions.
These data are used to train and evaluate the segmentation model under controlled conditions with known ground truth.

Contents include:
- Synthetic `.mat` data  
- Corresponding 2D slices and labels
- Link to scripts and instruction for data generation in the README.md

---

## 🧠 3. Model Training 

The **`model_training/`** folder contains the scripts and pretrained models for training the segmentation network.

Contents:
- `train.py` – Main training script
- `train.yaml` – Dataset configuration file
- `yolo11n-seg.pt` – Base YOLOv11 segmentation model
- `thick2.pt` – Example trained model weights

Dependencies include:
```bash
numpy>=1.24
scipy>=1.10
matplotlib>=3.7
opencv-python>=4.10
torch>=2.4
ultralytics>=8.3
```

---

## 🚀 4. Quick Start Example

The Quick Start Example folder demonstrates how to apply the APT Ninja workflow to example data.

It includes:

12cr.pos – Example APT dataset

QuickStart.ipynb – Jupyter Notebook illustrating:  
- **Step 1 Read pos File**  
- **Step 2 Slice and Save**  
- **Step 3 Run Segmentation**  
- **Step 4 Map Masks to Slices**    
- **Step 5 Reconstruct 3-D clusters**  

This example provides an end-to-end overview — from raw data to visualization — allowing new users to quickly understand and reproduce the workflow.

---

## 5. License
This project is licensed under the MIT License. (double check)

Copyright 2025, Battelle Energy Alliance, LLC 

## 6. Authors

- **Yalei Tang**  
  Contact: [yalei.tang@inl.gov](mailto:yalei.tang@inl.gov)

- **Mukesh Bachhav**  
  Contact: [mukesh.bachhav@inl.gov](mailto:vmukesh.bachhav@inl.gov)

- **Matthew W. Anderson**  
  Contact: [matthew.anderson2@inl.gov](mailto:matthew.anderson2@inl.gov)

 
