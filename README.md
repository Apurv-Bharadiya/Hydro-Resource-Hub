# 💧 Hydro-Resource-Hub

Welcome to the **Hydro-Resource-Hub**, a centralised, open-source knowledge base dedicated to Water Resources Engineering, computational hydrology, and hydraulic modelling. 

As water management becomes increasingly data-driven, bridging the gap between traditional civil engineering and modern computational tools is essential. This repository serves as a curated directory of free software, spatial analysis tools, public datasets, emerging technologies (AI/ML), and programming libraries to assist engineers, researchers, and students in analysing, modelling, and managing water systems effectively.

## 🗺️ GIS & Spatial Analysis
* [QGIS](https://qgis.org/) - A professional-grade, open-source Geographic Information System (GIS). Essential for manipulating spatial data, mapping flood zones, and preparing digital elevation models (DEMs) before importing them into hydrological models.
* [ArcGIS](https://www.esri.com/en-us/arcgis/about-arcgis/overview) - The industry-standard commercial GIS platform for advanced spatial analytics and mapping.
* [Google Earth Engine (GEE)](https://earthengine.google.com/) - A cloud-based geospatial processing platform that allows you to run algorithms on massive planetary-scale datasets (like Landsat and Sentinel) without downloading them.
* [GRASS GIS](https://grass.osgeo.org/) - A powerful GIS software suite used for geospatial data management and complex terrain analysis. It is particularly strong in raster processing.
* [WhiteboxTools](https://www.whiteboxgeo.com/manual/wbt_book/intro.html) - An advanced geospatial data analysis platform containing highly optimised tools for hydrological analysis, including watershed delineation, flow accumulation, and stream network extraction.

## 🌊 Hydrological & Hydraulic Modeling
* [EPA SWMM](https://www.epa.gov/water-research/storm-water-management-model-swmm) - The Storm Water Management Model. A dynamic rainfall-runoff simulation model used for single-event or long-term simulation of runoff quantity and quality from primarily urban areas.
* [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/) - Developed by the US Army Corps of Engineers, this River Analysis System allows you to perform one-dimensional steady flow, one and two-dimensional unsteady flow calculations, and sediment transport modelling.
* [SWAT](https://swat.tamu.edu/) - The Soil and Water Assessment Tool. A basin-scale, continuous-time model used extensively in academic research to simulate the quality and quantity of surface and groundwater and predict the environmental impact of land use and agricultural practices.
* [MODFLOW](https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model) - The USGS's modular finite-difference flow model, which is the international standard for simulating and predicting groundwater conditions and groundwater/surface-water interactions.
* [MIKE by DHI](https://www.mikepoweredbydhi.com/) - A comprehensive suite of commercial software for modelling water environments (urban, coastal, sea, and water resources).
* [HSPF](https://www.epa.gov/ceam/hydrological-simulation-program-fortran-hspf) - Hydrological Simulation Program - Fortran. Simulates the hydrologic and associated water quality processes on pervious and impervious land surfaces.
* [HydroGeoSphere](https://www.aquanty.com/hydrogeosphere) - A fully integrated 3D surface/subsurface flow and transport model.

## 🧪 Water Quality & Environmental Modeling
* [EPANET](https://www.epa.gov/water-research/epanet) - A widely used software application used to model the hydraulic and water quality behaviour of pressurised water distribution piping systems. 
* [QUAL2K](https://www.epa.gov/caddis-vol4/qual2k) - A one-dimensional river and stream water quality model supported by the EPA.
* [WASP](https://www.epa.gov/ceam/water-quality-analysis-simulation-program-wasp) - The Water Quality Analysis Simulation Program by the EPA. Helps users interpret and predict water quality responses to natural phenomena and man-made pollution in rivers, lakes, and estuaries.
* [CE-QUAL-W2](http://www.ce.pdx.edu/w2/) - A water quality and hydrodynamic model in 2D (longitudinal-vertical) for rivers, estuaries, lakes, reservoirs, and river basin systems.
* [InVEST](https://naturalcapitalproject.stanford.edu/software/invest) - A suite of free, open-source software models used to map and value the goods and services from nature, including water yield and nutrient retention.

## ⚖️ Decision Support Systems (DSS) & Water Allocation
* [WEAP](https://www.weap21.org/) - Water Evaluation And Planning system. (Note: Requires a license, but free for academic users in developing countries). A user-friendly tool that takes an integrated approach to water resources planning.
* [AQUATOOL](https://aquatool.webs.upv.es/aqt/en/home-en/) - A Decision Support System shell for the planning and management of complex water resources systems.
* [HYDRODSS](https://hydrodss.com/) - Tools and frameworks for building hydro-informatics and decision support systems.
* [Pywr](https://pywr.github.io/pywr-docs/) - A Python library for water resource system simulation and optimisation. Great for modelling how water should be distributed among agriculture, cities, and industry in a river basin.

## 🛰️ Public Datasets, Remote Sensing & Climate Data
* [NASA POWER](https://power.larc.nasa.gov/) - Prediction of Worldwide Energy Resources. Provides freely available solar and meteorological data sets from NASA research.
* [TRMM & GPM](https://gpm.nasa.gov/data/directory) - Tropical Rainfall Measuring Mission. Crucial for historical, satellite-based rainfall data.
* [MODIS](https://modis.gsfc.nasa.gov/data/) - Moderate Resolution Imaging Spectroradiometer. Excellent for tracking the water cycle, snow cover, and evapotranspiration over time.
* [Landsat & Sentinel (Copernicus)](https://scihub.copernicus.eu/) - Primary satellite constellations for medium to high-resolution optical imagery, essential for land use and water body mapping.
* [ERA5 (Copernicus)](https://cds.climate.copernicus.eu/) - The fifth generation ECMWF atmospheric reanalysis of the global climate. Essential for retrieving historical precipitation, temperature, and evaporation data.
* [CHIRPS](https://www.chc.ucsb.edu/data/chirps) - Climate Hazards Group InfraRed Precipitation with Station data. A 35+ year quasi-global rainfall dataset.
* [WorldClim](https://www.worldclim.org/) - Global climate data for ecological modelling and GIS, providing high-resolution average monthly climate data.
* [USGS Water Data for the Nation](https://waterdata.usgs.gov/nwis) - Provides access to water-resources data collected at approximately 1.9 million sites across the United States.
* [India WRIS](https://indiawris.gov.in/wris/) - The Water Resources Information System of India. A comprehensive portal providing regional data on rainfall, surface water, groundwater, and water quality.
* [EarthExplorer](https://earthexplorer.usgs.gov/) - The primary portal for downloading digital elevation models (DEMs), Landsat imagery, and other geospatial datasets necessary for watershed mapping.

## 🎯 Model Calibration & Uncertainty Analysis
* [PEST](https://pesthomepage.org/) - The industry standard for Model-Independent Parameter Estimation and Uncertainty Analysis. It automates the calibration of models like MODFLOW.
* [SWAT-CUP](https://swat.tamu.edu/software/swat-cup/) - A specialised software suite designed specifically for the calibration, validation, and uncertainty analysis of SWAT models.

## 🐍 Python Libraries for Water Engineers
* `geopandas` - Extends the datatypes used by `pandas` to allow spatial operations on geometric types. It makes working with vector data (shapefiles) in Python incredibly straightforward.
* `rasterio` - A library for reading and writing geospatial raster data (like GeoTIFFs). It allows you to analyse elevation data or satellite imagery directly within a Python script.
* `HydroStats` - A library specifically designed for computing error metrics (like Nash-Sutcliffe Efficiency or RMSE) to evaluate the accuracy of your hydrological models against observed data.
* `pyswmm` - A Python wrapper for EPA SWMM. It allows you to programmatically interact with the SWMM engine, enabling you to change parameters dynamically during a simulation.

## 📈 R Packages for Statistical Hydrology
*While Python is great for spatial analysis, R is deeply ingrained in academic hydrology for statistical analysis.*
* `HydroGOF` - An R package designed for Goodness-of-fit functions for comparison of simulated and observed hydrological time series (calculates NSE, RMSE, PBIAS, etc.).
* `dataRetrieval` - Created by the USGS, this package is designed to obtain USGS or EPA water quality and hydrology data directly into R for analysis.
* `fasstr` - Flow Analysis Summary Statistics Tool for R. Functions to tidy, summarise, analyse, trend, and visualise streamflow data.

## 🤖 Emerging Tech: AI & Machine Learning in Hydrology
*As hydrological data grows, ML is increasingly used for streamflow prediction, gap-filling data, and flood forecasting.*
* [TensorFlow](https://www.tensorflow.org/) & [PyTorch](https://pytorch.org/) - The premier deep learning frameworks. Highly useful for building Long Short-Term Memory (LSTM) networks for rainfall-runoff modelling.
* [scikit-learn](https://scikit-learn.org/) - The standard Python library for traditional machine learning algorithms (Random Forests, SVMs) used in regional hydrology studies.

## ☁️ Web Tools & Cloud Platforms
* [HydroServer](https://hydroserver.org/) - A suite of software applications for publishing and sharing hydrologic datasets on the web.
* [DHI Cloud Platforms](https://www.mikepoweredbydhi.com/products/mike-cloud) - Web-based platforms for running intensive hydraulic models and sharing results dynamically.

## 📚 Open Educational Resources
* [HydroLearn](https://www.hydrolearn.org/) - An open-source platform for active learning modules in hydrology and water resources engineering.
* [CUAHSI](https://www.cuahsi.org/) - Consortium of Universities for the Advancement of Hydrologic Science. Provides a wealth of data sets, educational materials, and cyberinfrastructure for water researchers.

---
*Maintained by Apurv Bharadiya*
