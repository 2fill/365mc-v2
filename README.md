# 365mc multi-output ML CDSS

Multi-output machine learning prototype for predicting postoperative liposuction outcomes.  
Built as a Streamlit-based clinical decision support system (CDSS) using a chained Extra Trees regression model.

---

## Project Status

| Module | Description | Status | Current Result | Artifact |
|----|-------------|--------|----------------|----------|
| M-1 | Data preprocessing and analytic dataset construction | complete | De-identified train/test datasets prepared for multi-output regression modeling | `data/` |
| M-2 | Exploratory data analysis and feature review | complete | Body composition, surgical, and demographic variables reviewed for model development | `notebooks/02-eda.ipynb` |
| M-3 | Multi-output model development | complete | Chained Extra Trees model selected and exported for application inference | `notebooks/03-modeling.ipynb` |
| M-4 | Final chained Extra Trees model export | complete | Final model bundle created with trained estimator, scaler, feature columns, scaled columns, target names, and prediction order | `models/chained_et_final.pkl` |
| M-5 | Streamlit CDSS integration | prototype complete | Interactive application implemented for individualized postoperative outcome prediction | `app/page.py` |
| M-6 | Model interpretation outputs | complete | Correlation, feature selection, and SHAP-based interpretation figures generated | `reports/` |

---

## Repo Layout

```text
365mc-multioutput-cdss/
|-- app/                 Streamlit CDSS application
|   `-- page.py
|
|-- assets/              Static application assets and UI images
|
|-- data/                De-identified analytic datasets
|   |-- processed/        Final processed data and inverse-scaled test examples
|   |-- train_x.csv
|   |-- train_y.csv
|   |-- test_x.csv
|   `-- test_y.csv
|
|-- models/              Runtime model artifacts
|   |-- chained_et_final.pkl
|   `-- scaler_bundle.pkl
|
|-- notebooks/           Research and model development notebooks
|   |-- 02-eda.ipynb
|   |-- 03-modeling.ipynb
|   `-- 04-modeling-final-chain-et.ipynb
|
|-- reports/             Model interpretation and evaluation figures
|   |-- correlation_matrix.png
|   |-- feature_selection(L1).png
|   |-- shap_et_weight_step1.png
|   `-- shap_et_size_step2.png
|
|-- requirements.txt
`-- README.md
```

---

## Model Summary

The final model is a chained Extra Trees regression pipeline for multi-output postoperative outcome prediction.

The model bundle includes:

- trained chained Extra Trees estimator
- scaler object
- feature column names
- scaled column names
- target names
- prediction order

The chained structure allows one predicted postoperative target to inform the next prediction step, which is useful when postoperative outcomes are correlated.

---

## Input Variables

The application uses demographic, surgical, and body composition variables.

| Category | Variables |
|----------|-----------|
| Demographics | Sex, age |
| Anthropometrics | Height, weight, BMI, body size |
| Body composition | Total body water, body protein, body mineral, fat-free mass, skeletal muscle mass, body fat mass, waist-hip ratio |
| Surgical information | Liposuction site, liposuction type |

---

## Output Targets

The current CDSS prototype predicts:

| Target | Description |
|--------|-------------|
| Postoperative weight | Predicted postoperative body weight |
| Postoperative body size | Predicted postoperative body size measurement |

---

## Quick Start

### Installation

```bash
git clone https://github.com/syselina/365mc-multioutput-cdss.git
cd 365mc-multioutput-cdss
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app/page.py
```

---

## Reproducing the Workflow

### M-1 / M-2: EDA and preprocessing

```bash
jupyter notebook notebooks/02-eda.ipynb
```

This notebook contains exploratory data analysis, preprocessing checks, and feature review.

### M-3: Model development

```bash
jupyter notebook notebooks/03-modeling.ipynb
```

This notebook contains model comparison, evaluation, and interpretation workflow.

### M-4: Final model export

```bash
jupyter notebook notebooks/04-modeling-final-chain-et.ipynb
```

This notebook exports the final chained Extra Trees model bundle used by the Streamlit application.

---

## Application Workflow

1. User enters demographic information.
2. User enters liposuction-related information.
3. User enters body composition measurements.
4. Application preprocesses the input using the saved scaler and feature order.
5. Chained Extra Trees model generates multi-output predictions.
6. Predicted postoperative outcomes are displayed in the Streamlit interface.

---

## Evidence and Artifacts

| Evidence Type | Location |
|--------------|----------|
| Final model bundle | `models/chained_et_final.pkl` |
| Scaler bundle | `models/scaler_bundle.pkl` |
| EDA notebook | `notebooks/02-eda.ipynb` |
| Modeling notebook | `notebooks/03-modeling.ipynb` |
| Final model notebook | `notebooks/04-modeling-final-chain-et.ipynb` |
| Interpretation figures | `reports/` |
| Streamlit app | `app/page.py` |

---

## Data Notice

The datasets included in this repository are de-identified analytic datasets prepared for research and demonstration purposes.

No directly identifying patient information is intended to be included in this repository.

---

## Current Limitations

- This repository is a prototype implementation.
- The Streamlit application is intended for demonstration and research use.
- Model performance should be interpreted within the context of the available dataset and preprocessing pipeline.
- The application should not be used as a standalone clinical decision-making tool.

---

## Priority Next Steps

1. Validate the Streamlit application after project restructuring.
2. Confirm model loading path after moving `page.py` into `app/`.
3. Add example input/output screenshots to the README.
4. Add a short model performance summary table.
5. Consider separating public demo data from full analytic data if the repository becomes public-facing.

---

## Disclaimer

This application is a research prototype for multi-output postoperative outcome prediction after liposuction.  
It is not intended to replace professional clinical judgment, institutional protocols, or physician-led decision-making.