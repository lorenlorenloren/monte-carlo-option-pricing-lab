from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="monte-carlo-option-pricing-lab",
    version="0.1.0",
    author="Lorenzo Martínez Malvar",
    author_email="lorenlorenloren@gmail.com",
    description="Professional quantitative finance lab for option pricing using Monte Carlo simulations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lorenlorenloren/monte-carlo-option-pricing-lab",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Education",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "yfinance>=0.1.70",
        "matplotlib>=3.4.0",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov", "jupyter"],
        "gpu": ["jax>=0.2.0"],
    },
    include_package_data=True,
    zip_safe=False,
)
