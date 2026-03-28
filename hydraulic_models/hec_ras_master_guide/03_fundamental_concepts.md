# 🧠 Chapter 3: Fundamental Hydraulic Concepts (The Physics)

Software buttons change, but engineering physics do not. To troubleshoot a failing model, you must understand the mathematical equations HEC-RAS is attempting to solve behind the scenes.

---

## 1D vs 2D Flow

### 1D Flow (One-Dimensional)
Assumes water flows exclusively in one direction: longitudinally downstream. 
* **How it works:** You draw cross-sections (lines perpendicular to the river). The software calculates the water surface elevation at Cross-Section 1, then computes the energy loss to find the elevation at Cross-Section 2.
* **Why it matters:** It is fast, stable, and excellent for confined river channels. However, it cannot accurately model water spilling out into a flat floodplain and flowing sideways.

### 2D Flow (Two-Dimensional)
Solves equations across a continuous grid, allowing water to flow in both $X$ and $Y$ directions.
* **How it works:** You lay a computational mesh over the terrain. HEC-RAS calculates the volume, velocity, and depth at the center of every single cell, mapping how water spills across faces into neighboring cells.
* **Why it matters:** It is computationally heavy but essential for complex urban environments, dam breaches, and wide, flat floodplains.

---

## Steady vs Unsteady Flow

### Steady Flow
Flow rate ($Q$) remains **constant** over time. 
* **Use Case:** "What is the absolute maximum water level if a 500 m³/s flood hits this bridge?"
* **Physics:** Solved using the standard Energy Equation.

### Unsteady Flow
Flow rate **changes** over time (a Hydrograph). 
* **Use Case:** "How long will it take for the peak of the flood wave to travel from the dam to the city, and how much will the floodplain store along the way?"
* **Physics:** Solved using the Saint-Venant equations.

---

## The Governing Equations

### The Saint-Venant Equations (1D Unsteady Flow)
These equations balance the conservation of mass (Continuity) and the conservation of momentum.

**1. Continuity Equation (Conservation of Mass):**
Water cannot be created or destroyed. What goes in must come out, plus or minus a change in storage.
$$\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = 0$$
*(Where $A$ is cross-sectional area, $t$ is time, $Q$ is flow, and $x$ is distance).*

**2. Momentum Equation (Conservation of Momentum):**
Accounts for the forces pushing the water (gravity) and slowing it down (friction).
$$\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA \frac{\partial H}{\partial x} + gA S_f = 0$$
*(Where $g$ is gravity, $H$ is water surface elevation, and $S_f$ is the friction slope).*

> ⚠️ **Why this matters in HEC-RAS:** If you set your computational time step ($\Delta t$) too large, the software attempts to push too much water ($Q$) across too large of a distance ($\Delta x$) in a single calculation. The matrix math fails to converge, and your model crashes.

---

## Manning’s Equation

Used to calculate the friction slope ($S_f$) in the momentum equation.

$$V = \frac{1}{n} R^{2/3} S^{1/2}$$
*(Where $V$ is velocity, $n$ is Manning's roughness coefficient, $R$ is hydraulic radius, and $S$ is the energy slope).*

### Why Manning's $n$ is your most important variable
Manning's $n$ is the primary parameter you will adjust during model **calibration**. 
* If your model says the flood depth is 2 meters, but historical gauge data says it was 2.5 meters, you might have underestimated the friction of the dense brush on the floodplain. 
* Increasing $n$ artificially slows the water down, causing it to pool deeper to push the same volume through the reach.

<br>

---
**[⬅️ Chapter 02: Installation & Setup](./02_installation_setup.md)** | **[🏠 Main Index](./00_index.md)** | **[Chapter 04: Data Requirements ➡️](./04_data_requirements.md)**
