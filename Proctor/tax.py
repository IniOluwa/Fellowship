# Tax Lab
def calculate_tax(income):
    if type(income) is not dict:
        return 'Only dictionaries are accepted.'

    tax = 0
    non_taxed_income = 0
    for key, val in income.items():
        the_income = income[key]

        if the_income >= 1000:
            tax = 1000 * 0.0
            non_taxed_income = the_income - 1000
        else:
            tax = 0
            non_taxed_income = the_income

        if non_taxed_income > 1000:
            tax += 9000 * 0.10
            non_taxed_income -= 9000
        elif non_taxed_income > 0 and non_taxed_income < 10000:
            tax += non_taxed_income * 0.10
            non_taxed_income -= non_taxed_income

        if non_taxed_income > 10200:
            tax += 10200 * 0.15
            non_taxed_income -= 10200
        elif non_taxed_income > 0 and non_taxed_income < 20200:
            tax += non_taxed_income * 0.15
            non_taxed_income -= non_taxed_income

        if non_taxed_income > 20200:
            tax += 20200 * 0.20
            non_taxed_income -= 20200
        elif non_taxed_income > 0 and non_taxed_income < 30750:
            tax += non_taxed_income * 0.20
            non_taxed_income -= non_taxed_income

        if non_taxed_income > 30750:
            tax += 30750 * 0.25
            non_taxed_income -= 30750
        elif non_taxed_income > 0 and non_taxed_income < 50000:
            tax += non_taxed_income * 0.25
            non_taxed_income -= non_taxed_income

        if non_taxed_income > 50000:
            tax += 50000 * 0.30
        elif non_taxed_income > 0 and non_taxed_income < 50000:
            tax += non_taxed_income * 0.30
            non_taxed_income -= non_taxed_income

        the_income = tax
        print non_taxed_income, tax


income = {
    'James': 20500,
    'jon': 10000,
    'arya': 25000,
    'bran': 39000,
    'sansa': 500
}

calculate_tax(income)
