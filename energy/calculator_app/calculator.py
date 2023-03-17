def calculator(consumption: list, distributor_tax: float, tax_type: str, dev_teste=False) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage
    
    For passing the teste, use dev_teste to returns a list values.
    """

    annual_savings = 0
    monthly_savings = 0
    applied_discount = 0
    consumption_average = sum(consumption) / len(consumption)

    if consumption_average < 10000:
        coverage = 0.90
        if tax_type == 'Residencial':
            applied_discount = 0.18
        elif tax_type == 'Comercial':
            applied_discount = 0.16
        elif tax_type == 'Industrial':
            applied_discount = 0.12

    elif consumption_average >= 10000 and consumption_average <= 2000:
        coverage = 0.95
        if tax_type == 'Residencial':
            applied_discount = 0.22
        elif tax_type == 'Comercial':
            applied_discount = 0.18
        elif tax_type == 'Industrial':
            applied_discount = 0.15

    else:
        coverage = 0.99
        if tax_type == 'Residencial':
            applied_discount = 0.25
        elif tax_type == 'Comercial':
            applied_discount = 0.22
        elif tax_type == 'Industrial':
            applied_discount = 0.18

    cost_monthly = distributor_tax * consumption_average * coverage
    monthly_savings = cost_monthly * applied_discount
    annual_savings = monthly_savings * 12
    
    if dev_teste is True:
        result = tuple(round(annual_savings, 2), round(monthly_savings, 2), applied_discount, coverage)
    else:
        result = {
            'annual_savings': round(annual_savings, 2),
            'monthly_savings': round(monthly_savings, 2),
            'applied_discount': applied_discount,
            'energy_coverage': coverage,
        }

    return result


if __name__ == "__main__":
    print("Testing...")

    assert calculator([1518, 1071, 968], 0.95871974, "Industrial", True) == (
        1473.19,
        122.77,
        0.12,
        0.9,
    )

    assert calculator([1000, 1054, 1100], 1.12307169, "Residencial", True) == (
        2295.32,
        191.28,
        0.18,
        0.9,
    )

    assert calculator([973, 629, 726], 1.04820025, "Comercial", True) == (
        1405.56,
        117.13,
        0.16,
        0.9,
    )

    assert calculator([15000, 14000, 16000], 0.95871974, "Industrial", True) == (
        24591.16,
        2049.26,
        0.15,
        0.95,
    )

    assert calculator([12000, 11000, 11400], 1.12307169, "Residencial", True) == (
        32297.74,
        2691.48,
        0.22,
        0.95,
    )

    assert calculator([17500, 16000, 16400], 1.04820025, "Comercial", True) == (
        35776.75,
        2981.40,
        0.18,
        0.95,
    )

    assert calculator([30000, 29000, 29500], 0.95871974, "Industrial", True) == (
        60478.73,
        5039.89,
        0.18,
        0.99,
    )

    assert calculator([22000, 21000, 21400], 1.12307169, "Residencial", True) == (
        71602.56,
        5966.88,
        0.25,
        0.99,
    )

    assert calculator([25500, 23000, 21400], 1.04820025, "Comercial", True) == (
        63832.12,
        5319.34,
        0.22,
        0.99,
    )

    print("Everything passed")
