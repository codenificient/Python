# Perfect number is a number which equals the sum of its divisors ie 6 (1+2+3)
def checkPerfect(num):
    sumFactors = 0

    for idx in range(1, num):
        if num % idx == 0:
            sumFactors += idx
        
    if sumFactors == num:
        return True
    
    return False

# Python Routine to List all the perfect numbers less than or equal to a given Upper limit
def ListPerfectNums(upper):
    PerfectNums = []
    for num in range(upper):
        if checkPerfect(num):
            PerfectNums.append(num)
    return PerfectNums
    

if __name__ == "__main__":
    print(ListPerfectNums(9))
    print(ListPerfectNums(190))
    print(ListPerfectNums(600))