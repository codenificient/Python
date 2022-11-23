def CompoundInterest(principal, interest, years):
    return principal * pow((1 + interest / 365), years)


if __name__ == "__main__":
    prin = 42970
    rate = 0.863
    years = 15
    ci = round(CompoundInterest(prin, rate, years), 2)
    print(f"The compound interest for principal of {prin} at {rate} interest for {12 * years} months is ${ci:,}")