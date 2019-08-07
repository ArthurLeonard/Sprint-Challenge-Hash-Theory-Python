#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # 0 - check if hash table works properly ************8
    # for i in range(length):
    #     hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    # print(tickets)
    # for i in range(length):
    #     print(hash_table_retrieve(hashtable, tickets[i].source))
    # 1 - Place destinations in hash table with source as key and destination as value

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    # 2 - Find the ticket that has source equal to None
    array_index = 0
    index = 0
    for i in range(length):
        if tickets[i].source == "NONE":
            index = i
            break
    next_stop = tickets[index].destination
    route[array_index] = next_stop

    print("first stop is : ", tickets[index].destination)

    while next_stop != "NONE":
        array_index += 1
        print("next stop is ", next_stop)
        # 3 - Search for its destination as a key in the hash table
        next_stop = hash_table_retrieve(hashtable, next_stop)
        route[array_index] = next_stop

    # 4 - Repeat step 3 for the value returned by hash retrieve

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
route = reconstruct_trip(tickets, 3)
print(route)