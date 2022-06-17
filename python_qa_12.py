# Calculate income tax for the given income by adhering to the below rules   

def tax_amount(income):
    if income <= 10000:
        return ("The income is not taxable")
    if 10000 < income < 20000:
        return((income -10000) * 0.1)
    
    if income > 20000:
        return (10000 * 0.1) +(income - 20000 * 0.2)

print(tax_amount(15000))