"""
Extract digit from a given number
input: 7895
output: [7, 8, 9, 5]
"""

def extract_digit(n):
    digits = []
    while n > 0:
        last_digit = n%10
        digits.append(last_digit)
        n = n // 10
    digits.reverse()
    return digits

if __name__ == "__main__":
    print(extract_digit(78958767))
