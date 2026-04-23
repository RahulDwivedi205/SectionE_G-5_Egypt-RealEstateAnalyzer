# Egypt Real Estate Market Analyzer 🇪🇬 🏢

## 📌 Project Overview
The **Egypt Real Estate Analyzer** is a comprehensive end-to-end data pipeline and analysis project focused on the Egyptian property market. It extracts, cleans, and analyzes real estate listings to identify undervalued properties, market trends, and key drivers of property prices in Egypt (e.g., Cairo, New Cairo City, etc.). 

This project aims to provide actionable insights for real estate investors, buyers, and market analysts by evaluating property features, locations, and pricing metrics like `price_per_sqft` and `undervaluation_score`.

## 🗂️ Project Structure
The analysis is broken down into a modular Jupyter Notebook pipeline:
- **`01_extraction.ipynb`**: Data ingestion and raw data compilation.
- **`02_cleaning.ipynb`**: Handling missing values, standardizing formats, and data type conversions.
- **`03_eda.ipynb`**: Exploratory Data Analysis (EDA) uncovering geographical pricing trends and property feature distributions.
- **`04_statistical_analysis.ipynb`**: Correlation mapping, statistical testing, and identifying significant price drivers (e.g., area, bedrooms, amenities).
- **`05_final_load_prep.ipynb`**: Final feature engineering (like `price_per_sqft`) and formatting the dataset for dashboard consumption.

## 📊 Dataset Features
The processed dataset (`data/processed/final_dataset.csv`) contains rich property information including:
- **Location details:** City, District, Coordinates (Lat/Lon)
- **Property attributes:** Property Type, Bedrooms, Bathrooms, Area (sqm), Furnishing status
- **Financial metrics:** Price in EGP, Price per sqft, Undervaluation score
- **Additional features:** Amenities, Agent/Broker details, Listing status

## 🛠️ Tech Stack & Libraries
- **Python 3.12+**
- **Data Manipulation:** `pandas`, `numpy`
- **Statistical Analysis:** `scipy`
- **Data Visualization:** `matplotlib`, `seaborn`
- **Environment:** Jupyter Notebooks

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/viveeeeek13/SectionE_G-5_Egypt-RealEstateAnalyzer.git
   cd SectionE_G-5_Egypt-RealEstateAnalyzer
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis:**
   Launch Jupyter Notebook and run the notebooks in sequence from `01` to `05`:
   ```bash
   jupyter notebook
   ```

## 👥 Team Members
- Vivek Kumar Raj
