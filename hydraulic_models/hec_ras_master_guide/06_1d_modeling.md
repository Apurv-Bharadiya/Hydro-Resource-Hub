# 📏 Chapter 6: The 1D Modeling Workflow (Steady & Unsteady)

> 💡 **Pro Tip:** 1D modelling is computationally fast and highly accurate for confined river channels. However, a 1D model is completely blind to anything between the cross-sections you draw. The software mathematically interpolates the space between Section A and Section B. If you space them too far apart, the energy equation will fail to converge.

This chapter walks you through the core modeling sequence: from initializing a blank project to analyzing the final water surface profiles.

---

## A. Creating a New Project

Before drawing a single line, you must establish a strict file architecture. [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) generates dozens of auxiliary files during a simulation.

### 1. File Setup & Naming Conventions
1. Open HEC-RAS and navigate to `File > New Project`.
2. **Naming Rule:** Never use spaces or special characters in your project name or folder path. HDF5 result files will fail to read/write if they encounter a space. 
   * ❌ *Bad:* `C:\My Documents\Aji River Model 100 yr flood.prj`
   * ✅ *Good:* `C:\HEC_Projects\Aji_River_100yr\Aji_River_Model.prj`

### 2. GitHub-Friendly Folder Structure
If you plan to push this model to a repository, structure your local folder exactly like this before saving:
* `/gis_data/` (Store your raw DEMs and LULC shapefiles here)
* `/hec_ras_model/` (Save your `.prj` file here)
* `/results_maps/` (Store exported flood inundation maps here)

---

## B. Geometry Creation

The geometry file (`.g01`) is the physical container for your flood. In a 1D model, we build this using River Centerlines and Cross-Sections.

### 1. DEM Integration in RAS Mapper
1. Open **RAS Mapper** (the globe icon).
2. Right-click `Terrains > Create a New RAS Terrain`.
3. Import the preprocessed `.tif` DEM you downloaded from [USGS Earth Explorer](https://earthexplorer.usgs.gov/) or [Bhuvan](https://bhuvan.nrsc.gov.in/). HEC-RAS will convert it into a highly compressed `.hdf` terrain file.

### 2. The River Centerline
* **How:** In RAS Mapper, right-click `Rivers > Edit Geometry`. Draw a line from upstream to downstream following the lowest point of the channel (the thalweg).
* **Why it matters:** This establishes the primary 1D routing path. HEC-RAS uses this line to calculate the longitudinal distance water travels.

### 3. Cutting Cross-Sections
* **How:** Select the `Cross Sections` layer and draw lines perpendicular to the river centerline. Ensure the line spans across the main channel and reaches high ground on *both* sides of the floodplain.
* **Spacing:** Cut a section every 50 to 100 meters. Place them closer together around sharp bends or bridges.
* **Why it matters:** 1D models do not "see" the continuous 3D world. They only calculate energy loss at the specific cross-sections you draw. If sections are 500 meters apart, the software cannot calculate the friction or volume correctly and will crash.

### 4. Defining Banks and Manning's Roughness ($n$)
1. Open the **Geometric Data Editor**. Open the `Cross Section` tool.
2. **Bank Stations:** Place red dots separating the deep "Main Channel" from the "Left Overbank" and "Right Overbank". 
   * *Why:* Water in the deep channel moves much faster than shallow water in the vegetated floodplain. HEC-RAS calculates the velocity for these three zones independently.
3. **Manning's $n$:** Enter friction values (e.g., $n=0.035$ for the channel, $n=0.060$ for the brushy overbanks).

---

## C. Flow Data Input

You have built the container; now you must add the water.

### 1. Steady Flow (Constant Peak Discharge)
Used for modelling a specific design storm (e.g., the 100-year flood).
* **Flow Input:** Open the **Steady Flow Data** editor. Enter a single peak flow rate (e.g., $1500 \text{ m}^3/\text{s}$).
* **Boundary Conditions:** Click `Reach Boundary Conditions`. Select **Normal Depth** for your downstream exit. 
   * *Why:* The model needs a starting water surface elevation to begin computing backwater calculations. Normal Depth uses Manning's equation and the average channel bed slope to estimate this starting elevation.

### 2. Unsteady Flow (Dynamic Flood Wave)
Used for routing a flood over time.
* **Flow Input:** Open the **Unsteady Flow Data** editor. Input a Flow Hydrograph (Discharge vs. Time) pulled from gauge data like [USGS Water Data](https://waterdata.usgs.gov/nwis) or hydrologic software like [HEC-HMS](https://www.hec.usace.army.mil/software/hec-hms/).
* **Initial Conditions:** ⚠️ **CRITICAL STEP.** You must enter a baseline "dummy flow" (e.g., $5 \text{ m}^3/\text{s}$) in the Initial Conditions tab. 
   * *Why:* The Saint-Venant equations will mathematically divide by zero and crash if the riverbed is completely dry when the simulation starts. The channel must be "wet" before the flood wave arrives.

---

## D. Running the Simulation

1. Open the **Steady** or **Unsteady Flow Analysis** window.
2. Go to `File > Save Plan As` (e.g., "100yr_Unsteady_Run").

### Computation Settings (Unsteady Flow)
* **Computation Interval ($\Delta t$):** The time step the math engine uses. Start with 1 Minute. 
* **Mapping Interval:** How often the software saves a visual frame for the flood animation. Set this to 10 or 15 Minutes to save hard drive space.

### Error Handling & Stability Issues
If you click "Compute" and a red error matrix appears:
1. **"Matrix will not converge":** Your Computation Interval ($\Delta t$) is too large. The software tried to push too much water too far in a single step. Reduce the time step to 30 seconds or 10 seconds.
2. **"Water surface crossed the bottom of the channel":** Your cross-sections are too far apart, causing a massive mathematical drop in energy. Go back to the Geometry Editor and use `Tools > XS Interpolation` to automatically generate sections every 25 meters.

---

## E. Results Analysis

Do not just accept a "Successful Compute" message. You must review the physics.

### 1. The Profile Plot
* Open the **Profile Plot** icon. This shows a side-view of the river from upstream to downstream.
* **Check for Spikes:** The Water Surface Elevation (WSE) should be a relatively smooth, continuous line. If the water level suddenly drops 5 meters and shoots back up at a single cross-section, you have a massive geometry error at that station.

### 2. Cross-Section Plots & "Glass-Walling"
* Open the **Cross-Section Plot** icon and cycle through your stations.
* ⚠️ **Look for the Glass Wall:** If the blue water line hits the absolute vertical edge of the box you drew, the model has failed. Because the model cannot calculate water outside the cross-section line, it assumes a vertical glass wall exists, forcing the water artificially higher. You must physically extend your cross-section wider in the Geometry editor.

### 3. Flood Mapping in RAS Mapper
* Open **RAS Mapper**.
* Check the box next to your new Results layer. Turn on **Depth** and **Velocity**.
* If you ran an Unsteady simulation, use the animation slider at the top right to watch the flood wave route through your system, pool behind bridges, and inundate the floodplain.

<br>

⬅️ **Previous:** [Chapter 5: Interface Overview](./05_interface_overview.md) | 🏠 **[Back to Master Index](./00_index.md)** | ➡️ **Next:** [Chapter 7: 2D Modeling Workflow](./07_2d_modeling.md)
