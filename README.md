<div align="center">

# 🇪🇬 Egypt Real Estate Market Analyzer

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

*A comprehensive end-to-end data pipeline and analysis project focused on uncovering investment opportunities and pricing trends in the Egyptian property market.*

</div>

---

## 📑 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features & Insights](#-key-features--insights)
- [Project Architecture](#-project-architecture)
- [Dataset Details](#-dataset-details)
- [Getting Started](#-getting-started)
- [Team Members](#-team-members)

---

## 📌 Project Overview
The **Egypt Real Estate Analyzer** is designed to process, clean, and analyze thousands of real estate listings across Egypt (focusing on major hubs like Cairo and New Cairo City). By evaluating property features, geographic locations, and pricing metrics, this tool provides actionable intelligence for:
- 🏢 **Real Estate Investors:** Identifying undervalued properties.
- 📈 **Market Analysts:** Understanding the key drivers of property prices.
- 🏠 **Home Buyers:** Comparing fair market values using metrics like `price_per_sqft`.

---

## 💡 Key Features & Insights
* **Price Per Square Foot Analysis:** Normalized valuation metric to compare properties of vastly different sizes.
* **Undervaluation Scoring:** Algorithmic identification of properties listed below market average for their specific district and feature set.
* **Geospatial Trends:** Analyzing how proximity to landmarks or specific compounds affects property value.
* **Feature Correlation:** Determining exactly how much a pool, garden, or extra bedroom adds to the listing price.

---

## 🏗️ Project Architecture
The analysis is structured sequentially using Jupyter Notebooks to maintain a clean ETL (Extract, Transform, Load) pipeline:

| Notebook | Purpose | Description |
| :--- | :--- | :--- |
| `01_extraction.ipynb` | **Ingestion** | Initial data gathering, reading raw CSVs, and initial structural checks. |
| `02_cleaning.ipynb` | **Transformation** | Handling missing values, standardizing strings (e.g., city names), and correcting data types. |
| `03_eda.ipynb` | **Exploration** | Generating distributions, geographic maps, and initial visual insights. |
| `04_statistical_analysis.ipynb` | **Analysis** | Correlation matrices, hypothesis testing, and determining statistical significance of features. |
| `05_final_load_prep.ipynb` | **Loading** | Final feature engineering (e.g., generating `undervaluation_score`) and exporting the dashboard-ready dataset. |

---

## 📊 Dataset Details
The finalized dataset (`data/processed/final_dataset.csv`) is highly enriched, containing variables such as:
- **📍 Location:** City, District, Subdistrict, Latitude, Longitude.
- **🏡 Property Specs:** Property Type (Villa, Apartment, Duplex), Bedrooms, Bathrooms, Area (sqm), Furnishing Status.
- **💰 Financials:** Price (EGP), Price per Sqft, Undervaluation Score.
- **✨ Amenities:** Extracted features like pools, gardens, security, and views.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have `Python 3.12+` and `git` installed on your machine.

### Installation & Execution
1. **Clone the repository:**
   ```bash
   git clone https://github.com/viveeeeek13/SectionE_G-5_Egypt-RealEstateAnalyzer.git
   cd SectionE_G-5_Egypt-RealEstateAnalyzer
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the environment:**
   ```bash
   jupyter notebook
   ```
   *Navigate to the `notebooks/` directory and execute the files sequentially from `01` to `05`.*

---

## 👥 Team Members
Developed and maintained by:
* **Vivek Kumar Raj**
* **Pratik Agade**
* **Vedant Satbhai**

<div align="center">
  <i>If you found this project helpful, please consider giving it a ⭐!</i>
</div>
