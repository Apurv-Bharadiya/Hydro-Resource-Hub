<div align="center">
  <h1>🌊 Hydro-Resource-Hub</h1>

  <img src="https://img.shields.io/badge/Domain-Water%20Resources%20Engineering-00C9FF?style=flat-square&logo=qgis&logoColor=white&labelColor=0055ff" alt="Domain">
  <img src="https://img.shields.io/badge/Ecosystem-Open%20Source-10B981?style=flat-square&logo=github&logoColor=white&labelColor=047857" alt="Ecosystem">
  <img src="https://img.shields.io/badge/Scale-Planetary%20Data-8B5CF6?style=flat-square&logo=googleearth&logoColor=white&labelColor=5B21B6" alt="Scale">
</div>

<div align="center">
<br>

  <i> "A comprehensive compilation of open-source software, public datasets, and computational tools for Water Resources Engineering and hydrological modelling." </i>
</div>

> 🌍 **Welcome to the Hub.** Engineered for graduate researchers, data scientists, and civil engineers, this repository serves as a centralised command centre for modern water management. Explore industry-standard software, harness planetary-scale satellite datasets, and deploy machine learning models to solve complex hydrological challenges.

---

## 🚀 Featured: The Ultimate HEC-RAS Master Guide

<div>
  <img src="https://img.shields.io/badge/Level-Beginner%20to%20Advanced-2EA043?style=flat-square&logo=gitbook&logoColor=white&labelColor=238636" alt="Level">
  <img src="https://img.shields.io/badge/Estimated%20Time-45%20Minutes-007EC6?style=flat-square&logo=clockify&logoColor=white&labelColor=005A9E" alt="Estimated Time">
  <img src="https://img.shields.io/badge/Domain-Hydraulic%20Engineering-F59E0B?style=flat-square&logo=digitalocean&logoColor=white&labelColor=B45309" alt="Domain">
</div>

<br>

This repository hosts a world-class, 14-chapter modular training manual for [HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/). It transitions from basic 1D steady-flow physics to advanced 2D "Rain-on-Grid" urban hydrodynamic simulations.

### 📑 Guide Roadmap

| **Section** | **Chapters** | **Highlights** |
| :--- | :--- | :--- |
| **🟢 Foundations** | [01](./hydraulic_models/hec_ras_master_guide/01_introduction.md) - [04](./hydraulic_models/hec_ras_master_guide/04_data_requirements.md) | Theory, Installation, and USGS / Bhuvan Data Sourcing. |
| **🟡 Core Workflows** | [05](./hydraulic_models/hec_ras_master_guide/05_interface_overview.md) - [08](./hydraulic_models/hec_ras_master_guide/08_ras_mapper.md) | 1D/2D Mesh Generation, Breaklines, and RAS Mapper Visualisation. |
| **🔴 Advanced Apps** | [09](./hydraulic_models/hec_ras_master_guide/09_case_study_rajkot.md) - [12](./hydraulic_models/hec_ras_master_guide/12_integrations.md) | Rajkot Urban Case Study, Troubleshooting, and HEC-HMS Integration. |
| **🐙 Management** | [13](./hydraulic_models/hec_ras_master_guide/13_github_practices.md) - [14](./hydraulic_models/hec_ras_master_guide/14_conclusion.md) | GitHub Best Practices for heavy models and Career Next Steps. |

👉 **[Start the Master Guide here: Chapter 0 - Main Index](./hydraulic_models/hec_ras_master_guide/00_index.md)**

---

## 📑 Table of Contents

