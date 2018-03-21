'''excercise from http://www.practicepython.org/'''
def input_character():
    name = raw_input("Give me your name: ")
    age = raw_input("Give me your age: ")
    print(name + ' You will become 100 in the year of ' + str(2117-int(age)))
    print_n=int(raw_input("Give me your name: "))
    i=0
    while(i<print_n):
        print(name + ' You will become 100 in the year of ' + str(2117 - int(age)))
        i += 1


def check_odd_even(x):
    '''Ask the user for a number. Depending on whether the number is even or odd, print out an message to the user
    Args:
        integer
    Returns:
        string (Even/Odd)
        '''
    if x%2 == 0:
        print ("{} is an Even number".format(x))
    else:
        print("{} is an Odd number".format(x))
#__name__ == '__main__' condition allow the function to be imported in REPL w/o running them. Whereas whatever you want to run,
# throw inside the if statement
#  can run using a script
if __name__ == "__main__":
    check_odd_even(16)