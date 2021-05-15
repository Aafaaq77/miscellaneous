# Uses python3
import sys

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

def get_operation(memory, i, num):
    """
    memory list of shortest paths (iterations) to i
    returns the operation: 1 = * by 2 
    2 = * 3
    3 = add 1
    """
    if memory[i//3] <= memory[i//2] and memory[i//3] <= memory[i -1]:
        return num // 3
    elif memory[i//2] <= memory[i//3] and memory[i//2] <= memory[i -1]:
        return num // 2
    else:
        return num - 1

def get_sequence(num):
    sequence = []
    sequence_num = num
    cache = {}
    memory = [0]
    for i in range(1, num + 1): # choses best path to i at every step
        if i == 1:
            memory.append(0)
            cache[str(i)] = 1
        elif (i % 2 == 0) and (i % 3 == 0):
            memory.append(1 + min(memory[i//2], memory[i//3], memory[i -1]))
            cache[str(i)] = 3
        elif i % 2 == 0:
            memory.append(1 + min(memory[i//2], memory[i - 1]))
            if memory[i//2] < memory[i - 1]:
                cache[str(i)] = 2
            else:
                cache[str(i)] = 1
        elif i % 3 == 0:
            memory.append(1 + min(memory[i//3], memory[i - 1]))
            cache[str(i)] = 3
        else:
            memory.append(1 + memory[i - 1])
            cache[str(i)] = 1
    while sequence_num >= 1:
            sequence.append(sequence_num)
            if cache[str(sequence_num)] == 1:
                sequence_num = sequence_num - 1
            else:
                sequence_num = sequence_num // cache[str(sequence_num)]          
    return sequence[::-1]
    # if num == 0:
    #     return num
    # tokens = [3, 2, 1]
    # for token in tokens:
    #     if token == 1:
    #         solution = get_sequence(num - 1, cache)
    #         sequence.append(num)
    #         solutions.add(solution)
    #     elif num % token == 0:
    #         solution = get_sequence(num / token, cache)
    #         solutions.add(solution)
            
    # return min(solutions)
            

input = sys.stdin.read()
n = int(input)
sequence = list(get_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

#print(get_sequence(10))
#print(sequence)
