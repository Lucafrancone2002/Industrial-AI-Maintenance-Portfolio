# Industrial AI & Automation Portfolio
### Luca Francone — Automation & Control Engineering

This repository presents a collection of technical projects focused on the application of Machine Learning and Digital Signal Processing within the domain of Industrial Reliability and Automation. The primary objective is to demonstrate the integration of Control Theory with data-driven prognostic and diagnostic frameworks.

---

## 1. Remaining Useful Life (RUL) Estimation for Turbofan Engines
**Focus:** Prognostics and Health Management (PHM)

This project implements a predictive maintenance framework utilizing the NASA CMAPSS dataset. The analysis focuses on the transition from nominal operational states to functional failure in high-bypass turbofan engines.

* **Methodology:** Development of a continuous RUL target through cycle-based degradation mapping.
* **Feature Engineering:** Statistical correlation analysis to identify high-fidelity degradation signals in sensor telemetry (e.g., thermal and pressure drift).
* **Analysis:** Evaluation of sensor signal divergence as a proxy for hardware fatigue and structural wear.

**Technical Documentation:** [NASA_RUL_Analysis.ipynb](./01_Predictive_Maintenance_RUL/NASA_RUL_Analysis.ipynb)

---

## 2. Real-Time Anomaly Detection in Industrial Control Loops
**Focus:** Fault Detection and Isolation (FDI)

An investigation into identifying operational deviations and sensor faults using both classical statistical methods and Deep Learning architectures.

* **Baseline:** Implementation of a 3-Sigma statistical control framework to establish a nominal operating envelope.
* **Neural Architecture:** Development of a Deep Autoencoder using the PyTorch framework to identify non-linear anomalies through reconstruction error analysis.
* **Comparative Study:** Evaluation of the trade-off between statistical sensitivity and the robustness of unsupervised learning models in detecting sensor drift.

**Technical Documentation:** [Anomaly_Detection_Core.ipynb](./02_Anomaly_Detection_Control_Signals/Anomaly_Detection_Core.ipynb)

---

## Technical Stack and Competencies
* **Computational Frameworks:** Python (NumPy, Pandas, Scikit-Learn, PyTorch).
* **Engineering Domains:** Reliability Engineering, Digital Signal Processing, System Identification, Control Systems.
* **Modeling Tools:** Jupyter Notebooks, Git Version Control, MATLAB/Simulink.

---

## Repository Structure
* `01_Predictive_Maintenance_RUL/`: Prognostic analysis and RUL estimation.
* `02_Anomaly_Detection_Control_Signals/`: Diagnostic frameworks and anomaly detection.
* `docs/`: Technical abstracts and supporting documentation.