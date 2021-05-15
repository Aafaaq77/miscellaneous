# Uses python3
import sys




def get_least_coins(money, coins, cache):
    if money == 0:
        return 0
    if money == 1:
        return 1
    solutions = []
    for coin in coins:
        if (money - coin >= 0):
            if f"get_least_coins({money - coin}" not in cache:
                solution = get_least_coins(money - coin, coins, cache)
                cache[f"get_least_coins({money - coin}"] = solution
                solutions.append(solution + 1)
            else:
                solution = cache[f"get_least_coins({money - coin}"]
                solutions.append(solution + 1)
        
    return min(solutions)
            


def get_change(m):
    #write your code here
    coins = [4, 3, 1]
    cache = {}
    num_coins = get_least_coins(m, coins, cache, )
    return num_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

# money = 6
# print(get_change(money))