count = 0
def my_print_counter(thing_to_print):
    global count
    count += 1
    print(thing_to_print)

my_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def print_first_item(items):
    print(items[1])
"""O(1)"""

def print_all_items(items):
    for item in items:
        my_print_counter(item)

print_all_items(my_items)
"""O(n)"""

def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            my_print_counter((first_item, second_item))

print_all_possible_ordered_pairs(my_items)
