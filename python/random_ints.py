import random

def random_ints():
    # Write your code here!
    num = 0
    l = []

    while not(num == 7):
        num = (int) (random.random() * 10 + 1)
        l.append(num)

    return l

def test():
    N = 10000
    total_length = 0
    for i in range(N):
        l = random_ints()
        assert not 0 in l
        assert not 11 in l
        assert l[-1] == 7
        total_length += len(l)
    assert abs(total_length / N - 10) < 1 # checks that the length of the random strings are reasonable.
    print("Success!")

if __name__ == "__main__":
    test()