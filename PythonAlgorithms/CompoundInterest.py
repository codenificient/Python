def CompoundInterest(principal, interest, years):
    return principal * pow((1 + interest / 100), years)


if __name__ == "__main__":
    prin = 80000
    rate = 9.2
    months = 10
    ci = round(CompoundInterest(prin, rate, months), 2)
    print(f"The compound interest for principal of {prin} at {rate} interest for {months} months is ${ci:,}")