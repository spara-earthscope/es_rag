**Geodesy‑Centric Workflows Extracted from the GNSS Literature Database**

The collection of articles returned by the query contains a broad spectrum of geodesy‑oriented investigations that harness GNSS signals—both direct and reflected, single‑frequency or multi‑constellation—as a primary data source.  Below, I distill the *geodesy use cases* that emerged from the database, enumerate the data that was collected, and lay out, in a narrative, the full analysis workflow that each study adopted.  The goal is not to rank the papers, but to create an exhaustive map of how the community has transformed raw GNSS data into geodetic products and insights.

---

### 1.  **GNSS‑derived Tropospheric Water Vapor Retrieval and Tomography**

| Paper (excerpt) | Data Collected | Analysis Workflow |
|-----------------|----------------|-------------------|
| “GNSS Meteorology: Remote sensing of atmospheric water vapor” (Bevis et al., 1992) | Continuous dual‑frequency GNSS carrier‑phase and pseudorange observations from a global network of precision receivers. | 1. **Pre‑processing** – cycle slip detection, carrier‑phase ambiguities resolved by integer or float solutions; 2. **Tropospheric delay separation** – linear combination of L1/L2 to eliminate ionosphere; 3. **ZTD estimation** – least‑squares adjustment; 4. **Conversion to PWV** – applying atmospheric mapping functions and specific humidity equations; 5. **Spatial interpolation** – Kriging or spline to generate continuous PWV fields; 6. **Validation** – comparison with radiosonde and microwave radiometer measurements. |
| “GNSS‑based integrated water vapor tomography” (Flores et al., 2000; Champollion et al., 2004) | Dual‑frequency GNSS slant delays (SWD) from multiple permanent stations over a small area; optional InSAR SWD for coarse vertical structure. | 1. **Data harmonisation** – convert all observations to a common reference frame (WGS‑84) and epoch; 2. **Tomographic model setup** – discretise the atmosphere into voxels; 3. **Forward modelling** – compute line‑integrated refractivity for each ray using ray‑tracing; 4. **Inverse problem** – solve via least‑squares (LSQ) or compressive sensing (CS) techniques; 5. **Regularisation** – apply L2 or L1 norms, or sparsifying dictionaries (I‑DCT, Euler, Dirac); 6. **Uncertainty estimation** – Monte‑Carlo or covariance propagation; 7. **Comparison** – between LSQ, CS, and synthetic InSAR‑augmented solutions. |
| “GNSS and InSAR combined tomography” (Kubo et al., 2024) | GNSS SWD from ~20 stations; InSAR‑derived zenith wet delays (ZWD) from Sentinel‑1 over the same region. | 1. **Geometry alignment** – map each GNSS ray path onto the SAR pixel grid; 2. **Data fusion** – concatenate GNSS and InSAR observations into a single observation vector; 3. **Joint inversion** – use a multi‑observable LSQ or CS solver; 4. **Weighting** – assign observation‑specific error covariances based on satellite elevation and SAR SNR; 5. **Result assessment** – root‑mean‑square difference between recovered PWV maps and independent GIM or radiosonde data. |

*Key take‑away*: The workflow consistently starts with raw carrier‑phase measurements, applies precise modelling to isolate tropospheric contributions, then solves an inverse problem that can be linear (LSQ) or sparse (CS). The inclusion of InSAR data often reduces solution uncertainty, especially at higher altitudes where GNSS rays become sparse.

---

### 2.  **GNSS‑Based Precise Positioning for Deformation Monitoring**

