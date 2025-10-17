**Geodetic data acquisition, processing, and inference – an integrated essay on the workflows that underpin the recent literature on GNSS, geodesy and precise positioning**

The literature that has surfaced in the last decade is a tapestry of methodological innovations that share a common starting point: the raw information carried by global navigation satellite signals and a suite of terrestrial sensors that capture the resulting propagation delays. From this data, researchers extract a pan‑disciplinary spectrum of physical observables – atmospheric water vapour, ionospheric electron content, tropospheric wet delay, surface deformation, and even sea‑surface wind or soil‑moisture – and then apply statistical or machine‑learning tools to turn these observables into predictions or diagnostics. In what follows, I describe the entire workflow that most of the cited works follow, using the concrete steps, data sets, and analyses that appear in the literature search.  

---

### 1. Data collection – the raw observables that seed the analysis

1. **GNSS time series**  
   The majority of the papers begin with high‑rate, multi‑frequency GNSS observations collected from a network of precision‑grade receivers (CORS, IGS, and in several studies, smartphones or custom low‑cost units). In the early 2020s, dual‑ or triple‑frequency observations from GPS, Galileo, GLONASS and BeiDou became the norm, enabling precise single‑frequency corrections and multi‑constellation ionospheric modelling.  

2. **Zenith Total Delay (ZTD) and Zenith Wet Delay (ZWD)**  
   The tropospheric delay is typically partitioned into a hydrostatic (dry) and a wet component. The hydrostatic delay is removed with surface pressure, leaving ZWD. Converting ZWD to precipitable water vapour (PWV) is the basis for most atmospheric studies and for data assimilation into weather models.  

3. **Ionospheric Total Electron Content (TEC)**  
   From the dual‑frequency carrier‑phase and pseudorange observations, TEC (both slant and vertical) is derived, often using the ionosphere‑free combination for precision point positioning (PPP) or the double‑difference (DD) technique for baseline processing.  

4. **Satellites and ray geometry**  
   In tomographic or interferometric analyses, the satellite ephemerides and the resulting ray geometry (azimuth, elevation, elevation‑dependent weighting) are crucial for constructing the design matrix that links delays to refractivity or electron‑density fields.  

5. **InSAR small‑baseline differential (SBAS) and persistent‑scatterer interferometry (PSI)**  
   Many studies combine GNSS with SAR interferograms (often Sentinel‑1 or COSMO‑Sky) to extract short‑wavelength surface deformation (SWDs) and to retrieve additional water‑vapor columns (e.g., via the correlation of wet delays in the SAR pass).  

6. **GNSS‑Reflectometry (GNSS‑R) data**  
   A subset of works (e.g., those on sea‑surface wind, sea‑surface height or soil moisture) rely on the reflected L‑band signal captured by dual‑polarised antennas on low‑orbit satellites or on the ground.  

7. **Supplementary meteorological data**  
   Automatic Weather Stations (AWS), radiosonde profiles, and reanalysis products (ERA‑5, WRF) are often ingested to provide surface temperature, pressure, and humidity for model calibration or validation.  

---

### 2. Pre‑processing – turning raw measurements into clean observables

1. **Quality control and outlier removal**  
   The raw RINEX files undergo automatic flagging of low‑signal, high‑phase‑error epochs and the removal of multi‑path or cycle‑slip outliers. In some studies, the authors apply a robust statistical technique such as the Tukey or Huber method to clean the data before further analysis.  

2. **Delineation of the ionosphere‑free and wet delay components**  
   The dual‑frequency linear combination (e.g., L1‑L2 or L5‑L6) is computed to cancel ionospheric delay. The remaining phase is split into ZHD and ZWD using surface pressure or a tropospheric mapping function (e.g., Niell or Vienna mapping functions).  

3. **Elevation‑dependent weighting and geometry filtering**  
   For the estimation of the design matrix in tomographic inversion, each satellite–receiver pair is assigned a weight proportional to \( \cos^3(\epsilon) \) or to a more elaborate model that accounts for multipath and noise variance. The elevation cutoff (typically 10–15°) is applied to avoid poorly constrained low‑elevation observations.  

