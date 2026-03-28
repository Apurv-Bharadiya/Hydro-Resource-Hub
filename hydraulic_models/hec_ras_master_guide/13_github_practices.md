# 🐙 Chapter 13: GitHub Best Practices for Hydraulic Models

> 💡 **Pro Tip:** [GitHub](https://github.com/) was built for software engineers writing lightweight lines of text. It was *not* built for Water Resources Engineers generating 50-Gigabyte binary flood simulation results. If you attempt to drag-and-drop a raw [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) project folder directly into a repository, it will immediately reject your upload, crash your commit, and lock your repository.

To build a professional, open-source engineering portfolio, you must master the art of version control for computational fluid dynamics. This chapter teaches you how to decouple your lightweight mathematical "inputs" from your massive computational "outputs."

---

## A. The Anatomy of HEC-RAS Files (What to Keep vs. Toss)

GitHub has a strict file size limit of **100 MB per file**. A typical 2D HEC-RAS Unsteady Flow result file (`.p01.hdf`) for an urban grid easily exceeds 5 GB. You absolutely cannot push result files to GitHub. 

You must only push the "Blueprint" (the inputs). This allows other engineers to download your repository and click "Compute" on their own machines to regenerate the heavy results locally.

### 🟢 Files You MUST Upload (The Blueprint)
These are lightweight text and XML files that define the physics and geometry of your model.
* **`.prj` (Project File):** The master directory file.
* **`.g01`, `.g02` (Geometry Files):** Contains your 1D cross-section coordinates, 2D mesh boundary coordinates, and Manning's $n$ values.
* **`.f01`, `.u01` (Flow Files):** Contains your steady discharges or unsteady time-series hydrographs.
* **`.p01`, `.p02` (Plan Files):** Contains your computational time-step settings and matrix tolerances.
* **`.b01` (Boundary Conditions):** Tied directly to unsteady flow data.

### 🔴 Files You MUST EXCLUDE (The Bloat)
* **`*.p01.hdf` (Plan HDF):** The massive binary results file containing every velocity and depth calculation. 
* **`*.g01.hdf` (Geometry HDF):** The processed 2D mesh properties. (Users can easily regenerate this on their own machine by opening RAS Mapper and hitting save).
* **`.comp` & `.log` (Computation Logs):** Temporary text files generated during an active run.
* **Raw `.tif` DEMs > 100MB:** If your terrain is massive, do not push it directly to the repository.

---

## B. The HEC-RAS `.gitignore` Masterclass

The only professional way to prevent accidental uploads of massive files is to use a `.gitignore` file. 

**Step-by-Step Implementation:**
1. Create a new file named exactly `.gitignore` in the root (main) directory of your repository.
2. Paste the following HEC-RAS specific exclusions into it:

```text
# Ignore HEC-RAS Temporary & Computation Files
*.comp
*.log
*.bco
*.b01.bak
*.g01.bak

# Ignore HEC-RAS Massive Binary HDF Files
# (This prevents 50GB results from crashing your GitHub upload)
*.hdf

# Ignore specific heavy result and geometry caching files
*.p*.hdf
*.g*.hdf
*.x*.hdf

# Ignore GIS heavy raster files (Host these externally)
*.tif
*.flt
*.vrt
```

---

## C. Handling Massive Geospatial Data

If your Digital Elevation Model (DEM) from [USGS Earth Explorer](https://earthexplorer.usgs.gov/) or [Bhuvan ISRO](https://bhuvan.nrsc.gov.in/) is 500 MB, you have two professional options for sharing it:

### Option 1: Git Large File Storage (LFS)
[Git LFS](https://git-lfs.com/) is an official extension for GitHub that replaces large files with tiny text pointers inside your repository, while storing the actual massive file contents on a remote server. 
* *Why use it:* Best if you want the user to be able to clone the `.tif` directly with the repository command without leaving GitHub.

### Option 2: Cloud Data Hosting (The Scientific Standard)
Do not treat GitHub as a cloud hard drive. Host your massive terrain and LULC datasets on dedicated scientific data repositories like [Zenodo](https://zenodo.org/) (which grants your dataset a citable DOI for research papers) or [Kaggle](https://www.kaggle.com/). 
* *The Workflow:* Upload your 500MB DEM to Zenodo. In your GitHub `README.md`, provide a direct download link: *"Please download the required Bare-Earth DEM from this Zenodo link and place it in the `/gis_data/` folder before opening the HEC-RAS project."*

---

## D. Structuring a Professional Hydraulic Repository (The 60-Second Rule)

An open-source hydraulic model should be organised so that a visiting engineer, an academic advisor, or a regulatory reviewer can understand your exact data pipeline in under 60 seconds. 

Never dump all your files into a single root folder. HEC-RAS is notoriously messy and generates dozens of temporary files during a run. You must strictly isolate your raw geospatial data from your computational sandbox. 

Adopt this exact folder hierarchy for all professional modelling repositories:

```text
Aji-River-Flood-Model/
├── .gitignore                 <-- Your exclusion rules (Mandatory)
├── README.md                  <-- The Executive Summary & visual maps
├── /docs/                     <-- Technical reports, damage assessments (PDFs)
├── /gis_data/                 
│   ├── /terrain/              <-- Clipped DEMs (Hosted via Git LFS or Zenodo)
│   └── /land_cover/           <-- Shapefiles processed in QGIS
├── /hydrology_inputs/         <-- HEC-HMS outputs, CWC gauge data (.csv or .dss)
├── /hec_ras_model/            <-- ONLY the lightweight .prj, .g01, .p01 files
└── /results_visuals/          <-- Exported flood maps (.png, .gif) for the README
```

---

## E. The "Reproducible Model" README Documentation

Your repository's `README.md` is the front page of your engineering portfolio. A professional hydraulic README must prove the validity of your work instantly.

### 1. The Executive Summary
What river is this? What is the flood event? (e.g., "1D/2D Coupled Simulation of the 100-Year Return Period Flood on the Aji River, Rajkot.")

### 2. Adding Visual Proof (GIFs and PNGs)
No one wants to download a model if they do not know what it looks like. 
* **Action:** Export a static PNG of your Maximum Depth map from RAS Mapper, or use screen-recording software to create a 5-second `.gif` of the flood wave routing through the city.
* **Markdown Implementation:** Embed it directly into your README using: `![Aji River Flood Wave](./results_visuals/flood_animation.gif)`

### 3. Physical Parameters & Assumptions
State the mesh resolution (e.g., $15\text{m} \times 15\text{m}$), the governing equations used (Diffusion Wave vs. Full Momentum), the Manning's $n$ values, and the computation time step ($\Delta t$).

### 4. How to Run the Model (Step-by-Step)
Provide explicit, idiot-proof instructions for the user. 
* *Example:* 1. Clone this repository to your local `C:\` drive (avoid long paths). 
  2. Download the external DEM from Zenodo and place it in `/gis_data/`.
  3. Open `Aji_River_Model.prj` in HEC-RAS v6.3.1. 
  4. Open RAS Mapper to ensure the terrain path is successfully connected. 
  5. Select Flow Plan 01 and hit Compute.

<br>

---
**[⬅️ Chapter 12: Software Integrations](./12_integrations.md)** | **[🏠 Main Index](./00_index.md)** | **[Chapter 14: Conclusion ➡️](./14_conclusion.md)**
