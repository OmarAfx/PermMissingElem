def solution(A):
    N = len(A)

    # Add up what the total WOULD be if no number were missing: 1 + 2 + ... + (N+1).
    # range stops one before its end value, so N + 2 makes it include N + 1.
    expected = 0
    for i in range(1, N + 2):
        expected = expected + i

    # Add up the numbers that are actually in the array
    actual = 0
    for x in A:
        actual = actual + x

    # The only thing that makes the totals differ is the missing number
    return expected - actual