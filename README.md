# Customer Metrics (Python)

This project implements a function that calculates customer-level metrics from order data.

## Function

```python
get_customer_metrics(data, from_, to, min_total_spend=None)
```

### Parameters

- data: list of order objects
- from_: start date (YYYY-MM-DD inclusive)
- to: end date (YYYY-MM-DD inclusive)
- min_total_spend: optional minimum total spend per customer

### Rules

- Date filtering applies to `orderDate`
- Order amount = sum(quantity * unitPrice)
- Metrics are calculated per customer
- Each customer result should include:
  - customerId
  - orderCount
  - totalSpend
  - avgOrderValue
- If `min_total_spend` is provided, only include customers whose totalSpend is at least that value
- Results must be sorted by customerId ascending

## Setup

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run tests

```bash
pytest
```
