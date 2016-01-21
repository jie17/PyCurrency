# PyCurrency
A Python package to convert currency or get exchange rate.

## Usage

### Get exchange rate

```
>>> PyCurrency.get("USD", "CNY")
6.5772
>>> PyCurrency.get("USDCNY")
6.5772
```

### Convert currency

```
>>> PyCurrency.convert("1.0USD", "CNY")
6.5772
```