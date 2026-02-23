"""Monte Carlo Option Pricing Lab

A professional quantitative finance library for option pricing using Monte Carlo simulations.

Main Components:
    - pricing: Core pricing engines for European, American, and exotic options
    - models: Stochastic models (GBM, jump-diffusion, volatility surfaces)
    - variance_reduction: Advanced techniques (antithetic, control variates, stratified sampling)
    - portfolio: Portfolio risk analysis (VaR, CVaR, stress testing)
    - data: Market data utilities and calibration
    - utils: Helper functions and metrics
"""

__version__ = "0.1.0"
__author__ = "Lorenzo Martínez Malvar"
__email__ = "lorenlorenloren@gmail.com"

from . import pricing
from . import models
from . import variance_reduction
from . import portfolio
from . import data
from . import utils

__all__ = [
    "pricing",
    "models",
    "variance_reduction",
    "portfolio",
    "data",
    "utils",
]
