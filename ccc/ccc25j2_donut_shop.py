"""
Problem: CCC '25 J2 - Donut Shop
Problem Code: ccc25j2
DMOJ URL: https://dmoj.ca/problem/ccc25j2
Language: Python 3
"""

D = abs(int(input()))
E = abs(int(input()))

for i in range(E):
    aSymbol = input().split()
    Q = abs(int(input()))
    if aSymbol[0] == "+":
        D += Q
    elif aSymbol[0] == "-":
        D -= Q

print(D)
