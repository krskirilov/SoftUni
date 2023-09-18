#  find the Greatest Common Divisor

A = int(input())
B = int(input())

while B:
    residual = A % B
    A = B
    B = residual

print(A)
