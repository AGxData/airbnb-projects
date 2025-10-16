# Airbnb Data Analysis Project

## Overview
This project analyzes Airbnb listings data to uncover insights, trends, and predictive patterns. The workflow includes downloading and combining monthly CSVs, feature engineering, exploratory data analysis, clustering, and predictive modeling with CatBoost. The goal is to understand factors affecting pricing, understanding the impact of listing microclusters, and providing a model able to assign prices to new listings, using model predictions as benchmarks.

## Project Notebooks

1. **pt1_data_loading**  
   - **Purpose:** Downloaded and combined monthly Airbnb CSVs from Inside Airbnb. A separate Python file was used to download the data from the website. The script will unlikely work in the future as listing data gets archived regularly, but the datasets can be found in this repo.
   - **Tools & Methods:** `requests`, `pandas`, `polars`, `duckdb` for data loading, schema enforcement, data type conversions, and merging.  

2. **pt2_feature_engineering**  
   - **Purpose:** Prepared features for modeling.  
   - **Tools & Methods:** Pandas used for one-hot encoding categorical features and general preprocessing.  

3. **pt3_visualizations**  
   - **Purpose:** Exploratory data analysis (EDA) and visualizations.  
   - **Tools & Methods:** Basic visualizations to understand distributions, correlations, and analyzing the target variable.

4. **pt4_catboost**  
   - **Purpose:** Fit a CatBoost model on listing data.  
   - **Tools & Methods:**  
     - Cleaned neighborhood data by mapping lat/lon shapes from a GeoJSON file to dataset coordinates.  
     - Used CatBoost pooling for high-cardinality categorical features.  
     - Hyperparameter tuning via Optuna.  

5. **pt5_clustering**  
   - **Purpose:** Created density-based microclusters of Airbnb listings.  
   - **Tools & Methods:**  
     - HDBSCAN clustering with training sets per borough in order to avoid cross-borough clusters and prevent boroughs with few listings to be considered as noise.
     - Euclidean distance for all boroughs except Manhattan (Manhattan distance used).  
     - Only lat/lon used as features.
     - Training sets were used, and the "test" portion of the data assigned cluster labels with approximations learned from the training data in order to prevent data leakage. Cluster labels were then assigned back to the original dataset.

6. **pt6_final_model**  
   - **Purpose:** Fit final CatBoost model with clustered features.  
   - **Tools & Methods:**  
     - 
     - Hyperparameter tuning with Optuna.  
     - Model evaluation with SHAP and Yellowbrick for interpretability and performance insights.  

## Key Insights
- Seasonality had low feature importance in the final model, suggesting that other factors play a more significant role in pricing.
- Location features, the minimum nights available were among the most important predictors of prices in the model.
- Amenities were far too sparse and the amenities listed were even ridiculous (First-Aid Kit, Fire Extinguisher, Smoke Detector, - Basic necessities!) Even after lemmization, unicode, and text standardization, there were still over 1500 "unique" and very loosely labeled amenities.
- The first model obtained a mean absolute error (MAE) of approximately $60 dollars, while the final model with cluster labels improved to an MAE of about $30.
- The model mostly struggled with very high-priced listings, as there were fewer data points for the model to learn from with prices above $1400 per night.

## Technologies Used
- **Programming Language:** Python
- **Development Tools:** Jupyter Notebooks, VSCode, Git, GitHub, Anaconda/Mamba
- **Data Storage & Wrangling:** DuckDB, NumPy, Pandas, GeoPandas, Polars
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn, CatBoost, HDBSCAN, Optuna, SHAP, Yellowbrick  