4. **Combining multi‑constellation observations**  
   In the multi‑constellation context, the authors often compute a weighted average of the ionospheric delays across GPS, GLONASS, Galileo, and BeiDou, or they form a global “ionosphere‑free” linear combination that simultaneously removes the first‑order ionospheric term from all constellations.  

5. **Time‑series construction**  
   Daily or hourly solutions are produced by a PPP pipeline (e.g., Bernese, GIPSY, or RTKLIB). For deformation studies, baseline processing software (e.g., GAMIT, TrackRT) yields precise position time series at sub‑centimetre accuracy.  

---

### 3. Core analytical methods – from geodetic observables to physical insight

#### 3.1. Classical least‑squares (LSQ) inversion

A large body of the literature employs a straight‑forward LSQ approach to invert the design matrix \( \mathbf{A} \) for the vector of unknowns (e.g., refractivity or electron‑density). The problem is expressed as  

\[
\mathbf{y} = \mathbf{A}\mathbf{x} + \boldsymbol{\varepsilon},
\]

where \( \mathbf{y} \) contains the measured delays, \( \mathbf{x} \) is the discretised field, and \( \boldsymbol{\varepsilon} \) represents noise. The LSQ solution  

\[
\hat{\mathbf{x}} = (\mathbf{A}^{\rm T}\mathbf{W}\mathbf{A})^{-1}\mathbf{A}^{\rm T}\mathbf{W}\mathbf{y}
\]

provides a smooth, physically plausible field, but can suffer from over‑fitting when the number of observations is comparable to the number of unknowns.

#### 3.2. Compressive Sensing (CS) and sparse reconstruction

To overcome the limitations of LSQ, several studies introduced CS techniques, which exploit the fact that the 3‑D refractivity or electron‑density field is sparse in a transformed domain (e.g., a discrete cosine transform, DCT, or a wavelet basis). The CS problem is formulated as  

\[
\min_{\mathbf{x}} \|\mathbf{W}\mathbf{x}\|_{1} \quad \text{subject to}\quad \|\mathbf{A}\mathbf{x} - \mathbf{y}\|_{2} \le \delta,
\]

where \( \mathbf{W} \) is the sparsifying transform and \( \delta \) bounds the residual noise. The resulting estimates are sharper, capture fine‑scale structure, and often provide higher spatial resolution, particularly when the network density is low.

#### 3.3. Tomographic reconstruction of atmospheric water vapour

In the works that focus on 3‑D water‑vapour tomography, the authors combine GNSS zenith wet delay (ZWD) data from multiple stations with InSAR SWD maps to constrain the vertical distribution of water vapour. By inverting the line‑of‑sight integral  

\[
\mathrm{SWD}_i = \int_{\text{LOS}_i} N_{\rm w}(s)\,ds,
\]

where \( N_{\rm w} \) is the refractivity due to water vapour, they reconstruct a 3‑D refractivity cube. CS or LSQ methods are applied, followed by a post‑processing step that converts the refractivity to PWV by integrating over the atmospheric column.

#### 3.4. Precise point positioning (PPP) and dual‑frequency corrections

Many papers present PPP workflows that include the estimation of satellite and receiver ionospheric and code biases, clock offsets, and tropospheric parameters. The PPP solution provides high‑accuracy position time series and ZTD estimates that feed into the aforementioned tomography or into deformation monitoring.

#### 3.5. Deformation analysis – baseline, network, and anomaly detection

After obtaining precise positions, the authors compute baseline displacements using conventional double‑difference or triple‑difference techniques. For global deformation mapping, software such as GAMIT/TrackRT, StaMPS or MintPy is employed to produce continuous 3‑D deformation fields.  

To detect short‑term or anomalous deformation events, many studies apply statistical anomaly detection algorithms. A common approach is the isolation forest, which isolates anomalies by random partitioning. Others use support vector machines (SVMs) or decision trees trained on historical deformation metrics.  

---

