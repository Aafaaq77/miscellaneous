# Uses python3
import sys

def optimal_weight(weight, items):
    # write your code here
    import numpy as np
    zeros_array = np.zeros((len(items), weight), dtype=int)
    results_list = zeros_array.tolist()
    for i in range(1, len(items)):
        for w in range(1, weight):
            results_list[i][w] = results_list[i - 1][w]
            if items[i] <= w:
                val = results_list[i - 1][w - items[i]] + items[i]
                if results_list[i][w] < val:
                    results_list[i][w] = val
                    
    # for x in w:
       # if result + x <= W:
        #    result = result + x
    return results_list[len(items) - 1][weight - 1]

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     W, n, *w = list(map(int, input.split()))
#     print(optimal_weight(W, w))

print(optimal_weight(10, [1, 4, 8]))
