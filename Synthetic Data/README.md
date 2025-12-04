# Synthetic Datasets

This folder contains 80 synthetic atom probe tomography (APT) point cloud datasets in .mat format. These datasets are ideal for testing clustering algorithms and training machine learning models, as they include ground truth labels—eliminating the need for manual annotation.  

Each dataset simulates APT data with varying chromium (Cr) concentrations, background noise levels, and clustering behaviors.

Each .mat file contains an array of shape (N, 4):  
[x, y, z, label]  
* x, y, z → 3D coordinates
* label → atom type (0 = Fe matrix, 1 = Cr cluster atom, etc.)

## 📂 Dataset Groups

### Synthetic Data 1–20  
* File names: Synthetic_1.npy … Synthetic_20.npy  
* Volume dimensions: 120 × 120 × 140  
* Total points: ~10,000,000  
* Cr percentage: 9%  
* Density: 8.5 × 10²² /m³ (±0.1 × 10²²)  
* Clusters: 50  
* Cluster radii (nm): ~2.4 ± 0.2 (x, y), 2.4 ± 0.1 (z)  
* Min cluster separation: 5 nm  

### Synthetic Data 21–40  
* File names: Synthetic_21.npy … Synthetic_40.npy  
* Volume dimensions: 80 × 80 × 80  
* Total points: ~7,000,000  
* Cr percentage: 12%  
* Density: 9.5 × 10²³ /m³ (±0.2 × 10²³)  
* Clusters: 100  
* Cluster radii (nm): ~1.5 ± 0.2 (x, y), 1.5 ± 0.1 (z)  
* Min cluster separation: 5 nm

### Synthetic Data 41–60  
* File names: Synthetic_41.npy … Synthetic_60.npy  
* Volume dimensions: 80 × 80 × 140  
* Total points: ~10,450,000  
* Cr percentage: 15%  
* Density: 3.2 × 10²⁴ /m³ (±0.3 × 10²⁴)  
* Clusters: 500  
* Cluster radii (nm): ~1.3 ± 0.1 (x, y), 0.4 ± 0.01 (z)  
* Min cluster separation: 2 nm

### Synthetic Data 61–80  
* File names: Synthetic_61.npy … Synthetic_80.npy  
* Volume dimensions: 80 × 80 × 140  
* Total points: ~10,000,000  
* Cr percentage: 18%  
* Density: 5.3 × 10²⁴ /m³ (±0.5 × 10²⁴)  
* Clusters: 700  
* Cluster radii (nm): ~1.2 ± 0.1 (x, y), 0.5 ± 0.01 (z)  
* Min cluster separation: 5 nm  

To generate additional synthetic datasets, refer to the [Step1_Synthetic_APT_Data_Generation](https://github.com/IdahoLabResearch/HiPerClust/tree/main/Step1_Synthetic_APT_%20Data_Generation) folder, which contains the necessary scripts and instructions.

## 💬 Feedback  
We welcome feedback to improve these datasets!  
Found an issue or inconsistency?  
* Have suggestions for additional synthetic cases (e.g., different latttice constant, detection efficiency, delocalization)?  
* Want to create realistic, customizable datasets tailored to your research?  

👉 Please open an [issue](https://github.com/IdahoLabResearch/HiPerClust/issues) in this repository.

Your feedback will help us refine and expand future versions of the dataset.

