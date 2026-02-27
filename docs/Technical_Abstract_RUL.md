# Technical Abstract: Prognostics and Remaining Useful Life (RUL) Estimation
**Domain:** Reliability Engineering & Predictive Maintenance  
**Author:** Luca Francone  

## 1. Executive Summary
This project develops a computational framework to estimate the **Remaining Useful Life (RUL)** of industrial assets, specifically high-bypass turbofan engines. By leveraging high-frequency telemetry data from the NASA CMAPSS dataset, the study successfully maps the transition from a nominal "healthy" state to a critical "failure" state. This allows for proactive maintenance, effectively reducing the risks associated with unscheduled downtime in precision-critical industries.

## 2. Methodology and Workflow
The research follows a structured three-phase engineering approach:
* **Target Synthesis:** Transforming raw operational cycle counts into a continuous RUL variable. This creates a quantitative timeline that represents the hardware's degradation path over time.
* **Feature Selection Strategy:** Not all sensor data is informative. Through statistical correlation mapping, the project filters 21 distinct sensor streams to isolate those showing the strongest physical drift. This ensures the model focuses on the most reliable indicators of wear.
* **Exploratory Signal Analysis:** Utilizing data visualization to observe how physical parameters (e.g., temperatures, pressures) diverge from their baseline as the asset approaches its end-of-life.

## 3. Key Findings and Results
* **Detection of Critical Health Indicators:** Sensors `s11` and `s12` (related to outlet temperatures) were identified as high-fidelity signals. Their consistent drift patterns provide early warning signatures long before catastrophic failure occurs.
* **Non-Linear Degradation Patterns:** The analysis reveals that equipment wear is rarely linear. As the asset reaches late-stage degradation, signal variance and "noise" increase significantly, indicating a loss of structural stability within the system.
* **Correlation Precision:** The study achieved a clear statistical hierarchy of sensors, distinguishing between stable parameters and those susceptible to environmental and operational stress.

## 4. Industrial Implications
This framework is highly relevant for the **Semiconductor Manufacturing** industry. By predicting failure, companies can shift from reactive repairs to optimized maintenance schedules, maximizing **Mean Time Between Failures (MTBF)** and protecting expensive wafer production cycles.