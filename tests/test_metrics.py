import json
from metrics import get_customer_metrics


with open("tests/fixtures.json") as f:
    data = json.load(f)


def by_customer(results):
    return {r["customerId"]: r for r in results}


def test_calculates_customer_metrics_within_inclusive_date_range():
    out = get_customer_metrics(
        data=data,
        from_="2026-01-10",
        to="2026-01-12"
    )

    assert out["results"] is not None
    assert [r["customerId"] for r in out["results"]] == [
        "cust_1",
        "cust_2",
        "cust_3"
    ]

    result_map = by_customer(out["results"])

    # cust_1: o1=30, o3=50 => orderCount=2 totalSpend=80 avgOrderValue=40
    assert result_map["cust_1"] == {
        "customerId": "cust_1",
        "orderCount": 2,
        "totalSpend": 80,
        "avgOrderValue": 40
    }

    # cust_2: o2=20, o5=20 => totalSpend=40 avgOrderValue=20
    assert result_map["cust_2"] == {
        "customerId": "cust_2",
        "orderCount": 2,
        "totalSpend": 40,
        "avgOrderValue": 20
    }

    # cust_3: o4=30
    assert result_map["cust_3"] == {
        "customerId": "cust_3",
        "orderCount": 1,
        "totalSpend": 30,
        "avgOrderValue": 30
    }


def test_applies_min_total_spend_after_customer_aggregation():
    out = get_customer_metrics(
        data=data,
        from_="2026-01-10",
        to="2026-01-12",
        min_total_spend=50
    )

    # cust_1=80 include, cust_2=40 exclude, cust_3=30 exclude
    assert out["results"] == [
        {
            "customerId": "cust_1",
            "orderCount": 2,
            "totalSpend": 80,
            "avgOrderValue": 40
        }
    ]


def test_date_range_is_inclusive_on_both_ends():
    out = get_customer_metrics(
        data=data,
        from_="2026-01-10",
        to="2026-01-10"
    )

    result_map = by_customer(out["results"])

    assert out["results"] == [
        {
            "customerId": "cust_1",
            "orderCount": 1,
            "totalSpend": 30,
            "avgOrderValue": 30
        },
        {
            "customerId": "cust_2",
            "orderCount": 1,
            "totalSpend": 20,
            "avgOrderValue": 20
        }
    ]


def test_results_are_sorted_by_customer_id_ascending():
    out = get_customer_metrics(
        data=data,
        from_="2026-01-10",
        to="2026-01-14"
    )

    assert [r["customerId"] for r in out["results"]] == [
        "cust_1",
        "cust_2",
        "cust_3"
    ]


def test_returns_empty_results_when_no_orders_match_date_range():
    out = get_customer_metrics(
        data=data,
        from_="2026-02-01",
        to="2026-02-05"
    )

    assert out == {"results": []}
