# 💧 Hydro-Resource-Hub

Welcome to the **Hydro-Resource-Hub**, a centralized, open-source knowledge base dedicated to Water Resources Engineering, computational hydrology, and hydraulic modeling. 

As water management becomes increasingly data-driven, bridging the gap between traditional civil engineering and modern computational tools is essential. This repository serves as a curated directory of free software, spatial analysis tools, public datasets, and Python libraries designed to assist engineers, researchers, and students in analyzing, modeling, and managing water systems effectively.

## 🗺️ GIS & Spatial Analysis
* [QGIS](https://qgis.org/) - A professional-grade, open-source Geographic Information System (GIS). Essential for manipulating spatial data, mapping flood zones, and preparing digital elevation models (DEMs) before importing them into hydrological models.
* [GRASS GIS](https://grass.osgeo.org/) - A powerful GIS software suite used for geospatial data management and spatial modeling. It is particularly strong in raster processing and complex terrain analysis.
* [WhiteboxTools](https://www.whiteboxgeo.com/manual/wbt_book/intro.html) - An advanced geospatial data analysis platform. It contains highly optimized tools for hydrological analysis, such as watershed delineation, flow accumulation, and stream network extraction.

## 🌊 Hydrological & Hydraulic Modeling
* [EPA SWMM](https://www.epa.gov/water-research/storm-water-management-model-swmm) - The Storm Water Management Model. A dynamic rainfall-runoff simulation model used for single-event or long-term simulation of runoff quantity and quality from primarily urban areas.
* [EPANET](https://www.epa.gov/water-research/epanet) - A widely used software application used to model the hydraulic and water quality behavior of water distribution piping systems. 
* [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) - Developed by the US Army Corps of Engineers, this River Analysis System allows you to perform one-dimensional steady flow, one and two-dimensional unsteady flow calculations, and sediment transport modeling.
* [SWAT](https://swat.tamu.edu/) - The Soil and Water Assessment Tool. A basin-scale, continuous-time model used extensively in academic research to simulate the quality and quantity of surface and ground water and predict the environmental impact of land use and agricultural practices.
* [MODFLOW](https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model) - The USGS's modular finite-difference flow model, which is the international standard for simulating and predicting groundwater conditions and groundwater/surface-water interactions.

## 📊 Public Datasets & Satellite Imagery
* [USGS Water Data for the Nation](https://waterdata.usgs.gov/nwis) - Provides access to water-resources data collected at approximately 1.9 million sites across the United States, useful for testing models and algorithms.
* [India WRIS](https://indiawris.gov.in/wris/) - The Water Resources Information System of India. A comprehensive portal providing regional data on rainfall, surface water, groundwater, and water quality.
* [Copernicus Open Access Hub](https://scihub.copernicus.eu/) - Provides complete, free, and open access to Sentinel-1, Sentinel-2, and Sentinel-3 satellite data, which is critical for remote sensing of water bodies and soil moisture.
* [EarthExplorer](https://earthexplorer.usgs.gov/) - The primary portal for downloading digital elevation models (DEMs), Landsat imagery, and other geospatial datasets necessary for watershed mapping.

## 🐍 Python Libraries for Water Engineers
* `geopandas` - Extends the datatypes used by `pandas` to allow spatial operations on geometric types. It makes working with vector data (shapefiles) in Python incredibly straightforward.
* `rasterio` - A library for reading and writing geospatial raster data (like GeoTIFFs). It allows you to analyze elevation data or satellite imagery directly within a Python script.
* `HydroStats` - A library specifically designed for computing error metrics (like Nash-Sutcliffe Efficiency or RMSE) to evaluate the accuracy of your hydrological models against observed data.
* `pyswmm` - A Python wrapper for EPA SWMM. It allows you to programmatically interact with the SWMM engine, enabling you to change node or link parameters dynamically during a simulation—perfect for testing real-time control algorithms.

---
*Maintained by [Apurv Bharadiya]*
