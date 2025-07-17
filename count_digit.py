import math
"""
Count digit from a given number
input 8767
output 4
"""
def count_digits(n: int) -> int:
    power = int(math.log10(n))
    return power + 1

if __name__ == "__main__":
    print(count_digits(n=7654))