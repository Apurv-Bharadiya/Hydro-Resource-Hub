# 🌊 Chapter 7: The Advanced 2D Modeling Workflow (Rain-on-Grid)

> 💡 **Pro Tip:** Moving from 1D to 2D modeling requires a complete paradigm shift. In 1D, you force water down a predefined pipe (your cross-sections). In 2D, you drop water onto a topographical grid and let the physics engine (gravity, friction, and terrain) decide where it flows. It is essential for urban stormwater routing, complex floodplains, and dam breaches.

This chapter details the absolute cutting-edge of [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) capabilities: Two-Dimensional Hydrodynamics. 

---

## A. The Physics of 2D Flow

Before drawing polygons, you must understand how HEC-RAS solves 2D flow. HEC-RAS offers two different mathematical equation sets for 2D modelling:

1.  **Diffusion Wave Equations (Default):** Calculates flow driven primarily by gravity and friction. It is mathematically stable, computes very fast, and is highly accurate for standard floodplain inundation where water rises slowly.
2.  **Full 2D Saint-Venant (Shallow Water) Equations:** Accounts for turbulence, eddy currents, and the Coriolis effect. 
    * *Why use it?* You MUST switch to the Full Momentum equations if you are modelling a sudden dam break, water hitting a bridge pier at high velocities, or tidal forces. It takes significantly longer to compute but captures complex hydrodynamics.

---

## B. 2D Flow Area Creation

Unlike 1D where you draw a single river line, 2D requires a bounding box.

### 1. Drawing the Polygon
* **How:** Open **RAS Mapper**, right-click `Geometries > 2D Flow Areas`, and select `Add a New 2D Flow Area`. Draw a polygon encompassing your entire study area.
* **Engineering Rule:** Do not draw your 2D area right on the edge of your flood zone. Give the model a "buffer" so the boundary conditions do not artificially force the water behaviour.

### 2. Mesh Generation & Sub-Grid Bathymetry
Once the polygon is drawn, you must generate the computational mesh (the grid).
* **Cell Size ($\Delta x$):** You specify a nominal cell size (e.g., $15\text{m} \times 15\text{m}$). The software generates thousands of computation points.
* **The HEC-RAS Superpower (Sub-Grid Bathymetry):** Unlike other 2D software that averages the elevation of a $15\text{m}$ cell into one flat block, HEC-RAS retains the high-resolution geometry of the underlying DEM from [USGS Earth Explorer](https://earthexplorer.usgs.gov/) or [Bhuvan ISRO](https://bhuvan.nrsc.gov.in/). 
* *Why it matters:* Even if you use a massive $50\text{m}$ cell, HEC-RAS still calculates the exact volume of a small $2\text{m}$ wide drainage ditch running through that cell. This allows you to use larger cells (faster computation) without losing volumetric accuracy.

---

## C. The Secret to 2D: Breaklines

If there is one concept to master in 2D modelling, it is **Breaklines**. 

### The Problem with Automated Grids
Imagine a $20\text{m}$ wide grid cell generated directly on top of a narrow, $5\text{m}$ wide elevated highway. The cell face spans across the highway, connecting the low ground on either side. Mathematically, water will flow right through the cell face, effectively "leaking" through the solid highway embankment.

### The Breakline Solution
* **How:** In RAS Mapper, draw manual Breaklines along the ridges of roads, levees, and riverbanks. 
* **Why:** When you enforce a breakline, HEC-RAS physically snaps the edges of the computational cells directly to the line you drew. This ensures that a cell face perfectly aligns with the top of the levee, forcing water to overtop the actual elevation of the road rather than leaking through the grid.

> ⚠️ **Common Mistake:** Failing to draw breaklines along major infrastructure will completely invalidate an urban flood model. Water will spread everywhere it shouldn't.

---

## D. Urban Flood Modelling (Rain-on-Grid)

Traditional river models push water in from the upstream edge. But what happens in a city where the storm drains overflow before the water even reaches the river?

### 1. Direct Precipitation
Instead of an upstream hydrograph, you apply rainfall directly onto the 2D mesh.
* **How:** In the **Unsteady Flow Data** editor, select `Add a Meteorological Data component`. You can input a Precipitation Hyetograph (e.g., $150\text{mm}$ of rain over 24 hours).
* **The Result:** HEC-RAS will literally "rain" onto every single cell in your 2D mesh. The water will pool in low-lying intersections and naturally route itself down the streets based entirely on the topography.

### 2. Infiltration (Where does the water go?)
If you rain $150\text{mm}$ onto a concrete city, most of it runs off. If you rain it onto a forest, the soil absorbs it. 
* **How:** You must attach Land Use / Land Cover (LULC) data (prepared in [QGIS](https://qgis.org/)) to your 2D mesh, and apply a Deficit and Constant infiltration method. This tells HEC-RAS to subtract water from the grid where the soil is permeable.

---

## E. Computational Stability: The Courant Condition

2D Unsteady models are highly prone to mathematical explosions. If you run a model and the water violently sloshes back and forth at $50\text{m/s}$, your matrix has failed.

To keep a 2D model stable, your Computational Time Step ($\Delta t$) and your Cell Size ($\Delta x$) must satisfy the **Courant Condition**:

$$C = \frac{V \Delta t}{\Delta x} \le 1.0$$

*(Where $V$ is the expected flood wave velocity in m/s).*

### How to balance the Courant Number:
1.  **Estimate Velocity:** If water is moving at $2\text{m/s}$.
2.  **Check Cell Size:** If your grid cells are $10\text{m}$ wide.
3.  **Calculate Time Step:** $2 \times \Delta t / 10 = 1.0$. Your maximum allowable time step is **5 seconds**. 
4.  *If you attempt to run this model at a 1-minute time step, it will instantly crash because the water tries to travel across 12 cells in a single computation.*

### 🚨 The Ultimate 2D Troubleshooting Rule
If your 2D model crashes with a "Matrix will not converge" error, **cut your computation time step in half** and run it again.

<br>

---
<div align="center">
  <a href="./06_1d_modeling.md"><b>⬅️ Chapter 06: 1D Modelling Workflow</b></a> | 
  🏠 <a href="./00_index.md"><b>Main Index</b></a> | 
  <a href="./08_ras_mapper.md"><b>Chapter 08: RAS Mapper & Visualisation ➡️</b></a>
</div>
