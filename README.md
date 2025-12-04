# APT Ninja

**APT Ninja** is an image-based software framework designed for **automated clustering and analysis of Atom Probe Tomography (APT) data**.
The workflow leverages YOLOv11 model to transform 3D atomic point clouds into 2D image representations for segmentation, classification, and quantitative analysis.

---

## 🧩 1. Introduction

Traditional APT clustering relies on distance-based or density-based methods, which can be sensitive to parameter selection and computationally expensive for large datasets.
**APT Ninja** introduces an **image-based approach** to APT data interpretation, enabling efficient processing, intuitive visualization, and the integration of modern computer vision techniques.  The benefit of this approach is 
speed and accuracy; this compute vision approach outperforms HDBSCAN by as much as two orders of magnitude.

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
- 2D image slices (in xy, yz, and xz orientations) and their corresponding YOLO-style labels  

Scripts and instructions for synthetic data generation have been introduced in detail in a previous GitHub repository: 🔗 [HiPerClust](https://github.com/IdahoLabResearch/HiPerClust)  
A related paper describing the synthetic data generation and workflow has been submitted.

Please cite as:   
```
@misc{github,
  author       = {Tang, Yalei and Bachhav, Mukesh and Anderson, Matthew},
  title        = {{HiPerClust}},
  url          = {https://github.com/IdahoLabResearch/HiPerClust},
  year         = {2025}
}
```
---

## 🧠 3. Model Training 

The **`model_training/`** folder contains the scripts and pretrained models for training the segmentation network.

📁 Contents
- `train.py` – Main training script
- `train.yaml` – Dataset configuration file
- `yolo11n-seg.pt` – Base YOLOv11 segmentation model
- `thick2.pt` – Example trained model weights
- `environment.yml` - List of dependencies

⚙️ Environment Setup  

Before starting, create the conda environment with all required dependencies:
```bash
conda env create -f environment.yml --name env_name
```

Then activate the environment:
```bash
conda activate env_name
```

🚀 Training Notes

Once the environment is set up, modify the train.yaml file to point to your dataset directories, then run:
```bash
python train.py
```
The trained model weights will be saved automatically in the runs/ directory for later inference or fine-tuning.

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
This project is licensed under the AGPL-3.0 license.

Copyright 2025, Battelle Energy Alliance, LLC, ALL RIGHTS RESERVED.

## 6. Authors

- **Yalei Tang**  
  Contact: [yalei.tang@inl.gov](mailto:yalei.tang@inl.gov)

- **Mukesh Bachhav**  
  Contact: [mukesh.bachhav@inl.gov](mailto:vmukesh.bachhav@inl.gov)

- **Matthew W. Anderson**  
  Contact: [matthew.anderson2@inl.gov](mailto:matthew.anderson2@inl.gov)

 
