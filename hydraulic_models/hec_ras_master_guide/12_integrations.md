# 🔗 Chapter 12: Integration with QGIS, HEC-HMS & Remote Sensing

> 💡 **Pro Tip:** A rockstar hydrologist never works in a silo. HEC-RAS is a hydraulic router—it tells you where water goes *after* it hits the ground. But to answer complex engineering questions, you must integrate HEC-RAS into a broader ecosystem of hydrologic and geospatial software.

When structuring advanced research or an M.E. thesis in Water Resources Engineering, relying solely on HEC-RAS is rarely enough. A master-level workflow requires coupling models. This chapter details how to build a continuous pipeline from cloud-based satellite data to final economic damage assessments.

---

## A. Hydrologic Coupling: HEC-HMS to HEC-RAS

If you only have rainfall data (e.g., from the India Meteorological Department), you cannot input that directly into a 1D HEC-RAS river model. You must first convert the meteorological storm into a physical volume of water.

### 1. The HEC-HMS Workflow
The Hydrologic Engineering Centre's Hydrologic Modelling System ([HEC-HMS](https://www.hec.usace.army.mil/software/hec-hms/)) is the sister software to RAS. 
* **The Physics:** HEC-HMS uses methods like the SCS Curve Number or Green-Ampt to calculate how much rain infiltrates the soil versus how much becomes surface runoff. It then routes that runoff through sub-basins to generate a discharge hydrograph at the outlet.
* **The Integration:** 1. Run your storm event in HEC-HMS.
    2. Export the final Outflow Hydrograph to a Data Storage System (`.dss`) file.
    3. Open HEC-RAS, go to the Unsteady Flow Editor, and link your Upstream Boundary Condition directly to that `.dss` file.

## B. Advanced GIS Post-Processing (QGIS & ArcGIS)

RAS Mapper is excellent for visual diagnostics, but it is not built for complex spatial analytics or economic damage calculations. For that, you must export your results to dedicated GIS software.

### 1. Flood Damage Analytics
If a river overtops its banks in a dense urban environment like Ahmedabad, how do you calculate the financial cost of the disaster?
* **Step 1:** In RAS Mapper, right-click your maximum `Depth` map and select `Export to GeoTIFF`.
* **Step 2:** Open [QGIS](https://qgis.org/) or [ArcGIS Pro](https://www.esri.com/en-us/arcgis/products/arcgis-pro/overview). Import your flood depth `.tif` and overlay it onto a municipal building footprint shapefile.
* **Step 3 (Zonal Statistics):** Use the GIS `Zonal Statistics` tool to calculate the exact maximum water depth inside every single building polygon. 
* **Step 4 (Damage Curves):** Apply a Depth-Damage Curve (e.g., if water is 0.5m deep, the building loses 20% of its value; if 1.0m deep, it loses 50%). You have now translated raw hydraulic physics into an actionable economic risk report for city planners.

## C. Remote Sensing Validation (Google Earth Engine & SAR)

How do you prove your 2D HEC-RAS model is accurate if there were no physical stream gauges in the river during a past flood? You use satellites.

### 1. Synthetic Aperture Radar (SAR)
Optical satellites (like Landsat) cannot see floods because massive storms are covered in heavy clouds. SAR sensors penetrate clouds and reflect strongly off flat water surfaces.
* **The Workflow:** Use [Google Earth Engine](https://earthengine.google.com/) to write a JavaScript or Python script that pulls Sentinel-1 SAR imagery from the [Copernicus Open Access Hub](https://scihub.copernicus.eu/) for the exact date of the historical flood.
* **The Integration:** 1. Extract the observed flood inundation boundary from the SAR imagery as a shapefile.
    2. Import that shapefile into RAS Mapper.
    3. Overlay your HEC-RAS computed inundation map on top of the satellite-observed map. If they match, your model is perfectly calibrated. If your model floods areas the satellite shows as dry, you need to adjust your Manning's $n$ or terrain data.

## D. Cloud Topography and Land Cover Pipelines

Do not rely on outdated local hard drives for your base data. Connect directly to cloud repositories.
* **Topography Update:** A river's geometry changes after every monsoon. Always check [USGS EarthExplorer](https://earthexplorer.usgs.gov/) or the [Bhuvan ISRO Geo-Platform](https://bhuvan.nrsc.gov.in/) for the most recently acquired CartoDEMs or LiDAR surveys before starting a new project.
* **Dynamic Friction (LULC):** Urban sprawl drastically changes floodplain friction. Use the [ESA WorldCover](https://esa-worldcover.org/en) portal to download the latest 10m-resolution land cover data to ensure your spatial Manning's $n$ values reflect the city *today*, not ten years ago.

<br>

⬅️ **Previous:** [Chapter 11: Pro Tips & Expert Workflows](./11_pro_tips.md) | 🏠 **[Back to Master Index](./00_index.md)** | ➡️ **Next:** [Chapter 13: GitHub Best Practices for Hydraulic Models](./13_github_practices.md)
