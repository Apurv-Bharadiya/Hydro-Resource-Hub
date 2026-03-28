# ⚙️ Chapter 2: Installation, System Requirements & Setup

Hydraulic modelling, particularly in 2D, is incredibly computationally expensive. Solving the Saint-Venant equations millions of times across a spatial grid requires a properly configured workstation.

---

## System Requirements

While HEC-RAS *can* run on basic laptops, professional-grade 2D simulations require serious hardware.

* **Operating System:** Windows 10 or 11 (64-bit). *Note: HEC-RAS is not natively supported on macOS or Linux.*
* **Processor (CPU):** High clock speed with multiple cores (e.g., Intel i7/i9 or AMD Ryzen 7/9). HEC-RAS 2D solvers utilise multi-threading heavily.
* **RAM:** Minimum 8GB. **Recommended: 16GB to 64GB.** If your RAM fills up during a 2D mesh generation, the software will crash instantly.
* **Storage:** Fast NVMe SSDs are absolutely critical. 2D results files (.HDF) read and write gigabytes of data per minute. Using an older HDD will bottleneck your simulation time by up to 500%.

## Download and Installation Steps

1. Navigate to the official USACE download portal: [HEC-RAS Downloads](https://www.hec.usace.army.mil/software/hec-ras/download.aspx).
2. Download the latest stable release executable (e.g., HEC-RAS 6.5 Setup).
3. **Right-click the downloaded `.exe` and select "Run as Administrator".** (Failing to do this can prevent HEC-RAS from writing critical temporary files to your `C:\` drive later).
4. Install the software in the default `C:\Program Files (x86)\HEC\HEC-RAS` directory. 

> ⚠️ **Common Mistake:** Always coordinate software versions with your team or academic advisors. HEC-RAS project files (`.prj`) saved in a newer version (e.g., 6.5) **cannot** be opened in an older version (e.g., 5.0.7). Always standardise the version across your project.

## Common Setup Errors and Fixes

### Error 1: "HDF5 file cannot be opened or is locked."
* **The Cause:** HEC-RAS uses HDF5 (Hierarchical Data Format) to store massive mapping datasets. The HDF5 reader physically breaks if there are spaces or special characters anywhere in the folder path.
* **The Fix:** Move your project out of `C:\Users\Name\My Documents\Project 1!`. Create a clean path at the root of your drive: `C:\HEC_Projects\Aji_River_Model\`.

### Error 2: Comma vs. Decimal Regional Settings
* **The Cause:** In some countries, Windows uses a comma (`,`) to denote decimal places (e.g., `3,14`). HEC-RAS is hardcoded to US standards and will interpret commas as thousands separators, destroying your geometry.
* **The Fix:** Go to Windows Control Panel ➡️ Region ➡️ Additional Settings. Change the **Decimal symbol** to a period (`.`) and the **Digit grouping symbol** to a comma (`,`).

<br>

---
<div align="center">
  <a href="./01_introduction.md"><b>⬅️ Chapter 01: Introduction</b></a> | 
  🏠 <a href="./00_index.md"><b>Main Index</b></a> | 
  <a href="./03_fundamental_concepts.md"><b>Chapter 03: Fundamental Concepts ➡️</b></a>
</div>
