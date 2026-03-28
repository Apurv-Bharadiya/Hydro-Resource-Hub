# 🖥️ Chapter 5: HEC-RAS Interface & Architecture Overview

> 💡 **Pro Tip:** Unlike modern CAD software (such as AutoCAD or Civil3D), where everything happens in a single window, [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) is intentionally **modular**. It mathematically separates the physical earth (Geometry) from the water entering it (Flow). This architecture allows an engineer to build one highly detailed river geometry and test dozens of different storm scenarios against it without duplicating massive terrain datasets.

To master the software, you must understand its four primary control centres and the specific files they generate.

---

## 1. The Modular File Architecture (Crucial for GitHub)

Before clicking any buttons, you must understand how HEC-RAS saves its brain. When you save a project, it does not create one giant file. It creates a web of interconnected text and binary files. 

Understanding this is critical for version control and uploading your model to a repository.

| File Type | Extension | What it Contains | Engineering Purpose |
| :--- | :--- | :--- | :--- |
| **Project File** | `.prj` | File associations and Unit System. | The "glue" that tells the software which Geometry connects to which Flow. |
| **Geometry File** | `.g01`, `.g02` | Cross-sections, 2D meshes, bridges. | The physical container (the river and floodplain). |
| **Flow File** | `.f01` (Steady)<br>`.u01` (Unsteady) | Discharges, hydrographs, boundary conditions. | The water is being pushed through the container. |
| **Plan File** | `.p01`, `.p02` | Computation settings, time steps, tolerances. | The exact simulation settings used to combine a specific Geometry and Flow. |
| **HDF Results** | `.p01.hdf` | Massive binary arrays of depths and velocities. | The actual calculated results are mapped to your 2D grid. (Do **not** upload to GitHub due to size). |

---

## 2. The Main Menu (The Command Hub)

This is the small, rectangular window that opens when you first launch the software. It acts as the central dispatch station.

### Key Workflows in the Main Menu
* **Setting the Unit System:** ⚠️ **CRITICAL STEP.** Before you draw a single line, go to `Options > Unit System` and select **System International (Metric System)**. If you accidentally leave it in US Customary (Feet) and import a Metric DEM from [Bhuvan ISRO](https://bhuvan.nrsc.gov.in/), a 300-meter-wide river will be calculated as a 300-foot-wide river, and your model is ruined.
* **Launching Modules:** The toolbar icons launch the Geometry Editor, Flow Editors, and RAS Mapper.
* **Saving the Project:** When you select `File > Save Project`, it only saves the `.prj` file. You must save Geometry and Flow files separately within their respective editors.

---

## 3. The Geometric Data Editor

This is the classic 1D editor where you construct the physical world. While newer 2D tools exist in RAS Mapper, the Geometric Data Editor remains essential for structural inputs.

### Core Functions
* **River Centerlines & Cross-Sections:** You can manually draw the stream routing and cut cross-sections perpendicular to the flow. 
* **Hydraulic Structures:** This editor is mandatory for adding **Inline Structures** (Dams/Weirs), **Lateral Structures** (Levees that spill water out of the river into a 2D area), and **Bridges/Culverts**.
* **Manning's Roughness ($n$):** You assign friction values directly to your 1D cross-section stations here.

> 📌 **Important Note:** The Geometric Data Editor does not know that water exists. It only processes mathematical station-elevation coordinates (X, Y, Z) and friction. 

---

## 4. The Flow Data Editors (Steady & Unsteady)

This is where you introduce hydrologic forces into your system. 

### The Steady Flow Editor
Used for calculating the absolute maximum water surface elevation of a constant peak discharge.
* **Input:** A single flow rate (e.g., $500 \text{ m}^3/\text{s}$).
* **Boundary Condition:** You must provide a Downstream Boundary condition, typically **Normal Depth**. You calculate this by measuring the average slope of your channel bed over the last few kilometres using [QGIS](https://qgis.org/) or RAS Mapper.

### The Unsteady Flow Editor
Used for dynamic flood routing, dam breaks, and modelling how floodplains store water over time.
* **Input:** Time-series Hydrographs (from external sources like [USGS Water Data](https://waterdata.usgs.gov/nwis)).
* **Boundary Condition:** You apply the hydrograph at the upstream end and a Friction Slope or Stage Hydrograph at the downstream end.
* **Initial Conditions:** You must set a starting flow rate for the entire system to prevent the mathematical matrix from dividing by zero (The "Dry Bed" crash).

---

## 5. RAS Mapper (The GIS Powerhouse)

Introduced in Version 5.0, RAS Mapper fundamentally transformed hydraulic engineering. It is a fully integrated spatial environment built directly into the software, eliminating the heavy reliance on external tools like [ArcGIS Pro](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview) for basic extraction.

### Core Capabilities
1. **Terrain Generation:** You import your raw GeoTIFF DEMs here to create a proprietary HEC-RAS Terrain `.hdf` file. 
2. **2D Mesh Generation:** You draw your 2D Flow Area polygons, generate the computational grid (e.g., $15\text{m} \times 15\text{m}$ cells), and enforce breaklines along elevated roads.
3. **Spatial Manning's $n$:** You import Land Use/Land Cover shapefiles to automatically assign friction values across millions of 2D cells simultaneously.
4. **Results Visualisation:** Once a simulation finishes, RAS Mapper animates the flood wave, allowing you to query water depths, flow velocities, and shear stress at any specific pixel in real-time.

### 🚨 Common Mistake: The Two Geometry Editors
A massive point of confusion for beginners: You can edit geometry in *both* the Geometric Data Editor and RAS Mapper. 
* **The Rule of Thumb:** Use **RAS Mapper** for anything spatial/2D (drawing meshes, breaklines, importing DEMs). Use the **Geometric Data Editor** for anything structural/1D (bridges, culverts, dam gates, weir coefficients). 

<br>

---
**[⬅️ Chapter 04: Data Requirements](./04_data_requirements.md)** | **[🏠 Main Index](./00_index.md)** | **[Chapter 06: 1D Modelling Workflow ➡️](./06_1d_modeling.md)**
