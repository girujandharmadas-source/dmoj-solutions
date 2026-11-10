"""
Problem: An Animal Contest 3 P1 - Monkey Shopping
Problem Code: aac3p1
DMOJ URL: https://dmoj.ca/problem/aac3p1
Language: Python 3
"""

A, B, C, D = map(int, input().split())

if A < B and C < D:
    print("Go to the department store")
elif A < B:
    print("Go to the grocery store")
elif C < D:
    print("Go to the pharmacy")
else:
    print("Stay home")
