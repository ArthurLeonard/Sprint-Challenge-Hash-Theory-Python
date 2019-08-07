#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # 0 - see if hash table functions properly *******

    # 1 - place each weight into the hashtable 
    print(weights)
        # key is weight, value is index of weight *******
    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)
    # for i in range(length):
    #     print(hash_table_retrieve(ht, weights[i]))

    # 2 - go through the list of weights, for each weight check if the corresponding weight exists in the hash table
    for i in range(length):
        # single weight
        result = hash_table_retrieve(ht, limit - weights[i])
        if result != None:
            print("pair found: ", i, result)
            return (result, i)


    # 3 - If the two proper weights are found return their indices (larger number first??)
    answer = 'SU'
    print_answer(answer)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights = [10, 20, 30 , 40, 50, 60, 70, 80, 90, 100]
get_indices_of_item_weights(weights, 10, 100)