# PyCurrency
A Python package to convert currency or get exchange rate.

[![PyPI version](https://badge.fury.io/py/currency-calculator.svg)](https://badge.fury.io/py/currency-calculator)

## Usage

### Installation

```bash
pip install currency-calculator
```

### Get exchange rate

```python
>>> import currency_calculator
>>> currency_calculator.get("USD", "CNY")
6.5772
>>> currency_calculator.get("USDCNY")
6.5772
```

### Convert currency

```python
>>> import currency_calculator
>>> currency_calculator.convert("1.0USD", "CNY")
6.5772
```