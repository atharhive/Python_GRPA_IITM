def collatz(n):
    # base case of the recursion
    # if n = 1, you don't need to call the function at all
    if n == 1:
        return 0
    # simple application of the piecewise defn of the
    # Collatz function
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    else:
        return 1 + collatz(3 * n + 1)