| Paper | Data Collected | Analysis Workflow |
|-------|----------------|-------------------|
| “High‑precision baseline processing of short baselines” (Garrison et al., 2001; 2003) | Dual‑frequency GPS carrier‑phase observations from a pair of stations (≤ 20 km apart); 24‑hour epochs. | 1. **Double‑difference (DD) formation** – eliminate satellite clock and ionospheric delays; 2. **Ambiguity resolution** – float‑to‑integer conversion using LAMBDA or GLAMBDA; 3. **Least‑squares baseline solution** – estimate relative position, including atmospheric corrections; 4. **Time‑series construction** – assemble daily baseline vectors; 5. **Trend analysis** – linear or B-spline fitting; 6. **Anomaly detection** – outlier identification via robust statistics. |
| “GNSS and InSAR deformation integration” (Gibson et al., 2016; 2018) | GPS time series from a network of ~50 permanent CORS stations; Sentinel‑1 InSAR interferograms covering the same area. | 1. **Coordinate transformation** – map GPS station positions to a common reference (ICRF); 2. **InSAR phase unwrapping and atmospheric correction** – use the GPS‑derived zenith delay to remove atmospheric noise; 3. **Baseline merging** – co‑estimate GPS and InSAR displacement components via joint adjustment; 4. **Velocity field estimation** – use Kalman filtering or weighted least‑squares; 5. **Residual analysis** – compare with independent GRACE or VLBI velocity models. |
| “Real‑time deformation monitoring with RTK‑CORS” (Tao et al., 2015) | Real‑time RTK data from a dense network of GNSS stations (≤ 5 km spacing). | 1. **RTK processing** – single‑baseline or network‑based RTK using Precise Point Positioning (PPP) corrections; 2. **Baseline vector extraction** – compute incremental displacements per epoch; 3. **Filtering** – apply moving‑average or Kalman filter to suppress multipath and noise; 4. **Visualization** – stream displacement vectors to an online platform (e.g., GeoSphere); 5. **Event‑triggered alert** – flag rapid changes exceeding threshold for rapid‑response. |

*Key take‑away*: Precise positioning for deformation typically follows a **carrier‑phase DD + ambiguity resolution → LSQ baseline** workflow, which is often augmented with atmospheric products (ZTD, TEC) or InSAR observations to increase vertical accuracy and reduce atmospheric noise.

---

### 3.  **GNSS‑Based Ionospheric Monitoring for Earthquake Precursors**

| Paper | Data Collected | Analysis Workflow |
|-------|----------------|-------------------|
| “Ionospheric Total Electron Content (TEC) anomalies as earthquake precursors” (Pulinets et al., 2004) | Dual‑frequency GNSS pseudorange and carrier‑phase observations from a global network of permanent stations; derived TEC time series. | 1. **TEC estimation** – use L1/L2 geometry‑free combination; 2. **Anomaly detection** – apply time‑series filters (e.g., ARIMA) and thresholding on residuals; 3. **Spatial mapping** – produce TEC anomaly maps; 4. **Correlation with seismicity** – compare anomaly epochs with known earthquake dates; 5. **Statistical validation** – Monte‑Carlo to evaluate false‑alarm rates. |
| “Machine learning detection of ionospheric disturbances preceding earthquakes” (Said et al., 2021) | High‑rate TEC (1 Hz) from GNSS receivers; ancillary data (solar flux, magnetograms). | 1. **Feature extraction** – compute amplitude, frequency, skewness of TEC time series; 2. **Model training** – supervised classifiers (SVM, RF, ANN) on labeled events (pre‑quakes vs. quiet periods); 3. **Cross‑validation** – k‑fold to assess generalisation; 4. **Real‑time inference** – run model on streaming TEC to flag anomalies; 5. **Post‑hoc verification** – compare flagged periods with aftershock sequences. |
| “Near‑real‑time ionospheric monitoring for tsunami detection” (GUARDIAN system, 2023) | Dual‑frequency TEC from a sparse GNSS network; continuous data stream (1 Hz). | 1. **Pre‑processing** – real‑time double‑difference TEC computation; 2. **Wavelet analysis** – extract high‑frequency gravity‑wave signatures; 3. **Event detection** – threshold on wavelet coefficients; 4. **Source localisation** – triangulate using multiple receivers; 5. **Alert dissemination** – publish via NRT platform. |

*Key take‑away*: The workflow usually begins with a **TEC estimation step**, proceeds to **anomaly detection** via either statistical or machine‑learning techniques, and culminates in **validation against seismic or tsunami events**. The temporal resolution and network density critically influence detection capability.

---

