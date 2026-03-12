# Task - Customer Metrics

## Goal

Implement a function that returns customer-level metrics for orders within a date range.

## Function to implement

get_customer_metrics({ data, from, to, minTotalSpend })

## Inputs

- data: array of orders
- from: YYYY-MM-DD (inclusive)
- to: YYYY-MM-DD (inclusive)
- minTotalSpend (optional): number. Minimum total spend per customer.

## Domain Rules

- Date filter applies to orderDate (inclusive).
- Computed order amount = sum(quantity * unitPrice) across lineItems.
- Metrics are aggregated per customerId.
- Each customer result should include:
  - customerId
  - orderCount
  - totalSpend
  - avgOrderValue = totalSpend / orderCount
- If minTotalSpend is provided, include only customers with totalSpend >= minTotalSpend.
- Sort results by customerId ascending.

## Return format

{
  results: [
    {
      customerId: string,
      orderCount: number,
      totalSpend: number,
      avgOrderValue: number
    }
  ]
}
