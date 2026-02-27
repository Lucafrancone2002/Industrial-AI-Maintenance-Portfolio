# Technical Abstract: Real-Time Anomaly Detection in Control Signals
**Domain:** Fault Detection and Isolation (FDI)  
**Author:** Luca Francone  

## 1. Executive Summary
This investigation addresses the challenge of identifying operational anomalies within automated industrial control loops. The project implements a dual-layered diagnostic system that monitors sensor signals to detect faults, drift, or sudden hardware deviations. The focus is on ensuring high signal integrity, which is essential for maintaining the precision required in modern automated manufacturing environments.

## 2. Technical Methodology
The study compares two distinct analytical paradigms:
* **Statistical Process Control (Baseline):** The implementation of a **3-Sigma** framework. This method establishes a "normal" operating band based on moving averages and standard deviations. Any signal exiting this band is flagged as an outlier.
* **Deep Learning Reconstruction (AI):** Using a **PyTorch-based Autoencoder**. This neural network is trained to "learn" the unique fingerprint of healthy operation. When presented with faulty data, the model fails to reconstruct the signal accurately. The resulting **Reconstruction Error** serves as a sophisticated, non-linear anomaly indicator.

## 3. Key Findings and Insights
* **Sensitivity Improvements:** While the 3-Sigma method is effective for detecting sudden spikes, the Autoencoder proved superior in identifying subtle, slow-drifting sensor faults that traditional statistics might overlook.
* **Noise vs. Fault Differentiation:** The AI model successfully learned to ignore stochastic (random) noise, reducing the rate of "false positives" that often plague industrial alarm systems.
* **Adaptive Thresholding:** By analyzing the reconstruction error distribution, the system can automatically adjust its sensitivity to different operational phases, providing a more robust monitoring solution.

## 4. Industrial Applications
In precision-driven environments like **High-Tech Automation**, detecting a sensor fault in real-time prevents the propagation of errors throughout the control loop. This prevents hardware damage and ensures that the final product meets strict quality tolerances without requiring constant human supervision.