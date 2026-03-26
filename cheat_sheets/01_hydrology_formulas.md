# 📐 Hydrology & Fluid Mechanics Master Cheat Sheet

A comprehensive, deep-dive reference guide to the fundamental and advanced equations used in Water Resources Engineering, fluid dynamics, and computational modelling.

---

## 📑 Table of Contents
- [🌊 Fluid Mechanics & Pipe Flow](#-fluid-mechanics--pipe-flow)
  - [1. Bernoulli's Equation](#1-bernoullis-equation-conservation-of-energy)
  - [2. Darcy-Weisbach Equation](#2-darcy-weisbach-equation)
  - [3. Hazen-Williams Equation](#3-hazen-williams-equation)
- [🏞️ Open Channel Hydraulics](#️-open-channel-hydraulics)
  - [4. Manning's Equation](#4-mannings-equation)
  - [5. Froude Number](#5-froude-number)
  - [6. Chézy Equation](#6-chézy-equation)
- [🌧️ Surface Water Hydrology](#️-surface-water-hydrology)
  - [7. SCS Curve Number (CN) Method](#7-scs-curve-number-cn-method)
  - [8. Green-Ampt Infiltration Model](#8-green-ampt-infiltration-model)
  - [9. Muskingum Routing Method](#9-muskingum-routing-method)
  - [10. Penman-Monteith Equation](#10-penman-monteith-equation)
  - [11. Rational Method](#11-rational-method)
  - [12. Horton's Infiltration Equation](#12-hortons-infiltration-equation)
- [🪨 Groundwater Hydrology](#-groundwater-hydrology)
  - [13. Darcy's Law](#13-darcys-law)
  - [14. Dupuit Equation](#14-dupuit-equation-unconfined-aquifer-flow)
  - [15. Theis Equation](#15-theis-equation)
  - [16. Thiem Equation](#16-thiem-equation-steady-state-confined-flow)

---

## 🌊 Fluid Mechanics & Pipe Flow

### 1. Bernoulli's Equation (Conservation of Energy)
Describes the behaviour of a fluid under varying conditions of pressure and height, stating that the total mechanical energy of a flowing fluid remains constant.

$$\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_f$$

* $P$ = Pressure ($N/m^2$)
* $\gamma$ = Specific weight of the fluid ($N/m^3$)
* $V$ = Fluid velocity ($m/s$)
* $z$ = Elevation head ($m$)
* $g$ = Acceleration due to gravity ($9.81m/s^2$)
* $h_f$ = Head loss due to friction ($m$)

> - **📜 Historical Context:** Published by Swiss mathematician **Daniel Bernoulli** in 1738 in his book *Hydrodynamica*.
> - **✅ Primary Applications:** Designing pipe networks, calculating pump head requirements, and understanding pitot tubes.
> - **⚠️ Key Limitations:** Cannot be used (in its strict theoretical form) for highly compressible fluids (gases at high speeds), highly viscous fluids, or flows where massive temperature changes occur.

### 2. Darcy-Weisbach Equation
The most theoretically robust equation for calculating the friction head loss in a pipe.

$$h_f = f \frac{L}{D} \frac{V^2}{2g}$$

* $h_f$ = Head loss due to friction ($m$)
* $f$ = Darcy friction factor (dimensionless, found via Moody chart)
* $L$ = Length of the pipe ($m$)
* $D$ = Diameter of the pipe ($m$)
* $V$ = Average flow velocity ($m/s$)

> - **📜 Historical Context:** Developed by **Henry Darcy** (1857) and modified by **Julius Weisbach** (1845).
> - **✅ Primary Applications:** Standard for modeling pressurized pipe systems.
> - **⚠️ Key Limitations:** Requires iterative calculations for $f$ if flow is turbulent; often swapped for Hazen-Williams in simple, cold-water municipal network design.

### 3. Hazen-Williams Equation
An empirical formula that relates the flow of water in a pipe with the physical properties of the pipe and the pressure drop caused by friction.

$$V = 0.849 C R^{0.63} S^{0.54}$$

* $V$ = Average velocity ($m/s$)
* $C$ = Hazen-Williams roughness coefficient (empirical, depends on pipe material)
* $R$ = Hydraulic radius ($m$)
* $S$ = Slope of the energy grade line (head loss per length of pipe, $h_f/L$)

> - **📜 Historical Context:** Developed by **Allen Hazen** and **Gardner Stewart Williams** in the early 1900s.
> - **✅ Primary Applications:** The default equation used in EPANET and civil engineering practice for municipal water distribution networks.
> - **⚠️ Key Limitations:** Only valid for water at ordinary temperatures (around $15^\circ C$) and turbulent flow. Completely invalid for highly viscous fluids (like oil) or hot water.

---

## 🏞️ Open Channel Hydraulics

### 4. Manning's Equation
An empirical equation used to calculate the average velocity of liquid flowing in an open channel driven by gravity.

$$V = \frac{1}{n} R^{2/3} S^{1/2}$$

* $V$ = Average velocity ($m/s$)
* $n$ = Manning's roughness coefficient (empirical)
* $R$ = Hydraulic radius ($A/P$) ($m$)
* $S$ = Channel bed slope ($m/m$)

> - **📜 Historical Context:** Proposed by Irish engineer **Robert Manning** in 1889.
> - **✅ Primary Applications:** The absolute backbone of open channel flow modelling (HEC-RAS, SWMM), sewer design, and flood routing.
> - **⚠️ Key Limitations:** Invalid for pressurised flow, flows with extremely high sediment loads (mudflows), or steep mountain torrents where water cascades rather than flows smoothly.

### 5. Froude Number
A dimensionless number used to determine the flow regime (subcritical, critical, or supercritical) in open channels, based on the ratio of inertial forces to gravitational forces.

$$Fr = \frac{V}{\sqrt{g y}}$$

* $Fr$ = Froude Number (dimensionless)
* $V$ = Flow velocity (m/s)
* $g$ = Acceleration due to gravity (9.81 m/s²)
* $y$ = Hydraulic depth (Cross-sectional area / Top width) (m)

> - **📜 Historical Context:** Named after English engineer **William Froude** in the mid-1800s (originally for ship hull resistance, later adapted for open channels).
> - **✅ Primary Applications:** Essential for designing spillways, predicting hydraulic jumps, and classifying flow states.
> - **⚠️ Key Limitations:** Does not apply to pressurised pipe flow or closed-conduit systems. 

### 6. Chézy Equation
A pioneering empirical equation for estimating the velocity of uniform flow in an open channel.

$$V = C \sqrt{R S}$$

* $V$ = Average flow velocity (m/s)
* $C$ = Chézy's roughness coefficient (depends on channel surface)
* $R$ = Hydraulic radius (m)
* $S$ = Channel bed slope (m/m)

> - **📜 Historical Context:** Developed by French engineer **Antoine de Chézy** in 1769 while designing a canal to supply water to Paris.
> - **✅ Primary Applications:** Theoretical open channel design and historical hydraulic studies. It laid the mathematical foundation for Manning's equation.
> - **⚠️ Key Limitations:** Largely superseded by Manning's equation in modern engineering because the Chézy coefficient ($C$) is harder to accurately estimate across varying water depths than Manning's $n$.

---

## 🌧️ Surface Water Hydrology

### 7. SCS Curve Number (CN) Method
An empirical method for predicting direct runoff or infiltration from rainfall excess.

$$Q = \frac{(P - I_a)^2}{(P - I_a + S)}$$

* $Q$ = Runoff depth ($mm$)
* $P$ = Total rainfall depth ($mm$)
* $I_a$ = Initial abstraction (commonly assumed as $0.2S$) ($mm$)
* $S$ = Potential maximum retention after runoff begins, where $S = \frac{25400}{CN} - 254$

> - **📜 Historical Context:** Developed by the **USDA Soil Conservation Service** (now NRCS) in 1954.
> - **✅ Primary Applications:** Estimating runoff for ungauged agricultural or urban watersheds based on soil type and land cover.
> - **⚠️ Key Limitations:** Not accurate for very large watersheds, highly forested areas with massive leaf litter, or purely concrete urban areas.

### 8. Green-Ampt Infiltration Model
A physically-based model estimating the rate at which water enters the soil, assuming a sharp wetting front.

$$f(t) = K \left( 1 + \frac{|\psi| \Delta \theta}{F(t)} \right)$$

* $f(t)$ = Infiltration rate at time $t$ ($cm/hr$)
* $K$ = Saturated hydraulic conductivity ($cm/hr$)
* $\psi$ = Suction head at the wetting front ($cm$)
* $\Delta \theta$ = Change in volumetric moisture content (porosity minus initial moisture)
* $F(t)$ = Cumulative depth of infiltrated water ($cm$)

> - **📜 Historical Context:** Developed by **W.H. Green** and **G.A. Ampt** in 1911.
> - **✅ Primary Applications:** Advanced rainfall-runoff modelling (like SWMM) where continuous simulation of soil moisture is required over long periods.
> - **⚠️ Key Limitations:** Cumbersome for quick, single-storm estimates because it requires solving implicitly. Fails in highly layered soils or soils with massive macropores (like deep root channels).

### 9. Muskingum Routing Method
A widely used hydrologic routing method that models the storage volume of flooding in a river channel to predict how a flood wave changes as it moves downstream.

$$Q_{i+1} = C_1 I_{i+1} + C_2 I_i + C_3 Q_i$$

* $Q$ = Outflow discharge
* $I$ = Inflow discharge
* $C_1, C_2, C_3$ = Routing coefficients derived from $\Delta t$, travel time ($K$), and a weighting factor ($X$)

> - **📜 Historical Context:** Developed by **G.T. McCarthy** in 1938 for the US Army Corps of Engineers during a study of the Muskingum River basin.
> - **✅ Primary Applications:** Routing flood hydrographs through long river reaches without needing full cross-sectional geometry.
> - **⚠️ Key Limitations:** Fails if there is a significant backwater effect (like from a downstream dam or tidal influence). In such cases, full dynamic hydraulic routing (HEC-RAS 1D/2D) is mandatory.

### 10. Penman-Monteith Equation
The gold standard for estimating reference Evapotranspiration ($ET_0$).

$$ET_0 = \frac{\Delta (R_n - G) + \rho_a c_p \frac{(e_s - e_a)}{r_a}}{\Delta + \gamma \left(1 + \frac{r_s}{r_a}\right)}$$

* $ET_0$ = Reference evapotranspiration ($mm/day$)
* $R_n$ = Net radiation at the crop surface ($MJ/m^2/day$)
* $G$ = Soil heat flux density
* $e_s - e_a$ = Vapour pressure deficit of the air
* $\Delta$ = Slope of the vapour pressure curve
* $\gamma$ = Psychrometric constant

> - **📜 Historical Context:** Derived by **Howard Penman** (1948) and refined for crop resistance by **John Monteith** (1965).
> - **✅ Primary Applications:** Irrigation scheduling, drought modelling, and climate change impact studies. Endorsed by the FAO.
> - **⚠️ Key Limitations:** Do not use if you lack comprehensive meteorological data (solar radiation, wind speed, humidity). 

### 11. Rational Method
The most widely used uncalibrated equation for estimating peak surface runoff from a small watershed due to a specific storm event.

$$Q_p = C i A$$

* $Q_p$ = Peak runoff rate (m³/s)
* $C$ = Runoff coefficient (dimensionless, based on land use and surface permeability)
* $i$ = Rainfall intensity for a duration equal to the time of concentration (m/s, though typically calculated in mm/hr and converted)
* $A$ = Drainage area (m²)

> - **📜 Historical Context:** Introduced by Irish engineer **Thomas Mulvaney** in 1851, and popularised in the US by Emil Kuichling in 1889.
> - **✅ Primary Applications:** Sizing storm sewers, road culverts, and small urban drainage systems where the catchment area is very small (typically less than 80 hectares / 200 acres).
> - **⚠️ Key Limitations:** Highly inaccurate for large river basins or watersheds with complex, mixed land uses. It assumes rainfall intensity is perfectly uniform over the entire catchment, which never happens in large storms.

### 12. Horton's Infiltration Equation
A classic empirical formula that models the exponential decline of soil infiltration capacity over time during a continuous rain event.

$$f(t) = f_c + (f_0 - f_c)e^{-kt}$$

* $f(t)$ = Infiltration capacity at time $t$ (mm/hr)
* $f_c$ = Final (equilibrium) infiltration capacity (mm/hr)
* $f_0$ = Initial infiltration capacity at $t=0$ (mm/hr)
* $k$ = Decay constant specific to the soil type (1/hr)
* $t$ = Time since the start of rainfall (hr)

> - **📜 Historical Context:** Developed by American hydrologist **Robert E. Horton** in 1933.
> - **✅ Primary Applications:** Continuous rainfall-runoff modelling where you need to calculate how much water pools on the surface over the lifespan of a storm. 
> - **⚠️ Key Limitations:** Fails if the rainfall intensity temporarily drops below the soil's infiltration capacity (because the soil will begin to dry and "recover," which this strict exponential decay curve does not account for).

---

## 🪨 Groundwater Hydrology

### 13. Darcy's Law
The foundational equation governing the flow of fluid through a porous medium.

$$Q = -K A \frac{dh}{dl}$$

* $Q$ = Total discharge ($m^3/s$)
* $K$ = Hydraulic conductivity ($m/s$)
* $A$ = Cross-sectional area to flow ($m^2$)
* $\frac{dh}{dl}$ = Hydraulic gradient 

> - **📜 Historical Context:** Discovered experimentally by French engineer **Henry Darcy** in 1856, based on sand filters in Dijon, France.
> - **✅ Primary Applications:** The mathematical basis for all groundwater models (like MODFLOW) and calculating seepage under dams.
> - **⚠️ Key Limitations:** Invalid for turbulent flow (e.g., in highly fractured karst/limestone aquifers or right next to a heavily pumping well).

### 14. Dupuit Equation (Unconfined Aquifer Flow)
Calculates the steady-state groundwater discharge per unit width between two observation wells in an unconfined aquifer.

$$q = \frac{K}{2L} (h_1^2 - h_2^2)$$

* $q$ = Discharge per unit width ($m^2/s$)
* $K$ = Hydraulic conductivity ($m/s$)
* $L$ = Distance between the two wells/observation points ($m$)
* $h_1, h_2$ = Hydraulic heads at points 1 and 2 ($m$)

> - **📜 Historical Context:** Formulated by **Jules Dupuit** in 1863 based on the assumption that groundwater flow is perfectly horizontal.
> - **✅ Primary Applications:** Estimating regional groundwater flow towards a trench, river, or drain in a shallow, unconfined aquifer.
> - **⚠️ Key Limitations:** Invalid where flow is highly vertical (like directly adjacent to a pumping well or near the water table's intersection with a seepage face).

### 15. Theis Equation
Used to predict the drawdown (decline in water level) in a confined aquifer due to pumping from a single well.

$$s = \frac{Q}{4 \pi T} W(u) \quad \text{where} \quad u = \frac{r^2 S}{4 T t}$$

* $s$ = Drawdown ($m$)
* $Q$ = Constant pumping rate ($m^3/day$)
* $T$ = Transmissivity ($m^2/day$)
* $S$ = Storativity (dimensionless)
* $W(u)$ = The Well function
* $r$ = Distance from the pumped well ($m$)
* $t$ = Time since pumping began ($days$)

> - **📜 Historical Context:** Developed by **Charles Vernon Theis** in 1935, applying heat-flow mathematics to groundwater.
> - **✅ Primary Applications:** Conducting aquifer pump tests to determine the hydraulic properties of a confined aquifer over time (transient flow).
> - **⚠️ Key Limitations:** Invalid for unconfined aquifers, aquifers that are not uniform/isotropic, or if the pumping rate fluctuates wildly.

### 16. Thiem Equation (Steady-State Confined Flow)
Calculates the transmissivity of a confined aquifer based on the steady-state drawdown observed in two monitoring wells.

$$Q = \frac{2 \pi T (h_2 - h_1)}{\ln(r_2 / r_1)}$$

* $Q$ = Constant pumping rate from the main well (m³/day)
* $T$ = Transmissivity of the aquifer (m²/day)
* $h_1, h_2$ = Hydraulic heads at observation wells 1 and 2 (m)
* $r_1, r_2$ = Radial distances from the pumping well to observation wells 1 and 2 (m)

> - **📜 Historical Context:** Developed by German hydrologist **Günther Thiem** in 1906, adapting the earlier work of Jules Dupuit.
> - **✅ Primary Applications:** Analysing aquifer pump test data after the water levels have completely stabilised (reached steady-state) to determine how easily water moves through the confined rock/sand.
> - **⚠️ Key Limitations:** Cannot be used during the initial hours/days of a pump test when water levels are still actively dropping (you must use the Theis equation for that transient state). Invalid for unconfined aquifers.
