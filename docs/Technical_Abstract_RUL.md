# Technical Abstract: Predictive Maintenance and RUL Estimation
**Author:** Luca Francone  
**Focus:** Reliability Engineering, Signal Processing, and Data-Driven Diagnostics  

## 1. Executive Summary
This project implements a data-driven framework for estimating the **Remaining Useful Life (RUL)** of complex industrial equipment. By analyzing high-frequency sensor telemetry from the NASA CMAPSS dataset, the study identifies degradation patterns and identifies critical "Health Indicators" to predict potential hardware failures before they occur.

## 2. Methodology
The analysis follows a rigorous three-step engineering workflow:
* **Target Engineering:** Conversion of time-series operational cycles into a continuous RUL target variable, mapping asset life from healthy state to functional failure.
* **Statistical Feature Selection:** Implementation of a correlation-based analysis to filter 21 sensor streams. This step identifies which physical parameters (e.g., temperature, pressure, rotation speeds) show the strongest statistical drift relative to equipment wear.
* **Signal Visualization:** Generation of trend-analysis plots and correlation heatmaps to provide actionable insights into the equipment's health state.

## 3. Key Findings (Preliminary)
* **Identification of High-Impact Sensors:** Sensors such as `s11` and `s12` demonstrate a high negative correlation with RUL, making them primary candidates for early-warning detection systems.
* **System Degradation Profiles:** The study confirms that equipment health does not always decline linearly; significant signal variance and "noise" increase as the asset approaches its critical failure point.

## 4. Industrial Application
This methodology is directly applicable to high-tech manufacturing environments (such as Semiconductor Tooling) where maximizing **MTBF (Mean Time Between Failures)** and reducing unscheduled downtime are critical for operational efficiency and cost reduction.

---
*Note: This abstract represents a technical proof-of-concept using public industrial datasets.* 

