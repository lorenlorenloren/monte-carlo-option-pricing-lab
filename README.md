# Monte Carlo Option Pricing Lab

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A professional-grade quantitative finance library for option pricing using Monte Carlo simulations. Built for financial engineers, quantitative analysts, and students in computational finance. Features advanced variance reduction, American option pricing via Longstaff-Schwartz LSM, portfolio risk analysis, and real market data integration.

## 🎉 Features

### Core Pricing Engine
- **Geometric Brownian Motion (GBM)** simulation with Cholesky decomposition for correlated assets
- **European & American Options** (calls and puts)
- **Exotic Derivatives**: Asian options, barrier options, basket options
- **Multi-asset derivatives** with correlation modeling

### Advanced Techniques
- **Variance Reduction Methods**:
  - Antithetic variates
  - Control variates (using Black-Scholes as comparator)
  - Stratified sampling
- **American Option Pricing**: Longstaff-Schwartz Least-Squares Monte Carlo (LSM)
- **Greek Estimation**: Delta, Gamma, Vega, Theta via bump-and-revalue

### Portfolio Analytics
- Value-at-Risk (VaR) and Expected Shortfall (CVaR) under Monte Carlo
- Portfolio P&L distribution and stress testing
- Scenario analysis with volatility and jump shocks

### Market Integration
- Real data fetching via `yfinance` (Yahoo Finance)
- Historical volatility calibration
- Term structure support (flat and piecewise-constant rates)
- Comparison tools: Monte Carlo vs Black-Scholes vs Binomial Tree

## 📚 Documentation & Examples

Comprehensive Jupyter notebooks and markdown guides:

- `docs/THEORY.md` - Mathematical foundations and variance reduction theory
- `notebooks/01_vanilla_options.ipynb` - European option pricing basics
- `notebooks/02_variance_reduction.ipynb` - Antithetic & control variates comparison
- `notebooks/03_american_options.ipynb` - LSM implementation and early-exercise premium
- `notebooks/04_multi_asset.ipynb` - Basket and correlated assets
- `notebooks/05_greeks.ipynb` - Sensitivity analysis and Greeks
- `notebooks/06_portfolio_var.ipynb` - Portfolio risk metrics
- `notebooks/07_case_study_ewz.ipynb` - Real market example: EWZ 3-month call

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/lorenlorenloren/monte-carlo-option-pricing-lab.git
cd monte-carlo-option-pricing-lab
pip install -r requirements.txt
```

### Basic European Call Pricing

```python
from src.pricing.european import EuropeanCall
import numpy as np

# Parameters
S0 = 100      # Current stock price
K = 105       # Strike price
T = 0.5       # Time to maturity (years)
r = 0.05      # Risk-free rate
sigma = 0.2   # Volatility
paths = 100000

# Pricing
call = EuropeanCall(S0, K, T, r, sigma)
price, std_error = call.price_mc(paths=paths)
bs_price = call.price_bs()  # Benchmark

print(f"MC Price: {price:.4f} ± {std_error:.4f}")
print(f"BS Price: {bs_price:.4f}")
print(f"Error: {abs(price - bs_price):.4f}")
```

### American Put with LSM

```python
from src.pricing.american import AmericanPut

# LSM with polynomial basis functions
put = AmericanPut(S0=100, K=105, T=1.0, r=0.05, sigma=0.2)
price, ci = put.price_lsm(paths=10000, degree=3)

print(f"American Put Price: {price:.4f} (95% CI: [{ci[0]:.4f}, {ci[1]:.4f}])")
```

### Portfolio VaR

```python
from src.portfolio import Portfolio
import yfinance as yf

# Fetch real data
tickers = ['PETR4.SA', 'VALE3.SA']  # Petrobras, Vale (Brazil)
prices = yf.download(tickers, period='1y')

# Portfolio with options
portfolio = Portfolio(
    underlying_prices=prices['Adj Close'].iloc[-1],
    positions={'PETR4.SA': 100, 'VALE3.SA': 50},
    options=[
        {'type': 'call', 'ticker': 'PETR4.SA', 'K': 25, 'T': 0.25}
    ]
)