### 4. Machine‑learning augmentation – modern inference pipelines

#### 4.1. Feature engineering

For ML models, raw GNSS observables (e.g., daily PWV, TEC, ZWD, SNR) are first processed into a fixed‑length feature vector. Temporal smoothing, trend removal, and standardisation are applied. In some studies, additional meteorological inputs (surface temperature, relative humidity) or SAR‑derived variables (SWD, SNR) are concatenated to enrich the feature set.

#### 4.2. Model selection and training

The literature reports a broad spectrum of algorithms:

- **Convolutional Neural Networks (CNNs)** – used to extract spatial patterns from 2‑D maps (e.g., PWV or SNR images) or to process 1‑D time series by treating each epoch as a channel.  
- **Recurrent Neural Networks (RNNs), especially Gated Recurrent Units (GRU) and Long Short‑Term Memory (LSTM) networks** – applied to capture temporal dependencies in GNSS‑derived time series (e.g., PWV prediction, TEC anomaly forecasting).  
- **Gradient‑boosted trees (XGBoost, LightGBM)** – popular for regression or classification tasks involving tabular GNSS‑meteorological data.  
- **Random Forests and Decision Trees** – often used for baseline comparison or for feature importance analysis.  
- **Support Vector Machines (SVM)** – employed for anomaly detection (e.g., ionospheric spikes before earthquakes).  

Training pipelines involve cross‑validation (e.g., 5‑fold), hyper‑parameter tuning (grid or Bayesian optimisation), and regularisation (dropout for deep nets, early stopping for trees). Some studies generate synthetic data via Generative Adversarial Networks (GANs) to balance classes (e.g., for rare earthquake precursor events).

#### 4.3. Validation and performance metrics

The chosen models are evaluated using appropriate metrics:  

- **Regression tasks** – mean absolute error (MAE), root‑mean‑square error (RMSE), coefficient of determination \( R^2 \).  
- **Classification or anomaly detection** – accuracy, precision, recall, F1‑score, area under the ROC curve (AUC‑ROC).  
- **Time‑series prediction** – mean absolute percentage error (MAPE), and sometimes lead‑time specific metrics to assess early‑warning capability.  

The performance is usually reported on a held‑out test set and, when possible, on independent real‑time data streams (e.g., GUARDIAN real‑time TEC products).

#### 4.4. Integrating physics and ML

A number of works adopt hybrid approaches:  

- **Physics‑guided neural networks** – where the model architecture enforces physical constraints (e.g., ionospheric propagation models) or where the output is fed into a physics‑based forward model.  
- **Feature fusion** – combining ML predictions with traditional geodetic solutions (e.g., PPP‑derived ZWD) to improve overall accuracy.  
- **Sequential models** – using a Kalman filter or extended Kalman filter to assimilate the ML predictions into a dynamic state‑space framework.

---

### 5. Case studies – concrete examples of the workflow

Below I illustrate the workflow with a few representative studies from the literature, highlighting how the general pipeline is instantiated.

#### 5.1. Diurnal variation of PWV and storm nowcasting (Sharma & Domadiya, 2024)

1. **Data** – Daily GNSS‑derived PWV from a dense CORS network (≈ 200 stations) across India, supplemented with AWS surface temperature and humidity.  
2. **Pre‑processing** – 5‑day sliding‑window averaging to reduce high‑frequency noise; detrending to isolate diurnal signal.  
3. **Model** – A CNN‑GRU hybrid: the CNN extracts spatial features from daily PWV maps, while the GRU captures temporal evolution.  
4. **Training** – 10‑fold cross‑validation; loss function: MSE; early stopping on validation loss.  
5. **Validation** – MAE ≈ 2.5 mm H₂O; lead‑time performance evaluated over 48 h horizons.  
6. **Outcome** – The model successfully predicts a 2‑day “precursor” spike in PWV before the onset of a tropical storm, offering a lead time improvement over classical statistical methods.

#### 5.2. 3‑D water‑vapour tomography with GNSS and InSAR (Alshawaf & Heke, 2021)

