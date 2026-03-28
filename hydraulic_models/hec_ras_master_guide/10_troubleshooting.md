# 🚨 Chapter 10: The Ultimate Troubleshooting Guide

> 💡 **Pro Tip:** 90% of your time in [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) will be spent fixing errors. A model crashing is not a failure; it is the physics engine explicitly telling you that your inputs violate the laws of conservation of mass or momentum. 

Here is the master diagnostic manual for identifying, understanding, and resolving the most common hydraulic modelling failures.

---

## A. The "Matrix Will Not Converge" Error

This is the most terrifying and common error in Unsteady Flow modelling. It means the Saint-Venant equations failed to balance the forces and volumes within the specified tolerances.

### Cause 1: Time Step ($\Delta t$) Too Large
* **The Physics:** The flood wave moved across too many cross-sections or 2D cells in a single computation interval.
* **The Fix:** Cut your Computation Interval in half. If you are running at 1 minute, go to 30 seconds. In extreme 2D urban models, you may need a 2-second to 5-second time step to satisfy the Courant condition.

### Cause 2: Cross-Sections Too Far Apart (1D)
* **The Physics:** If there is a massive drop in channel elevation between two sections spaced 500 meters apart, the software cannot accurately calculate the energy slope between them.
* **The Fix:** Go to the Geometric Data Editor. Use `Tools > XS Interpolation` to automatically generate intermediate cross-sections every 50 meters.

### Cause 3: Bad 2D Mesh Topography
* **The Physics:** A single, infinitely deep spike or "NoData" hole in your DEM causes the computed water velocity to approach infinity, instantly destroying the matrix.
* **The Fix:** Do not fix this in HEC-RAS. Open your original DEM in [QGIS](https://qgis.org/), use the `Fill Sinks` or raster calculator tools to repair the bad pixels, and re-import the terrain into RAS Mapper.

---

## B. The "Dry Bed" Instability

* **The Error:** The model crashes at 0% or 1% computation, often pointing to a specific cross-section.
* **The Physics:** The momentum equation involves dividing by Depth ($D$) and Area ($A$). If your river has absolutely no flow in it, the depth is zero. You cannot mathematically divide by zero.
* **The Fix:** 1. Open the **Unsteady Flow Data** editor.
    2. Go to the **Initial Conditions** tab.
    3. You must establish a "Minimum Flow" or baseline dummy flow (e.g., $5\text{ m}^3/\text{s}$) for every reach in your model. This ensures the channel is mathematically "wet" before the main flood hydrograph arrives.

---

## C. High Volume Accounting Errors

When the simulation finishes, HEC-RAS generates a computation log reporting the "Volume Accounting Error." This tracks exactly how much water entered the system versus how much left or remains stored.

* **The Acceptable Limit:** A legally defensible model should have a volume error of **less than 1%**.
* **If Error is > 2%:** Your model is leaking mathematically. 
    * *Fix 1 (Mesh Refinement):* In 2D models, your cell sizes might be too large near complex, steep terrain. Refine your mesh to a smaller $\Delta x$ around these drops.
    * *Fix 2 (Tolerances):* Go to `Unsteady Flow Analysis > Options > Calculation Options and Tolerances`. Increase the "Water Surface Calculation Tolerance" slightly (e.g., from 0.006m to 0.01m), or increase the "Maximum Number of Iterations" from 20 to 40. This gives the software more attempts to balance the math before giving up.

---

## D. "Glass-Walling" (1D Geometry Errors)

* **The Error:** The model runs successfully, but your mapped flood depths seem insanely high (e.g., 10 meters deep in a small creek).
* **The Physics:** You drew a cross-section that was only 50 meters wide, but the actual flood wave required 200 meters of width to spread out onto the floodplain. Because HEC-RAS cannot push water past the end point of your drawn line, it builds a vertical "glass wall," forcing all that volume straight up into the air.
* **The Fix:** 1. Open the **Cross-Section Plots** and cycle through your stations.
    2. Look for the blue water line touching the absolute vertical edge of the black boundary box. 
    3. If it touches, you must return to the Geometry Editor and physically extend your cross-section line further out into the floodplain.

---

## E. Unstable Downstream Boundaries

* **The Error:** Water artificially pools at the very last cross-section of your river, or the model crashes precisely at the exit point.
* **The Physics:** Your "Normal Depth" friction slope was estimated incorrectly, forcing the model to calculate an artificially high starting water surface, which sends a backwater wave *upstream* into your study area.
* **The Fix:** 1. **Move the Boundary:** The downstream boundary must be far away from your actual area of interest. If you are studying a bridge, your model should extend at least 2 kilometres downstream of that bridge so boundary condition errors do not affect your results.
    2. **Recalculate Slope:** Ensure you calculated the friction slope ($S = \frac{\Delta \text{Elevation}}{\text{Distance}}$) accurately using the channel bed, not the water surface.

<br>

---
<div align="center">
  <a href="./09_case_study_rajkot.md"><b>⬅️ Chapter 09: Case Study (Rajkot)</b></a> | 
  🏠 <a href="./00_index.md"><b>Main Index</b></a> | 
  <a href="./11_pro_tips.md"><b>Chapter 11: Pro Tips & Expert Workflows ➡️</b></a>
</div>
