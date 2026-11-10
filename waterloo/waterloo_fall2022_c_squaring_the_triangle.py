"""
Problem: Waterloo Local Contest Fall 2022 Problem C - Squaring the Triangle
Language: Python 3
"""

import sys

def solve():
    stdin = sys.stdin
    first_line = stdin.readline()
    if not first_line:
        return

    MOD = 1_000_000_007
    INV6 = 166666668  
    INV2 = 500000004  
    write = sys.stdout.write

    for line in stdin:
        parts = line.split()
        if not parts:
            continue

        N = int(parts[0])
        p = int(parts[1])
        q = int(parts[2])

        if N < 3:
            write("0\n")
            continue

        rho = (p * pow(q, 1000000005, MOD)) % MOD
        rho2 = (rho * rho) % MOD
        rho3 = (rho2 * rho) % MOD
        rho5 = (rho3 * rho2) % MOD
        rho6 = (rho5 * rho) % MOD

        c3 = (N * (N - 1) % MOD * (N - 2) % MOD * INV6) % MOD

        if N >= 4:
            c2 = (N * (N - 1) % MOD * (N - 2) % MOD * (N - 3) % MOD * INV2) % MOD
        else:
            c2 = 0

        total_pairs = (c3 * c3) % MOD
        c01 = (total_pairs - c2 - c3) % MOD

        ans = (c3 * rho3 + c2 * rho5 + c01 * rho6) % MOD
        write(str(ans) + "\n")

if __name__ == "__main__":
    solve()
