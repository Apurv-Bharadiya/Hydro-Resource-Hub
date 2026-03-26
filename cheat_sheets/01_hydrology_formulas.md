# 📐 Hydrology & Fluid Mechanics Master Cheat Sheet

A comprehensive, deep-dive reference guide to the fundamental and advanced equations used in Water Resources Engineering, fluid dynamics, and computational modeling.

---

## 🌊 Fluid Mechanics & Pipe Flow

### 1. Bernoulli's Equation (Conservation of Energy)
Describes the behavior of a fluid under varying conditions of pressure and height, stating that the total mechanical energy of a flowing fluid remains constant.

$$\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_f$$

* $P$ = Pressure ($N/m^2$)
* $\gamma$ = Specific weight of the fluid ($N/m^3$)
* $V$ = Fluid velocity ($m/s$)
* $z$ = Elevation head ($m$)
* $g$ = Acceleration due to gravity ($9.81m/s^2$)
* $h_f$ = Head loss due to friction ($m$)

> - **📜 Who & When:** Published by Swiss mathematician **Daniel Bernoulli** in 1738 in his book *Hydrodynamica*.
> - **✅ Where to use:** Designing pipe networks, calculating pump head requirements, and understanding pitot tubes.
> - **⚠️ When NOT to use:** Cannot be used (in its strict theoretical form) for highly compressible fluids (gases at high speeds), highly viscous fluids, or flows where massive temperature changes occur.

### 2. Darcy-Weisbach Equation
The most theoretically robust equation for calculating the friction head loss in a pipe.

$$h_f = f \frac{L}{D} \frac{V^2}{2g}$$

* $h_f$ = Head loss due to friction ($m$)
* $f$ = Darcy friction factor (dimensionless, found via Moody chart)
* $L$ = Length of the pipe ($m$)
* $D$ = Diameter of the pipe ($m$)
* $V$ = Average flow velocity ($m/s$)

> - **📜 Who & When:** Developed by **Henry Darcy** (1857) and modified by **Julius Weisbach** (1845).
> - **✅ Where to use:** Standard for modeling pressurized pipe systems (like EPANET).
> - **⚠️ When NOT to use:** Requires iterative calculations for $f$ if flow is turbulent; purely empirical formulas like Hazen-Williams are sometimes preferred for quick, simple water distribution estimates.

---

## 🏞️ Open Channel Hydraulics

### 3. Manning's Equation
An empirical equation used to calculate the average velocity of liquid flowing in an open channel driven by gravity.

$$V = \frac{1}{n} R^{2/3} S^{1/2}$$

* $V$ = Average velocity ($m/s$)
* $n$ = Manning's roughness coefficient (empirical)
* $R$ = Hydraulic radius ($A/P$) ($m$)
* $S$ = Channel bed slope ($m/m$)

> - **📜 Who & When:** Proposed by Irish engineer **Robert Manning** in 1889.
> - **✅ Where to use:** The absolute backbone of open channel flow modeling (HEC-RAS, SWMM), sewer design, and flood routing.
> - **⚠️ When NOT to use:** Invalid for pressurized flow, flows with extremely high sediment loads (mudflows), or steep mountain torrents where water cascades rather than flows smoothly.

---

## 🌧️ Surface Water Hydrology

### 4. SCS Curve Number (CN) Method
An empirical method for predicting direct runoff or infiltration from rainfall excess.

$$Q = \frac{(P - I_a)^2}{(P - I_a + S)}$$

* $Q$ = Runoff depth ($mm$)
* $P$ = Total rainfall depth ($mm$)
* $I_a$ = Initial abstraction (commonly assumed as $0.2S$) ($mm$)
* $S$ = Potential maximum retention after runoff begins, where $S = \frac{25400}{CN} - 254$

> - **📜 Who & When:** Developed by the **USDA Soil Conservation Service** (now NRCS) in 1954.
> - **✅ Where to use:** Estimating runoff for ungauged agricultural or urban watersheds based on soil type and land cover.
> - **⚠️ When NOT to use:** Not accurate for very large watersheds, highly forested areas with massive leaf litter, or purely concrete urban areas (where the rational method is better). It does not produce a time-distributed hydrograph without further routing.

### 5. Penman-Monteith Equation
The gold standard for estimating reference Evapotranspiration ($ET_0$).

$$ET_0 = \frac{\Delta (R_n - G) + \rho_a c_p \frac{(e_s - e_a)}{r_a}}{\Delta + \gamma \left(1 + \frac{r_s}{r_a}\right)}$$

* $ET_0$ = Reference evapotranspiration ($mm/day$)
* $R_n$ = Net radiation at the crop surface ($MJ/m^2/day$)
* $G$ = Soil heat flux density
* $e_s - e_a$ = Vapor pressure deficit of the air
* $\Delta$ = Slope of the vapor pressure curve
* $\gamma$ = Psychrometric constant

> - **📜 Who & When:** Derived by **Howard Penman** (1948) and refined for crop resistance by **John Monteith** (1965).
> - **✅ Where to use:** Irrigation scheduling, drought modeling, and climate change impact studies. Endorsed by the FAO (Food and Agriculture Organization).
> - **⚠️ When NOT to use:** Do not use if you lack comprehensive meteorological data (solar radiation, wind speed, humidity). If data is scarce, simpler methods like Hargreaves are required.

---

## 🪨 Groundwater Hydrology

### 6. Darcy's Law
The foundational equation governing the flow of fluid through a porous medium.

$$Q = -K A \frac{dh}{dl}$$

* $Q$ = Total discharge ($m^3/s$)
* $K$ = Hydraulic conductivity ($m/s$)
* $A$ = Cross-sectional area to flow ($m^2$)
* $\frac{dh}{dl}$ = Hydraulic gradient 

> - **📜 Who & When:** Discovered experimentally by French engineer **Henry Darcy** in 1856 based on sand filters in Dijon, France.
> - **✅ Where to use:** The mathematical basis for all groundwater models (like MODFLOW) and calculating seepage under dams.
> - **⚠️ When NOT to use:** Invalid for turbulent flow (e.g., in highly fractured karst/limestone aquifers or right next to a heavily pumping well where flow velocities are too high).

### 7. Theis Equation
Used to predict the drawdown (decline in water level) in a confined aquifer due to pumping from a single well.

$$s = \frac{Q}{4 \pi T} W(u) \quad \text{where} \quad u = \frac{r^2 S}{4 T t}$$

* $s$ = Drawdown ($m$)
* $Q$ = Constant pumping rate ($m^3/day$)
* $T$ = Transmissivity ($m^2/day$)
* $S$ = Storativity (dimensionless)
* $W(u)$ = The Well function
* $r$ = Distance from the pumped well ($m$)
* $t$ = Time since pumping began ($days$)

> - **📜 Who & When:** Developed by **Charles Vernon Theis** in 1935, applying heat-flow mathematics to groundwater.
> - **✅ Where to use:** Conducting aquifer pump tests to determine the hydraulic properties of a confined aquifer over time (transient flow).
> - **⚠️ When NOT to use:** Invalid for unconfined aquifers, aquifers that are not uniform/isotropic, or if the pumping rate fluctuates wildly.
