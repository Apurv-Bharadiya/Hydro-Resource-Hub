# 📐 Hydrology & Fluid Mechanics Cheat Sheet

A quick-reference guide to the fundamental equations used in Water Resources Engineering, open-channel flow, and groundwater modelling.

---

## 🌊 Open Channel Flow & Hydraulics

### 1. Continuity Equation
The principle of conservation of mass for incompressible fluids in a pipe or channel.
$$Q = A_1 V_1 = A_2 V_2$$
* $Q$ = Discharge / Flow rate ($m^3/s$)
* $A$ = Cross-sectional area of flow ($m^2$)
* $V$ = Average velocity ($m/s$)

### 2. Manning's Equation
Used to calculate the average velocity of liquid flowing in an open channel driven by gravity.
$$V = \frac{1}{n} R^{2/3} S^{1/2}$$
$$Q = \frac{1}{n} A R^{2/3} S^{1/2}$$
* $n$ = Manning's roughness coefficient
* $R$ = Hydraulic radius ($A / P$) where $P$ is the wetted perimeter ($m$)
* $S$ = Channel slope ($m/m$)

### 3. Froude Number
A dimensionless number used to determine the flow regime (subcritical, critical, or supercritical) in open channels.
$$Fr = \frac{V}{\sqrt{g y}}$$
* $V$ = Flow velocity ($m/s$)
* $g$ = Acceleration due to gravity ($9.81 m/s^2$)
* $y$ = Hydraulic depth ($m$)
* *Note: If $Fr < 1$ (Subcritical), $Fr = 1$ (Critical), $Fr > 1$ (Supercritical).*

---

## 🌧️ Surface Water Hydrology

### 4. Rational Method
Used to estimate peak surface runoff rate from a small watershed due to a specific rainfall event.
$$Q_p = C i A$$
* $Q_p$ = Peak runoff rate
* $C$ = Runoff coefficient (dimensionless, based on land use)
* $i$ = Rainfall intensity
* $A$ = Drainage area

---

## 🪨 Groundwater Hydrology

### 5. Darcy's Law
Describes the flow of a fluid through a porous medium, foundational for groundwater modelling (like MODFLOW).
$$Q = -K A \frac{dh}{dl}$$
* $Q$ = Total discharge ($m^3/s$)
* $K$ = Hydraulic conductivity ($m/s$)
* $A$ = Cross-sectional area to flow ($m^2$)
* $\frac{dh}{dl}$ = Hydraulic gradient (change in head over distance)

---

## 💧 Fluid Mechanics

### 6. Reynolds Number
Helps predict flow patterns in different fluid flow situations (laminar vs. turbulent).
$$Re = \frac{\rho V D}{\mu} = \frac{V D}{\nu}$$
* $\rho$ = Fluid density ($kg/m^3$)
* $V$ = Flow velocity ($m/s$)
* $D$ = Characteristic length (e.g., pipe diameter) ($m$)
* $\mu$ = Dynamic viscosity ($Pa \cdot s$)
* $\nu$ = Kinematic viscosity ($\mu / \rho$) ($m^2/s$)