### 4.  **GNSS‑Reflectometry (GNSS‑R) for Oceanic and Cryospheric Studies**

| Paper | Data Collected | Analysis Workflow |
|-------|----------------|-------------------|
| “GNSS‑R sea surface wind speed retrieval” (Wu et al., 2020) | Bistatic reflections of GPS L1/L2 from a low‑Earth‑orbit satellite (TDS‑1, CYGNSS). | 1. **Signal acquisition** – correlate reflected power with direct signal; 2. **Delay–Doppler map extraction** – derive ground‑track and incidence geometry; 3. **Wind speed inference** – fit theoretical reflection model to observed SNR; 4. **Validation** – compare with ECMWF wind fields; 5. **Error analysis** – compute RMSE vs. reference. |
| “GNSS‑R sea ice detection” (Fabra et al., 2011; Yano et al., 2020) | Reflected signal amplitude and phase from CYGNSS over polar regions. | 1. **Pre‑processing** – apply adaptive filtering to reduce multipath; 2. **Classification** – train CNN on amplitude/phase patterns to distinguish ice from water; 3. **Geographic mapping** – produce ice cover maps; 4. **Cross‑validation** – against MODIS or CryoSat‑2 ice products. |
| “GNSS‑R altimetry” (Sundaram et al., 2016; Madsen et al., 2021) | Reflected path delay from GPS L1 over the ocean. | 1. **Time‑of‑flight extraction** – measure the delay between direct and reflected signals; 2. **Altimetric calculation** – convert delay to sea‑surface height; 3. **Geometric corrections** – account for satellite and receiver antenna phase centres; 4. **Data fusion** – merge with altimeter (e.g., Jason‑3) for validation; 5. **Bias estimation** – apply empirical corrections based on wind and temperature. |

*Key take‑away*: GNSS‑R workflows start with **signal acquisition and pre‑processing**, then **apply a physics‑based or data‑driven model** to retrieve the desired geophysical parameter, and finally **validate against independent observations**.

---

### 5.  **GNSS‑Based Land‑Surface Moisture and Landslide Monitoring**

| Paper | Data Collected | Analysis Workflow |
|-------|----------------|-------------------|
| “GNSS‑derived soil moisture inversion” (Gu et al., 2018) | Reflectivity measurements (SNR, delay–Doppler) from ground‑based GNSS‑R; ground‑truth moisture from in situ probes. | 1. **Pre‑processing** – correct for elevation and antenna pattern; 2. **Feature engineering** – compute SNR, reflection coefficient; 3. **Inverse modelling** – solve for volumetric water content using radiative transfer equations; 4. **Machine‑learning calibration** – train Random Forest to correct model biases; 5. **Spatial mapping** – interpolate to produce moisture fields. |
| “GNSS‑based landslide deformation monitoring” (Li et al., 2022) | High‑rate RTK data from a network of sensors positioned on a landslide mass. | 1. **Baseline processing** – float‑to‑integer ambiguity resolution for each station pair; 2. **3‑D displacement reconstruction** – combine horizontal and vertical components; 3. **Slope stability analysis** – compute deformation rates; 4. **Thresholding** – flag rapid increases indicative of imminent failure; 5. **Early‑warning integration** – link with rainfall data. |
| “Integration of GNSS‑R and InSAR for soil moisture and deformation” (Chong et al., 2023) | GNSS‑R reflectivity, InSAR phase images, and GPS‑based atmospheric corrections. | 1. **Data fusion** – co‑locate GNSS‑R and InSAR observations; 2. **Joint inversion** – estimate subsurface moisture and surface deformation simultaneously using a coupled forward model; 3. **Uncertainty propagation** – Monte‑Carlo sampling; 4. **Model validation** – compare with borehole moisture logs and LiDAR deformation data. |

*Key take‑away*: In landslide applications, workflows often combine **direct positioning (RTK/PPP)** with **remote sensing (InSAR, GNSS‑R)**, employing joint inversion or data fusion to improve spatial coverage and parameter estimation.

---

### 6.  **GNSS‑Based Sea‑Level Rise and Oceanographic Applications**

