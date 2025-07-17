import math

def count_digits(n: int) -> int:
    power = int(math.log10(n))
    return power + 1

if __name__ == "__main__":
    print(count_digits(n=7654))