# 🏙️ Chapter 9: Real-World Case Study (Urban Flood Modelling in Rajkot)

> 💡 **Pro Tip:** Theory and pristine tutorial datasets only take you so far. The true test of a Water Resources Engineer is taking messy, imperfect, real-world data and forcing it to obey the laws of physics inside a computational matrix. This chapter bridges the gap between the classroom and the consulting firm.

This chapter outlines a master-level practical application: Simulating a 100-year flood event on the Aji River as it passes through the densely populated urban centre of Rajkot, Gujarat. We will build a **Coupled 1D/2D Unsteady Flow Model**.

---

## A. The Objective & Engineering Scope

**The Problem:** Rajkot experiences intense, concentrated monsoon cloudbursts. The Aji River bisects the city, and the Aji Dam sits immediately upstream of the municipal limits. We need to map the maximum inundation zone if a massive spillway release (unsteady hydrograph) coincides with heavy urban stormwater runoff (rain-on-grid).

**The Solution Architecture (1D/2D Coupling):** * **Why not pure 1D?** The urban floodplain is entirely paved and flat; water will flow down city streets in multiple directions. 1D cannot map this.
* **Why not pure 2D?** The main Aji River channel is deeply incised. Modelling a deep, fast-moving river purely in 2D requires a microscopic cell size, which would cause the simulation to take weeks to compute.
* **The Master Workflow:** We will model the main river channel in 1D for computational speed, model the city grid in 2D for spatial accuracy, and connect them with a "Lateral Structure" (a mathematical retaining wall). When the 1D river overflows the wall, water spills into the 2D city.

---

## B. Data Procurement (Building the Digital Twin)

We cannot model Rajkot without first building its digital twin. Real-world data is messy, so we rely on authoritative government portals.

1.  **Topography (DEM):** * We require a high-resolution "bare-earth" DEM to capture both the deep river thalweg and the subtle crowns of the city roads. 
    * *Action:* Download the CartoDEM (10m or better resolution) covering the Rajkot catchment from the [Bhuvan ISRO Geo-Platform](https://bhuvan.nrsc.gov.in/).
2.  **Land Use / Land Cover (LULC):** * We must differentiate the friction of the dense concrete urban core ($n=0.015$) from the natural scrubland outside the city limits ($n=0.060$). 
    * *Action:* Download regional LULC shapefiles from [Bhuvan ISRO](https://bhuvan.nrsc.gov.in/) or the global [ESA WorldCover](https://esa-worldcover.org/en) database.
3.  **Hydrology (The Storm Forces):** * *Action:* Access historical monsoon daily rainfall grid data from the [India Meteorological Department (IMD)](https://mausam.imd.gov.in/) and gauge discharge data from the [Central Water Commission (CWC)](https://cwc.gov.in/) or [India WRIS](https://indiawris.gov.in/wris/#/).

---

## C. Hydrologic Pre-Processing (Outside HEC-RAS)

[HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) is a *hydraulic* routing tool; it needs a flow hydrograph. We cannot just input raw rainfall depth for the upstream boundary.

1.  **The Transformation:** We build a hydrologic model in [HEC-HMS](https://www.hec.usace.army.mil/software/hec-hms/).
2.  **The Physics:** We use the SCS Curve Number (CN) method. Because Rajkot is highly urbanised (high impervious area), the CN will be very high (e.g., 85-90). This tells HEC-HMS that very little rain infiltrates the soil; almost all of it becomes violent surface runoff.
3.  **The Output:** HEC-HMS calculates the lag time and outputs a final Discharge Hydrograph (Flow vs. Time) representing the 100-year flood wave entering the Aji River from the dam. Export this to a `.dss` file.

---

## D. HEC-RAS Geometry Setup (The Coupled Model)

1.  **The 1D River Skeleton:** * In RAS Mapper, trace the Aji River centerline. 
    * Cut cross-sections every 100 meters. 
    * *Crucial Step:* Use the Geometric Data Editor to physically input the exact deck elevations and pier widths of the major bridge crossings (like the Ring Road bridge). Bridges are the primary cause of urban backwater flooding.
2.  **The 2D Urban Grid:** * Draw a 2D Flow Area polygon covering the low-lying neighbourhoods adjacent to the river. 
    * Generate a $15\text{m} \times 15\text{m}$ computational mesh.
    * Draw Breaklines along all major elevated highways and railway embankments to prevent water from "leaking" through them.
3.  **The 1D/2D Connection (Lateral Structure):** * In the Geometric Data Editor, draw a `Lateral Structure` along the exact left and right bank stations of your 1D river. 
    * Set the "Tailwater Connection" to your new 2D Flow Area. 
    * *The Physics:* The software now constantly monitors the 1D Water Surface Elevation. The second it rises higher than the crest of your Lateral Structure, the equations shift the volume out of the 1D matrix and dump it into the 2D grid.

---

## E. Execution & Advanced Troubleshooting

We run the Unsteady Flow simulation. 

⚠️ **The 1D/2D Interface Crash:**
The most common point of failure in a coupled model is the exact moment water spills over the Lateral Structure. If $500\text{ m}^3/\text{s}$ of water violently hits a dry 2D cell in a single 1-minute time step, the Courant condition is shattered, and the model crashes.
* **The Fix:** Go to the Unsteady Flow Analysis window $\rightarrow$ `Options` $\rightarrow$ `Calculation Options and Tolerances`. 
* Turn on **1D/2D Flow Iterations**. Set the maximum iterations to 20. This forces the software to double-check the math between the 1D river and the 2D floodplain multiple times per time step before moving forward.

---

## F. Results Interpretation & Engineering Action

Once the matrix successfully converges, we open RAS Mapper to analyse the disaster.

1.  **Identifying Velocity Chokepoints:** * Turn on the `Velocity` map. If you see extreme red zones ($> 3\text{m/s}$) directly beneath the Ring Road bridge, the bridge opening is too small. It is acting like a choked nozzle, creating a pressurised backwater effect that floods the neighbourhoods *upstream* of the bridge.
2.  **Urban Inundation Mapping:** * The `Depth` map reveals that water overtopping the left bank flows downhill into a heavily populated residential zone, pooling to depths of 1.2 meters. 
3.  **Export and Decision Making:** * Export the Maximum Depth raster to a GeoTIFF. 
    * Load it into [QGIS](https://qgis.org/) and overlay it onto building footprints. 
    * *Engineering Action:* As the Lead Water Resources Engineer, you use this map to justify the municipal budget to either (A) widen the Ring Road bridge span, or (B) construct a 2-meter continuous concrete floodwall along the vulnerable left bank.

<br>

---
<div align="center">
  <a href="./08_ras_mapper.md"><b>⬅️ Chapter 08: RAS Mapper & Visualisation</b></a> | 
  🏠 <a href="./00_index.md"><b>Main Index</b></a> | 
  <a href="./10_troubleshooting.md"><b>Chapter 10: Troubleshooting Guide ➡️</b></a>
</div>