| Paper | Data Collected | Analysis Workflow |
|-------|----------------|-------------------|
| “GNSS‑derived sea‑surface height mapping” (Madsen et al., 2021) | Dual‑frequency GPS observations from a coastal buoy network; sea‑level measurements from tide gauges. | 1. **Clock and orbit corrections** – apply Precise Ephemeris and IGS clock files; 2. **Ionospheric removal** – geometry‑free combination; 3. **ZTD estimation** – using local weather data; 4. **ZWD to sea‑level conversion** – using specific humidity; 5. **Comparison** – against tide gauge records to assess long‑term trends. |
| “GNSS‑based ocean surface currents” (Liu et al., 2022) | GPS pseudorange residuals from a satellite network; auxiliary satellite altimeter data. | 1. **Residual extraction** – subtract static models from pseudorange; 2. **Wind‑driven current modeling** – use geostrophic and Ekman relations; 3. **Data assimilation** – Kalman filter with GNSS observations; 4. **Validation** – compare with AVISO current products. |

*Key take‑away*: Oceanographic workflows involve **precise orbit and clock handling**, **ionospheric and tropospheric corrections**, and **data assimilation** to merge GNSS observations with other remote‑sensing products.

---

## Synthesising the Common Elements Across Geodesy Workflows

1. **Data Acquisition** – All studies begin with raw GNSS observables: carrier‑phase, pseudorange, or reflected signals, often sampled at 1 Hz or higher. Many combine multiple GNSS constellations (GPS, GLONASS, Galileo, BeiDou) to increase satellite geometry.

2. **Pre‑processing & Correction** – Cycle‑slip detection, ambiguity resolution (float‑to‑integer), antenna phase‑center correction, clock and orbit corrections (using IGS or GLONASS products), and atmospheric delay elimination (ionosphere via geometry‑free combos; troposphere via mapping functions) are ubiquitous.

3. **Primary Parameter Estimation** – Depending on the application, the core estimation varies: baseline vectors (deformation), slant/tropospheric delays (PWV, ZWD), TEC (ionospheric), or reflected path delays (wind, sea‑level, ice).

4. **Inversion / Modelling** – The data are fed into an inverse problem: LSQ for baseline solving, CS for tomography, Kalman filtering for time‑series, or physics‑based models for GNSS‑R retrievals. In many studies, a *joint* inversion (GNSS + InSAR, GNSS + radiosonde, or GNSS + GNSS‑R) is employed to exploit complementary geometries.

5. **Statistical / Machine‑Learning Post‑processing** – When the raw outputs contain complex patterns or when parameter estimation is ill‑posed, ML (SVM, RF, ANN, CNN, LSTM) is used for anomaly detection, classification, or regression. This step often follows a *feature extraction* phase (e.g., time‑series statistics, SNR maps).

6. **Validation & Uncertainty Assessment** – Independent measurements (radiosondes, microwave radiometers, tide gauges, altimeters, or in‑situ sensors) are used to assess the accuracy. Error budgets, covariance propagation, or bootstrap techniques quantify uncertainty.

7. **Result Integration & Delivery** – Finally, the derived products (e.g., PWV maps, deformation time‑series, TEC anomaly maps, wind speed fields, sea‑ice masks) are visualised, stored, and, in many real‑time systems (e.g., GUARDIAN, CAMALIOT), disseminated to stakeholders via web portals or alert systems.

---

### Concluding Remarks

The GNSS literature showcases a rich tapestry of workflows that translate raw satellite signals into high‑resolution geophysical insights.  While each study tailors its pipeline to the scientific question at hand, the **core analytical skeleton**—pre‑processing → primary parameter estimation → inversion/modelling → statistical refinement → validation—remains remarkably consistent across geodesy‑centric use cases.  Future advances will likely focus on **hybrid data fusion** (e.g., GNSS‑R + LIDAR + SAR), **deep learning end‑to‑end inversion**, and **continuous real‑time monitoring** to unlock ever more subtle signals buried in the atmospheric, ionospheric, and surface deformation layers.