- [📂 Interactive Templates & Cheat Sheets](#-interactive-templates--cheat-sheets)

1. [🗺️ GIS & Spatial Analysis](#️-gis--spatial-analysis)
2. [🌊 Hydrological & Hydraulic Modelling](#-hydrological--hydraulic-modelling)
3. [🧪 Water Quality & Environmental Modelling](#-water-quality--environmental-modelling)
4. [⚖️ Decision Support Systems (DSS) & Water Allocation](#️-decision-support-systems-dss--water-allocation)
5. [🛰️ Public Datasets, Remote Sensing & Climate Data](#️-public-datasets-remote-sensing--climate-data)
6. [🎯 Model Calibration & Uncertainty Analysis](#-model-calibration--uncertainty-analysis)
7. [🐍 Python Libraries for Water Engineers](#-python-libraries-for-water-engineers)
8. [📈 R Packages for Statistical Hydrology](#-r-packages-for-statistical-hydrology)
9. [🤖 Emerging Tech: AI & Machine Learning in Hydrology](#-emerging-tech-ai--machine-learning-in-hydrology)
10. [☁️ Web Tools & Cloud Platforms](#️-web-tools--cloud-platforms)
11. [📚 Open Educational Resources](#-open-educational-resources)
12. [📋 Master Reference Table](#-master-reference-table)

---

## 📂 Interactive Templates & Cheat Sheets

We have built actual starter code and reference guides directly into this repository. Click below to view or download them:
* 📝 **[Hydrology & Fluid Mechanics Master Cheat Sheet](./cheat_sheets/01_hydrology_formulas.md)** - A complete mathematical reference guide for 16 core engineering equations, including their historical context and key limitations.
* 🐍 **[Simple Hydrograph Plotter](https://github.com/Apurv-Bharadiya/Hydro-Resource-Hub/blob/main/python_templates/01_simple_hydrograph.py)** - A beginner-friendly Python script using pandas and matplotlib to visualise synthetic streamflow data.
* 📡 **[GloFAS River Data Fetcher](https://github.com/Apurv-Bharadiya/Hydro-Resource-Hub/blob/main/python_templates/02_river_data_fetcher.py)** - An advanced Python script that connects to the Open-Meteo API to download and plot live, simulated discharge data for international rivers.

---

## 🗺️ GIS & Spatial Analysis

Every hydrological model begins with a spatial understanding of the terrain. Geographic Information Systems (GIS) are the bedrock of modern Water Resources Engineering, allowing researchers to delineate watersheds, process Digital Elevation Models (DEMs), and map flood inundation zones before any fluid mechanics equations are even applied.

| **Resource** | **Description** |
| :--- | :--- |
| **[QGIS](https://qgis.org/)** | A professional-grade, open-source Geographic Information System (GIS). Essential for manipulating spatial data, mapping flood zones, and preparing digital elevation models (DEMs) before importing them into hydrological models. |
| **[ArcGIS](https://www.esri.com/en-us/arcgis/pro)** | The industry-standard commercial GIS platform for advanced spatial analytics and mapping. |
| **[Google Earth Engine (GEE)](https://earthengine.google.com/)** | A cloud-based geospatial processing platform that allows you to run algorithms on massive planetary-scale datasets (like Landsat and Sentinel) without downloading them. |
| **[GRASS GIS](https://grass.osgeo.org/)** | A powerful GIS software suite used for geospatial data management and complex terrain analysis. It is particularly strong in raster processing. |
| **[WhiteboxTools](https://www.whiteboxgeo.com/)** | An advanced geospatial data analysis platform containing highly optimised tools for hydrological analysis, including watershed delineation, flow accumulation, and stream network extraction. |

---

## 🌊 Hydrological & Hydraulic Modelling

This is the computational core of water engineering. Hydrological models simulate the rainfall-runoff process across a catchment, while hydraulic models route that water through rivers, pipes, and channels. Together, they allow us to design resilient infrastructure and forecast flood events under changing climate scenarios.

| **Resource** | **Description** |
| :--- | :--- |
| **[EPA SWMM](https://www.epa.gov/water-research/storm-water-management-model-swmm)** | The Storm Water Management Model. A dynamic rainfall-runoff simulation model used for single-event or long-term simulation of runoff quantity and quality from primarily urban areas. |
| **[HEC-RAS](https://www.hec.usace.army.mil/software/hec-ras/)** | Developed by the US Army Corps of Engineers, this River Analysis System allows you to perform one-dimensional steady flow, one and two-dimensional unsteady flow calculations, and sediment transport modelling. |
| **[SWAT](https://swat.tamu.edu/)** | The Soil and Water Assessment Tool. A basin-scale, continuous-time model used extensively in academic research to simulate the quality and quantity of surface and groundwater and predict the environmental impact of land use and agricultural practices. |
| **[MODFLOW](https://www.usgs.gov/software/modflow-6-usgs-modular-hydrologic-model)** | The USGS's modular finite-difference flow model, which is the international standard for simulating and predicting groundwater conditions and groundwater/surface-water interactions. |
| **[MIKE by DHI](https://www.mikepoweredbydhi.com/)** | A comprehensive suite of commercial software for modelling water environments (urban, coastal, sea, and water resources). |
| **[HSPF](https://www.epa.gov/ceam/hydrological-simulation-program-fortran-hspf)** | Hydrological Simulation Program - Fortran. Simulates the hydrologic and associated water quality processes on pervious and impervious land surfaces. |
| **[HydroGeoSphere](https://www.aquanty.com/hydrogeosphere)** | A fully integrated 3D surface/subsurface flow and transport model. |

---

## 🧪 Water Quality & Environmental Modelling

Modern water management must address quality, not just quantity. These modelling tools simulate the transport and fate of pollutants, nutrients, and thermal changes in water bodies. They are critical for environmental impact assessments, protecting aquatic ecosystems, and ensuring safe municipal water supplies.

| **Resource** | **Description** |
| :--- | :--- |
| **[EPANET](https://www.epa.gov/water-research/epanet)** | A widely used software application used to model the hydraulic and water quality behaviour of pressurised water distribution piping systems. |
| **[QUAL2K](https://www.epa.gov/caddis-vol4/qual2k)** | A one-dimensional river and stream water quality model supported by the EPA. |
| **[WASP](https://www.epa.gov/ceam/water-quality-analysis-simulation-program-wasp)** | The Water Quality Analysis Simulation Program by the EPA. Helps users interpret and predict water quality responses to natural phenomena and man-made pollution in rivers, lakes, and estuaries. |
| **[CE-QUAL-W2](https://www.cee.pdx.edu/w2/)** | A water quality and hydrodynamic model in 2D (longitudinal-vertical) for rivers, estuaries, lakes, reservoirs, and river basin systems. |
| **[InVEST](https://naturalcapitalproject.stanford.edu/software/invest)** | A suite of free, open-source software models used to map and value the goods and services from nature, including water yield and nutrient retention. |

---

## ⚖️ Decision Support Systems (DSS) & Water Allocation

Engineering meets policy. When water becomes scarce, balancing the competing demands of agriculture, urban centres, and industry requires rigorous optimisation. Decision Support Systems provide a framework for scenario testing, helping stakeholders make data-driven allocation policies and manage reservoir operations.

| **Resource** | **Description** |
| :--- | :--- |
| **[WEAP](https://www.weap21.org/)** | Water Evaluation And Planning system. A user-friendly tool that takes an integrated approach to water resources planning. |
| **[AQUATOOL](https://aquatool.webs.upv.es/)** | A Decision Support System shell for the planning and management of complex water resources systems. |
| **[HYDRODSS](https://hydrodss.org/)** | Tools and frameworks for building hydro-informatics and decision support systems. |
| **[Pywr](https://pywr.github.io/pywr-docs/)** | A Python library for water resource system simulation and optimisation. Great for modelling how water should be distributed among agriculture, cities, and industry in a river basin. |

---

## 🛰️ Public Datasets, Remote Sensing & Climate Data

A model is only as good as its input data. With physical stream gauges becoming sparse or unreliable in many regions, remote sensing and planetary-scale satellite data have become the lifeblood of hydrological research. These public datasets provide critical historical and real-time inputs for precipitation, evapotranspiration, and land-cover.

| **Resource** | **Description** |
| :--- | :--- |
| **[NASA POWER](https://power.larc.nasa.gov/)** | Prediction of Worldwide Energy Resources. Provides freely available solar and meteorological data sets from NASA research. |
| **[TRMM & GPM](https://gpm.nasa.gov/)** | Tropical Rainfall Measuring Mission. Crucial for historical, satellite-based rainfall data. |
| **[MODIS](https://modis.gsfc.nasa.gov/)** | Moderate Resolution Imaging Spectroradiometer. Excellent for tracking the water cycle, snow cover, and evapotranspiration over time. |
| **[Landsat & Sentinel (Copernicus)](https://scihub.copernicus.eu/)** | Primary satellite constellations for medium to high-resolution optical imagery, essential for land use and water body mapping. |
| **[ERA5 (Copernicus)](https://climate.copernicus.eu/climate-reanalysis)** | The fifth generation ECMWF atmospheric reanalysis of the global climate. Essential for retrieving historical precipitation, temperature, and evaporation data. |
| **[CHIRPS](https://www.chc.ucsb.edu/data/chirps)** | Climate Hazards Group InfraRed Precipitation with Station data. A 35+ year quasi-global rainfall dataset. |
| **[WorldClim](https://www.worldclim.org/)** | Global climate data for ecological modelling and GIS, providing high-resolution average monthly climate data. |
| **[USGS Water Data for the Nation](https://waterdata.usgs.gov/nwis)** | Provides access to water-resources data collected at approximately 1.9 million sites across the United States. |
| **[India WRIS](https://indiawris.gov.in/wris/#/)** | The Water Resources Information System of India. A comprehensive portal providing regional data on rainfall, surface water, groundwater, and water quality. |
| **[EarthExplorer](https://earthexplorer.usgs.gov/)** | The primary portal for downloading digital elevation models (DEMs), Landsat imagery, and other geospatial datasets necessary for watershed mapping. |

---

## 🎯 Model Calibration & Uncertainty Analysis

Uncalibrated models are merely hypotheses. To transition a model from a theoretical exercise to a reliable predictive tool, it must be rigorously calibrated against observed historical data. These tools automate complex parameter estimation and quantify the inherent uncertainty in our hydrological predictions.

| **Resource** | **Description** |
| :--- | :--- |
| **[PEST](https://pesthomepage.org/)** | The industry standard for Model-Independent Parameter Estimation and Uncertainty Analysis. It automates the calibration of models like MODFLOW. |
| **[SWAT-CUP](https://swat.tamu.edu/software/swat-cup/)** | A specialised software suite designed specifically for the calibration, validation, and uncertainty analysis of SWAT models. |

---

## 🐍 Python Libraries for Water Engineers

Python has radically transformed hydro-informatics. By shifting away from tedious point-and-click GUI workflows, engineers can use Python to automate spatial geoprocessing, rapidly clean massive climate datasets, and build reproducible, open-source modelling pipelines.

| **Resource** | **Description** |
| :--- | :--- |
| **`geopandas`** | Extends the datatypes used by pandas to allow spatial operations on geometric types. It makes working with vector data (shapefiles) in Python incredibly straightforward. |
| **`rasterio`** | A library for reading and writing geospatial raster data (like GeoTIFFs). It allows you to analyse elevation data or satellite imagery directly within a Python script. |
| **`HydroStats`** | A library specifically designed for computing error metrics (like Nash-Sutcliffe Efficiency or RMSE) to evaluate the accuracy of your hydrological models against observed data. |
| **`pyswmm`** | A Python wrapper for EPA SWMM. It allows you to programmatically interact with the SWMM engine, enabling you to change parameters dynamically during a simulation. |

---

## 📈 R Packages for Statistical Hydrology

While Python dominates spatial automation, R remains deeply entrenched in academic hydrology for its unparalleled statistical capabilities. These packages are essential for rigorous frequency analysis, flow duration curves, and calculating goodness-of-fit metrics for model validation.

| **Resource** | **Description** |
| :--- | :--- |
| **`HydroGOF`** | An R package designed for Goodness-of-fit functions for comparison of simulated and observed hydrological time series (calculates NSE, RMSE, PBIAS, etc.). |
| **`dataRetrieval`** | Created by the USGS, this package is designed to obtain USGS or EPA water quality and hydrology data directly into R for analysis. |
| **`fasstr`** | Flow Analysis Summary Statistics Tool for R. Functions to tidy, summarise, analyse, trend, and visualise streamflow data. |

---

## 🤖 Emerging Tech: AI & Machine Learning in Hydrology

The frontier of water resources engineering is increasingly data-driven. Machine Learning algorithms are beginning to augment, and in some cases outperform, traditional physics-based models—especially in rapid streamflow forecasting and gap-filling incomplete historical datasets.

| **Resource** | **Description** |
| :--- | :--- |
| **[TensorFlow](https://www.tensorflow.org/) & [PyTorch](https://pytorch.org/)** | The premier deep learning frameworks. Highly useful for building Long Short-Term Memory (LSTM) networks for rainfall-runoff modelling. |
| **[scikit-learn](https://scikit-learn.org/)** | The standard Python library for traditional machine learning algorithms (Random Forests, SVMs) used in regional hydrology studies. |

---

## ☁️ Web Tools & Cloud Platforms

The era of desktop-bound modelling is ending. Cloud platforms allow engineers to bypass local hardware limitations, running massive parallel simulations and sharing dynamic, interactive dashboards directly with stakeholders and policymakers.

| **Resource** | **Description** |
| :--- | :--- |
| **[HydroServer](https://hydroserver.org/)** | A suite of software applications for publishing and sharing hydrologic datasets on the web. |
| **[DHI Cloud Platforms](https://www.mikepoweredbydhi.com/products/mike-cloud)** | Web-based platforms for running intensive hydraulic models and sharing results dynamically. |

---

## 📚 Open Educational Resources

Continuous learning is vital in an industry transformed by digital tech. These open-source platforms and consortiums democratize access to advanced hydrological science, ensuring that graduate researchers and practitioners have the training needed to tackle complex water challenges.

| **Resource** | **Description** |
| :--- | :--- |
| **[HydroLearn](https://www.hydrolearn.org/)** | An open-source platform for active learning modules in hydrology and water resources engineering. |
| **[CUAHSI](https://www.cuahsi.org/)** | Consortium of Universities for the Advancement of Hydrologic Science. Provides a wealth of data sets, educational materials, and cyberinfrastructure for water researchers. |

---

## 📋 Master Reference Table

*A quick-reference matrix of the critical tools, models, and datasets used in modern Water Resources Engineering.*

| *Name* | *Type* | *Publisher / Agency* | *Mission / Data Coverage* | *Primary Use (Why use it?)* |
| :--- | :--- | :--- | :--- | :--- |
| **QGIS** | GIS Software | Open Source | N/A | Free, professional-grade mapping, DEM processing, and spatial data manipulation. |
| **Google Earth Engine** | Cloud GIS | Google | Global | Running geospatial algorithms on planetary-scale datasets without downloading them. |
| **EPA SWMM** | Hydrologic Model | US EPA | N/A | Industry standard for urban stormwater, rainfall-runoff, and sewer simulation. |
| **HEC-RAS** | Hydraulic Model | US Army Corps | N/A | 1D/2D river flow routing, flood inundation mapping, and sediment transport. |
| **SWAT** | Basin Model | USDA / Texas A&M | N/A | Long-term basin-scale agricultural, land-use, and environmental impact modelling. |
| **MODFLOW** | Groundwater Model | USGS | N/A | The definitive global standard for 3D groundwater flow and surface-water interaction. |
| **EPANET** | Pipe Network Model | US EPA | N/A | Simulating hydraulic and water quality behaviour in pressurised distribution pipes. |
| **WEAP** | DSS / Allocation | Stockholm Env. Inst. | N/A | Integrated water resources planning, scenario testing, and basin allocation. |
| **NASA POWER** | Climate Dataset | NASA | Global | Reliable solar and meteorological datasets for hydrology and agricultural modelling. |
| **TRMM & GPM** | Satellite Dataset | NASA / JAXA | Global (Tropical/Broad) | Crucial for historical and real-time precipitation mapping from space. |
| **Landsat & Sentinel** | Satellite Imagery | USGS / Copernicus | Global | High-resolution optical imagery for land-use classification and surface water tracking. |
| **ERA5** | Climate Reanalysis | ECMWF / Copernicus | Global (1940-Present) | Best-in-class historical climate data (precipitation, temperature, evaporation). |
| **India WRIS** | Public Dataset | Gov. of India | India (Regional) | Centralised portal for Indian river basin data, groundwater levels, and rainfall. |
| **PEST** | Calibration Tool | Watermark Numerical | N/A | Automates complex model calibration (like MODFLOW) and uncertainty analysis. |
| **TensorFlow / PyTorch** | AI/ML Frameworks | Google / Meta | N/A | Building advanced deep learning models (like LSTMs) for streamflow/flood forecasting. |
| **geopandas** | Python Library | Open Source | N/A | Brings spatial data manipulation (shapefiles) directly into Python workflows. |

---
**<i> Maintained by Apurv Bharadiya </i>**