var_95, cvar_95 = portfolio.calculate_var_mc(paths=10000, confidence=0.95)
print(f"VaR (95%): ${var_95:.2f}")
print(f"CVaR (95%): ${cvar_95:.2f}")
```

## 📄 Project Structure

```
.
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
├── LICENSE                   # MIT License
├── .gitignore                # Python .gitignore
├── src/
│   ├── __init__.py
│   ├── pricing/              # Core pricing engines
│   │   ├── european.py     # European options (Call, Put)
│   │   ├── american.py     # American options with LSM
│   │   ├── exotic.py       # Asian, Barrier, Basket options
│   │   ├── engine.py       # Base MC simulation engine
│   │   └── greeks.py      # Greeks calculation
│   ├── models/               # Stochastic models
│   │   ├── gbm.py         # Geometric Brownian Motion
│   │   ├── jump_diffusion.py  # Jump-diffusion models
│   │   └── volatility.py  # Vol surfaces & calibration
│   ├── variance_reduction/   # Advanced techniques
│   │   ├── antithetic.py
│   │   ├── control.py
│   │   └── stratified.py
│   ├── portfolio/            # Portfolio analytics
│   │   ├── portfolio.py
│   │   ├── risk.py         # VaR, CVaR, stress tests
│   │   └── scenarios.py
│   ├-- data/                 # Market data utilities
│   │   ├── market.py
│   │   └── calibration.py
│   └-- utils/                # Helpers
│       ├── math_utils.py
│       └__ metrics.py
├── notebooks/                # Jupyter tutorials & examples
│   ├── 01_vanilla_options.ipynb
│   ├── 02_variance_reduction.ipynb
│   ├── 03_american_options.ipynb
│   ├── 04_multi_asset.ipynb
│   ├── 05_greeks.ipynb
│   ├── 06_portfolio_var.ipynb
│   └── 07_case_study_ewz.ipynb
├── tests/                    # Unit tests
│   ├── test_pricing.py
│   ├── test_variance_reduction.py
│   └── test_portfolio.py
├── docs/                     # Documentation
│   ├── THEORY.md             # Mathematical background
│   ├── API.md                # API reference
│   └── BENCHMARK.md          # Performance & accuracy benchmarks
```

## 📚 Academic References

1. **Longstaff & Schwartz (2001)** - "Valuing American Options by Simulation: A Simple Least-Squares Approach"
   - *The Review of Financial Studies*, 14(1), 113-147
   - Foundational LSM paper for American option pricing

2. **Glasserman (2003)** - *Monte Carlo Methods in Financial Engineering*
   - Comprehensive reference for simulation techniques and variance reduction

3. **Black & Scholes (1973)** - "The Pricing of Options and Corporate Liabilities"
   - *The Journal of Political Economy*, 81(3), 637-654
   - Benchmark for European option pricing

4. **Broadie & Glasserman (1996)** - "Estimating Security Price Derivatives Using Simulation"
   - Greeks estimation via finite differences in Monte Carlo

## 🤪 Requirements

- Python 3.8+
- NumPy >= 1.19
- SciPy >= 1.5
- Pandas >= 1.1
- Matplotlib >= 3.0
- yfinance >= 0.1.70
- Jupyter >= 1.0 (for notebooks)

Install all with:

```bash
pip install -r requirements.txt
```

## 👨‍🔬 Testing

Run unit tests to verify accuracy:

```bash
python -m pytest tests/ -v
```

Tests include:
- **Convergence tests**: MC prices converge to Black-Scholes within tolerance
- **Variance reduction efficacy**: Antithetic variates reduce error by ~50%
- **LSM validation**: American put prices > European put prices

## 🎨 Use Cases

### Academic
- Computational finance coursework (Insper, UC3M, international programs)
- Monte Carlo simulation assignments
- Derivative pricing projects

### Professional
- Quantitative analyst interview preparation
- Risk management framework prototyping
- Volatility and correlation analysis
- Portfolio optimization testing

### Research
- Variance reduction technique comparison
- Exotic option pricing validation
- Model calibration studies
- Numerical stability analysis

## 😘 Contributing

Contributions are welcome! Areas for expansion:

- Stochastic volatility models (Heston, SABR)
- Jump-diffusion processes
- FD/PDE solvers for comparison
- GPU acceleration via CuPy/JAX
- Real-time market data feeds

Please open an issue to discuss before submitting a PR.

## 📄 License

MIT License - See [LICENSE](LICENSE) for details. Free for academic and commercial use.

## 📋 Author

**Lorenzo Martínez Malvar**  
Economics Undergraduate | Quantitative Finance Specialist  
Universidad Carlos III de Madrid | Insper  

- GitHub: [@lorenlorenloren](https://github.com/lorenlorenloren)
- LinkedIn: [Lorenzo Martínez Malvar](https://linkedin.com/in/lorenlorenloren)

## 🗣 Acknowledgments

- Inspired by industrial quant frameworks and academic research
- Built with NumPy, SciPy, and the Python data science ecosystem
- References to Glasserman, Longstaff-Schwartz, and classical option pricing theory

---

**Star ⭐ this repo if you find it useful!**  
Fork it and build your own quantitative finance tools.
