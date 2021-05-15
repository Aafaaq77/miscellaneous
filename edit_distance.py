# Uses python3
import numpy as np

def edit_distance(s, t):
    #write your code here
    str1_len = len(s)
    str2_len = len(t)
    distance_array = distance_array = np.zeros((str1_len + 1, str2_len + 1), dtype=int)
    distance_list = distance_array.tolist()
    for i in range(len(distance_list)):
        distance_list[i][0] = i
    
    for j in range(len(distance_list[0])):
        distance_list[0][j] = j
    
    for j in range(1, str2_len + 1):
        for i in range(1, str1_len + 1):
            insertion = distance_list[i][j - 1] + 1
            deletion = distance_list[i - 1][j] + 1
            match = distance_list[i - 1][j - 1]
            mismatch = distance_list[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                distance_list[i][j] = min(match, deletion, insertion)
            else:
                distance_list[i][j] = min(mismatch, deletion, insertion)
            
    return distance_list[str1_len][str2_len]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
# print(edit_distance("editing", "distance"))

