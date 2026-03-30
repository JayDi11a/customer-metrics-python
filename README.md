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

**Install uv** (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh  # Mac/Linux
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows
```

**Clone and run tests**:
```bash
git clone https://github.com/snevans7-commits/customer-metrics-python.git
cd customer-metrics-python
uv run pytest
```
