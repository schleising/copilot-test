# Create n sets of ten random numbers between 1 and 1000 each using a list comprehension.
# and print them out.
import random
def create_list_of_sets(num_sets: int) -> list[set]:
    list_of_sets = [set(random.sample(range(1, 1001), 10)) for i in range(num_sets)]
    for i in range(num_sets):
        print(f"Set {i+1}: {list_of_sets[i]}")
    return list_of_sets

# Write a function to check whether any item is in more than one of n sets.
# If so, return True, otherwise return False.
# The function should take n sets as arguments and use set intersection
def check(list_of_sets: list[set]) -> bool:
    for i in range(len(list_of_sets)):
        for j in range(i+1, len(list_of_sets)):
            if list_of_sets[i] & list_of_sets[j]:
                return True
    return False

# Write a test function to check that the function works correctly.
# The test function should create n sets of ten random numbers between 1 and 1000 each.
# It should then check whether any item is in more than one of n sets.
# If so, it should print "True" and the sets in which the item is found.
# Otherwise, it should print "False".
def test():
    list_of_sets = create_list_of_sets(6)
    if check(list_of_sets):
        print("True")
    else:
        print("False")

# Write a main function to call the test function 100 times.
# It should print the number of times that the function returns True.
def main():
    count = 0
    for i in range(100):
        list_of_sets = create_list_of_sets(6)
        if check(list_of_sets):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
