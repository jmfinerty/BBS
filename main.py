# x_n+1 = x^2_n (mod M)
def bbs(p, q, s, N):
    M = p*q
    result = ''
    for _ in range(N):
        s = (s**2) % M
        result += str(s % 2)
    return result


# Given a string s,
# returns a list containing every
# subsequence in s of length n.
# Cuts off end remainder if present.
def subsequences(s, n):
    subseqs = []
    if n != 0:
        while s:
            if len(s[:n]) == n:
                subseqs.append(s[:n])
                s = s[n:]
            else:
                break
    return subseqs


def main():

    # "Use the algorithm with p = 1000003 and q = 2001911.
    # Select a valid seed x (there are valid seed that are
    # less than 10, pick one of them) and generate a
    # sequence of length 100,000."
    result100k = bbs(1000003, 2001911, 5, 100000)

    subseqs = subsequences(result100k, 1000)
    counts0 = []
    for s in subseqs:
        counts0.append(s.count("0"))
    avg0 = sum(counts0) / len(counts0)

    seq4 = ["0000", "0001", "0010", "0011",
            "0100", "0101", "0110", "0111",
            "1000", "1001", "1010", "1011",
            "1100", "1101", "1110", "1111"]
    subseqs = subsequences(result100k, 4)
    seq4_counts = []
    for seq in seq4:
        count = subseqs.count(seq)
        seq4_counts.append((seq, count))

    # Printing results to console
    print("\nIn generated sequence of length 100,000")
    print("where p = 1000003, q = 2001911, x = 5:")

    # "Compute the average number of 0's in a subsequence
    # of length 1000 over all such subsequences."
    print("\nAverage number of 0's in subsequences of length 1000:")
    print(avg0)

    # "Among all subsequences of length 4 (there are 16 of them)
    # tabulate the frequence of each of them occuring as a
    # subsequence of the sequence you generated."
    print("\nFrequency of each subsequence of length 4:")
    print("seq ", ":", "freq")
    for s in seq4_counts:
        print(s[0], ":", s[1])


main()
