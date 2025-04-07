# Portfolio Optimization Project

## Project Description

This project explores various methods of portfolio optimization using quantitative finance techniques. The goal is to build an efficient investment portfolio by balancing risk and return through the following methods:

- **Mean-Variance Optimization (Markowitz Model)**: Minimizing risk at a given return level.
- **Sharpe Ratio Optimization**: Maximizing the risk-adjusted returns of the portfolio.
- **Black-Litterman (High-Growth) Model** : Incorporating investor views into the optimization process.


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
  5. `05_black_litterman.ipynb`

### Strategy Dashboard

- Run the Dash app to explore strategies interactively:

- python `app.py`
- Visit `http://127.0.0.1:8050` in your browser to:
- Compare portfolio growth (Max Sharpe, High Growth, DCA)
- View allocation pie charts
- See forecast overlays

## Results Summary

The results and key insights from each optimization method are documented clearly in each notebook. For detailed analysis, visualizations, and discussions, explore the notebooks located in the `notebooks/` directory:

- **Mean-Variance Optimization:** [03_mean_variance_optimization.ipynb](notebooks/03_mean_variance_optimization.ipynb)
- **Sharpe Ratio Optimization:** [04_sharpe_ratio_optimization.ipynb](notebooks/04_sharpe_ratio_optimization.ipynb)
- **Black-Litterman Model:** [05_black_litterman.ipynb](notebooks/05_high_growth_portfolio.ipynb)

