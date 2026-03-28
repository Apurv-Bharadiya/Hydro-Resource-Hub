# 🗺️ Chapter 4: Data Requirements & Preprocessing (Garbage In, Garbage Out)

> 💡 **Pro Tip:** In hydraulic modelling, your simulation is only as accurate as your underlying data. Spending 80% of your time preprocessing high-quality terrain and hydrology data will save you weeks of troubleshooting unstable matrices later. HEC-RAS is incredibly strict about file formats and coordinate systems. 

To build a professional HEC-RAS model, you need a precise digital representation of the physical world (Terrain), the friction of the surface (Land Cover), and the forces acting upon it (Hydrology).

---

## 1. Topographic Terrain Data (DEM)

### What it is & Required Formats
A Digital Elevation Model (DEM) is a 3D raster grid where each pixel contains an elevation value representing the bare-earth topography.
* **Accepted HEC-RAS Format:** GeoTIFF (`.tif`) or Floating Point Raster (`.flt`). GeoTIFF is the modern industry standard.

### Why it is needed
[HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) routes water strictly based on the ground surface. It calculates volume based on the pixel size and elevation. 

⚠️ **Common Mistake:** Never use a Digital Surface Model (DSM) for hydraulic modelling unless you actively want to simulate water flowing over the tops of forest canopies and skyscraper roofs. You must use a "Bare-Earth" DEM (often derived from LiDAR).

### Where to Download
* **Global (30m Resolution):** [USGS Earth Explorer](https://earthexplorer.usgs.gov/) (Use the SRTM 1-Arc Second dataset).
* **Global (10m-30m Resolution):** [Copernicus Open Access Hub](https://scihub.copernicus.eu/) (Excellent for European and global Copernicus DEMs).
* **India (High-Resolution):** [Bhuvan ISRO](https://bhuvan.nrsc.gov.in/) (CartoDEM is highly recommended for Indian catchments).

### 🛠️ How to Preprocess for HEC-RAS (Step-by-Step)
Raw downloaded DEMs will instantly crash HEC-RAS if imported directly. You must preprocess them in a GIS software like [QGIS](https://qgis.org/) or [ArcGIS](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview).

1. **Mosaic the Tiles:** If your study area covers multiple downloaded DEM tiles, use the `Merge` tool in QGIS to stitch them into a single seamless raster.
2. **The Coordinate System Translation (CRITICAL STEP):** Satellite data is downloaded in a Geographic Coordinate System (GCS), measuring in Decimal Degrees (e.g., WGS 84). **HEC-RAS cannot calculate hydraulic volume in degrees.**
   * In QGIS, use the `Warp (Reproject)` tool.
   * Translate the DEM into a **Projected Coordinate System (PCS)** using a UTM Zone (e.g., UTM Zone 42N for Gujarat). This converts the X and Y cell dimensions into linear **Meters** or **Feet**.
3. **Clip to Watershed:** Use the `Clip Raster by Mask Layer` tool to cut the DEM down to your exact watershed boundary. This drastically reduces file size and saves RAM during HEC-RAS computations.
4. **Export:** Export the final preprocessed layer as a `GeoTIFF (.tif)`.

---

## 2. Land Use & Land Cover Data (LULC)

### What it is & Required Formats
Spatial data categorising ground cover (e.g., dense forest, paved concrete, agricultural fields). 
* **Accepted HEC-RAS Format:** Shapefile (`.shp`). While rasters can be used, vector shapefiles are cleaner for assigning attribute data in RAS Mapper.

### Why it is needed
In 2D modelling, we use LULC data to automatically generate spatially varying Manning's roughness coefficients ($n$). Water flows significantly faster over a paved highway ($n = 0.015$) than through dense brush ($n = 0.100$). HEC-RAS uses this layer to apply friction to specific grid cells.

### Where to Download
* **Global (10m Resolution):** [ESA WorldCover](https://esa-worldcover.org/en) (Industry standard for modern land cover).
* **India (Regional):** [Bhuvan ISRO](https://bhuvan.nrsc.gov.in/) (Look for LULC 1:50k datasets).

### 🛠️ How to Preprocess for HEC-RAS
1. **Reproject:** Open the LULC data in [QGIS](https://qgis.org/) and reproject it to the **exact same UTM coordinate system** as your DEM. If the projections do not match, HEC-RAS will drop the layer in the wrong location.
2. **Vectorise:** If your downloaded LULC is a raster, use the `Polygonise (Raster to Vector)` tool to convert it into a Shapefile (`.shp`).
3. **Attribute Mapping:** Open the shapefile's attribute table. Add a new decimal column named `Mannings_N`. Assign standard engineering friction values to each land cover class based on Chow's Open Channel Hydraulics tables.

---

## 3. Hydrological Data (Boundary Conditions)

### What it is & Required Formats
Time-series data representing the volume of water entering or leaving your system. 
* **Discharge Data:** Streamflow in cubic meters per second (m³/s) over time (a Hydrograph).
* **Rainfall Data:** Precipitation depth in millimetres (mm) over time (a Hyetograph).
* **Accepted HEC-RAS Formats:** Comma Separated Values (`.csv`), Excel (`.xlsx`), or the highly preferred USACE Data Storage System format (`.dss`).

### Why it is needed
The Saint-Venant momentum and continuity equations require Boundary Conditions to solve the mathematical matrix. You must tell the model exactly how much water is being pushed into the 2D mesh (upstream boundary) and at what elevation it leaves (downstream boundary).

### Where to Download
* **Stream Gauge Data (USA):** [USGS Water Data](https://waterdata.usgs.gov/nwis).
* **Stream Gauge Data (India):** [Central Water Commission (CWC)](https://cwc.gov.in/) or the [India WRIS Portal](https://indiawris.gov.in/wris/#/).
* **Rainfall Data (Global):** [CHIRPS Precipitation Data](https://data.chc.ucsb.edu/products/CHIRPS-2.0/) or [NASA GPM (IMERG)](https://gpm.nasa.gov/data/directory).

### 🛠️ How to Preprocess for HEC-RAS
Time-series data is notoriously messy. A single missing data point (`NaN`) will instantly crash an unsteady HEC-RAS run.

1. **Clean the Data (Python/Excel):** Remove all null values. Interpolate missing hours if necessary. Ensure there are no negative discharge values.
2. **Formatting Time:** Ensure your timestamps are evenly spaced (e.g., exactly 1-hour intervals). HEC-RAS prefers the strict date format: `DDMMMYYYY HH:mm` (e.g., `01Jan2020 14:00`).
3. **Hydrologic Routing (If applicable):** HEC-RAS routes water, it does *not* convert rain into runoff (except in specific Rain-on-Grid setups). If you only have raw rainfall data, you must first build a model in [HEC-HMS](https://www.hec.usace.army.mil/software/hec-hms/) to calculate infiltration and generate a discharge hydrograph.
4. **Convert to DSS:** For massive datasets (e.g., 10 years of hourly flow), use the [HEC-DSSVue Utility](https://www.hec.usace.army.mil/software/hec-dssvue/) to convert your Excel/CSV data into a `.dss` database file. HEC-RAS reads `.dss` files thousands of times faster than manual text inputs.

<br>

---
**[⬅️ Chapter 03: Fundamental Concepts](./03_fundamental_concepts.md)** | **[🏠 Main Index](./00_index.md)** | **[Chapter 05: Interface Overview ➡️](./05_interface_overview.md)**
