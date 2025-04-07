# Portfolio Optimization Project

## Project Description

This project explores various methods of portfolio optimization using quantitative finance techniques. The goal is to build an efficient investment portfolio by balancing risk and return through the following methods:

- **Mean-Variance Optimization (Markowitz Model)**: Minimizing risk at a given return level.
- **Sharpe Ratio Optimization**: Maximizing the risk-adjusted returns of the portfolio.
- **Black-Litterman Model** *(Optional)*: Incorporating investor views into the optimization process.
- **Machine Learning-based Return Predictions** *(Optional)*: Enhancing portfolio allocation using predictive modeling.

## Quickstart Instructions

### Setup
1. Clone this repository and navigate to the project directory:
```bash
git clone <repository-url>
cd PortfolioOptimization_V0.1
```

2. Set up a Python virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Running the Notebooks
- Launch Jupyter Notebook:
```bash
jupyter notebook
```

- Navigate to the `notebooks/` directory and run the notebooks in the following suggested order:
  1. `01_data_collection.ipynb`
  2. `02_exploratory_analysis.ipynb`
  3. `03_mean_variance_optimization.ipynb`
  4. `04_sharpe_ratio_optimization.ipynb`
  5. *(Optional)* `05_black_litterman.ipynb`
  6. *(Optional)* `06_ml_return_predictions.ipynb`

## Results Summary

The results and key insights from each optimization method are documented clearly in each notebook. For detailed analysis, visualizations, and discussions, explore the notebooks located in the `notebooks/` directory:

- **Mean-Variance Optimization:** [03_mean_variance_optimization.ipynb](notebooks/03_mean_variance_optimization.ipynb)
- **Sharpe Ratio Optimization:** [04_sharpe_ratio_optimization.ipynb](notebooks/04_sharpe_ratio_optimization.ipynb)
- **Black-Litterman Model:** *(Optional)* [05_black_litterman.ipynb](notebooks/05_black_litterman.ipynb)
- **ML-based Predictions:** *(Optional)* [06_ml_return_predictions.ipynb](notebooks/06_ml_return_predictions.ipynb)

### Directory Structure
```
PortfolioOptimization_V0.1/
├── data/                # Raw and processed datasets
├── notebooks/           # Jupyter notebooks with analysis
├── scripts/             # Supporting Python scripts
├── outputs/             # Generated results and visualizations
├── requirements.txt     # Python package requirements
└── README.md            # Project documentation
```

