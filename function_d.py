def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    for num in numbers : 
        if num == max(numbers):
            return num

#just testing some stuff
if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
