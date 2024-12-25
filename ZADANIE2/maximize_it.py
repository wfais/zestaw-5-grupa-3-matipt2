from itertools import product

def maximize_expression(K, M, lists):
    max_s = 0
    for combination in product(*lists):
        s = sum(x**2 for x in combination) % M
        max_s = max(max_s, s)
    return max_s

if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
