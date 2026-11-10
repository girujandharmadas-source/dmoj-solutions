"""
Problem: CCC '25 J1 - Roller Coaster Ride
Problem Code: ccc25j1
DMOJ URL: https://dmoj.ca/problem/ccc25j1
Language: Python 3
"""

N = int(input().strip())
C = int(input().strip())
P = int(input().strip())

if N <= C * P:
    print("yes")
else:
    print("no")