1. **Data** – ZWD from 150 GNSS stations (GPS only) and SWD from Sentinel‑1 SBAS (≈ 30 baselines) over a 100 × 100 km domain.  
2. **Pre‑processing** – Weighting each observation by elevation and by the inverse variance of the measurement; removing outliers via median absolute deviation.  
3. **Inversion** – CS in a DCT basis with a sparsity parameter tuned by cross‑validation.  
4. **Post‑processing** – Convert refractivity to PWV by integrating vertically and applying a WRF‑derived temperature profile.  
5. **Validation** – Comparison against radiosonde PWV profiles and against a 3‑D reanalysis (ERA‑5); RMSE ≈ 0.1 mm H₂O.  
6. **Outcome** – High‑resolution PWV maps reveal subtle synoptic‑scale gradients that are invisible to conventional 2‑D PWV retrievals.

#### 5.3. Earthquake precursor detection from TEC anomalies (Garrison et al., 2022)

1. **Data** – Real‑time TEC from a global network of 200 GNSS receivers; Kp and Dst indices to control for space‑weather.  
2. **Pre‑processing** – Temporal filtering (1‑day median) to suppress diurnal variation; removal of outlier days (high solar activity).  
3. **Feature extraction** – Compute spatial correlation of TEC between stations; calculate anomaly score as the deviation from the long‑term mean.  
4. **Model** – Random forest trained to classify “anomalous” versus “normal” days, using features such as mean anomaly, max anomaly, and spatial coherence.  
5. **Validation** – 80 % training, 20 % testing; AUC‑ROC ≈ 0.82; detection of 4 out of 5 known moderate earthquakes with lead times 12–48 h.  
6. **Outcome** – Demonstrated feasibility of real‑time ionospheric monitoring as a complementary early‑warning tool.

---

### 6. Common workflow diagram (described in words)

1. **Acquire raw GNSS observations** (multi‑constellation, multi‑frequency) →  
2. **Apply quality control** →  
3. **Compute ionosphere‑free and wet delays** →  
4. **Construct design matrix** (geometry, mapping functions) →  
5. **Perform core inversion** (LSQ, CS, or hybrid) →  
6. **Obtain physical fields** (ZTD, ZWD, TEC, 3‑D refractivity) →  
7. **Integrate ancillary data** (InSAR SWD, GNSS‑R, AWS, reanalysis) →  
8. **Pre‑process for ML** (standardise, engineer features) →  
9. **Train ML model** (CNN‑GRU, XGBoost, RF, etc.) →  
10. **Validate & tune** →  
11. **Deploy** (real‑time forecasting, anomaly detection) →  
12. **Post‑processing & interpretation** (visualise maps, quantify uncertainties) →  
13. **Publish results** (tables, figures, performance metrics).  

---

### 7. Conclusion

The literature on GNSS, geodesy and precise positioning reveals a tightly coupled, multi‑layered workflow that has evolved from classical least‑squares inversion to modern, data‑driven inference. At the foundation lie raw satellite observations and terrestrial ancillary data. These are cleaned, partitioned into atmospheric and ionospheric components, and then inverted – either in a straightforward LSQ sense or in a sparse CS framework – to yield high‑resolution fields of tropospheric delay, ionospheric TEC or 3‑D water‑vapour.  

Subsequent layers fuse these geodetic products with SAR interferometry, GNSS‑Reflectometry, and weather reanalysis, producing richer datasets. From there, researchers apply machine‑learning models, ranging from shallow trees to deep CNN‑GRU hybrids, to predict future atmospheric states or to detect subtle precursors to earthquakes and storms. The ML pipelines are carefully tuned and validated against both held‑out data and independent observations, often achieving performance improvements over purely statistical methods.  

In sum, the recent geodesy literature presents a coherent, end‑to‑end framework that begins with raw satellite signals and culminates in actionable predictions or diagnostics. The integration of rigorous geodetic inversion with sophisticated machine‑learning inference continues to push the boundaries of what can be learned from the invisible, but highly informative, signals that travel between the Earth’s surface and its satellite constellations.