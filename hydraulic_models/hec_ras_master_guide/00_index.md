# 🌊 The Ultimate HEC-RAS Master Guide: From Zero to 2D Hydrodynamics

<div align="center">
  
  ![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-green) ![Estimated Time](https://img.shields.io/badge/Estimated_Time-45%20Minutes-blue) ![Domain](https://img.shields.io/badge/Domain-Hydraulic%20Engineering-orange)


</div>

> 💡 **Welcome to the ultimate command centre for hydraulic modelling.**
> 
> The Hydrologic Engineering Centre's River Analysis System ([HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/)) is the global industry standard for river and floodplain simulation. This multi-part handbook bridges the gap between software operation and engineering physics. It is designed to take you from a blank screen to a professional-grade 2D hydrodynamic simulation.
---

## 📑 Master Syllabus & Navigation

### 🟢 Part 1: Foundations & Setup
*Before touching the software, an engineer must understand the physical forces and data requirements governing the model.*

* **[Chapter 01: Introduction](./01_introduction.md)**
  *Discover the scope of HEC-RAS, its real-world engineering applications, and the difference between hydrologic and hydraulic routing.*
* **[Chapter 02: Installation & Setup](./02_installation_setup.md)**
  *System requirements, software installation, and initialising a clean, error-free working environment.*
* **[Chapter 03: Fundamental Concepts](./03_fundamental_concepts.md)**
  *A deep dive into the physics: the Saint-Venant equations, 1D vs. 2D flow, and the Courant condition.*
* **[Chapter 04: Data Requirements](./04_data_requirements.md)**
  *Sourcing authoritative geospatial data, including Digital Elevation Models (DEMs) and Land Use/Land Cover (LULC) datasets.*

---

### 🟡 Part 2: Core Modelling Workflows
*The transition from raw data to a functioning computational matrix.*

* **[Chapter 05: Interface Overview](./05_interface_overview.md)**
  *Mastering the modular architecture of HEC-RAS: Project, Geometry, Flow, and Plan files.*
* **[Chapter 06: 1D Modelling Workflow](./06_1d_modeling.md)**
  *Building river centerlines, cutting cross-sections, and running steady/unsteady flow profiles.*
* **[Chapter 07: 2D Modelling Workflow](./07_2d_modeling.md)**
  *Generating computational meshes, enforcing breaklines, and running direct precipitation (Rain-on-Grid) simulations.*
* **[Chapter 08: RAS Mapper & Visualisation](./08_ras_mapper.md)**
  *Translating massive binary results into dynamic depth, velocity, and shear stress maps using the integrated GIS environment.*

---

### 🔴 Part 3: Advanced Applications & Troubleshooting
*Bridging the gap between a beginner whose model simply runs, and a professional whose model is accurate.*

* **[Chapter 09: Case Study (Rajkot)](./09_case_study_rajkot.md)**
  *A master-level practical application: Building a coupled 1D/2D urban flood model for the Aji River in Rajkot, Gujarat.*
* **[Chapter 10: Troubleshooting Guide](./10_troubleshooting.md)**
  *The ultimate diagnostic manual for fixing "Matrix Will Not Converge," volume accounting errors, and dry-bed instabilities.*
* **[Chapter 11: Pro Tips & Expert Workflows](./11_pro_tips.md)**
  *Advanced techniques for model calibration, sensitivity analysis, and computational time-step optimisation.*
* **[Chapter 12: Software Integrations](./12_integrations.md)**
  *Coupling HEC-RAS with [QGIS](https://qgis.org/), [HEC-HMS](https://www.hec.usace.army.mil/software/hec-hms/), and satellite Remote Sensing for economic damage assessments.*

---

### 🛠️ Part 4: Repository Management
*How to share massive computational models with the engineering community without breaking version control.*

* **[Chapter 13: GitHub Best Practices](./13_github_practices.md)**
  *Mastering `.gitignore` protocols, Git Large File Storage (LFS), and separating lightweight blueprints from heavy binary results.*
* **[Chapter 14: Conclusion](./14_conclusion.md)**
  *Final thoughts, continuous learning, and exploring the future of 3D hydrodynamics and Python automation.*

---

<div align="center">
  <b>Ready to begin?</b><br><br>
  <a href="./01_introduction.md"><b>Start Chapter 01: Introduction ➡️</b></a>
</div>
