# Define the function for data_types
def number_data_type_examples():
    # this is the first comment
    spam = 1  # and this is the second comment

    text = '# This is...inside quotes'
    print(text)

    # numbers, strings, lists...

    simple_sum = 2 + 2
    print(simple_sum)

    print(50 - 5 * 6)

    print((50 - 5 * 6) / 4)

    print(8 / 5)

    # naming issues -> always lower case
    simpleSum = 'abc'
    print(simpleSum)

    print(17 / 3)

    print(17 // 3)
    print(17 % 3)
    print(5 * 3 + 2)

    print(5 ** 2)
    print(2 ** 7)

    print(-3 ** 2)
    print((-3) ** 2)

    width = 20
    height = 5 * 90
    print(width * height)
    print(width * height / 2)

    # print(n)  # not defined, value not set
    print(3 * 3.75 / 1.5)
    print(height + width)
    print(7.0 / 2)  # echo PHP, System.out.println(...) Java

    # trailing semicolon in the statement -> not needed in Python
    print(spam);

    number_prefix = 1
    number_prefix += 2
    number_prefix = number_prefix + 2
    # ++number_prefix
    print(number_prefix)

    # int / float: decimals, fractions, complex numbers

    print(pow(10, 2))
    print(round(1.5))


# function called from 5 places, issue in 1 place
def string_data_type_examples():
    simple_string = 'spam eggs'
    print(simple_string)

    print('don\'t')
    print("don't")

    print('"Yes," he said')

    # 2 contents ->
    # first content: First line.
    # second content: Second line
    ss = 'First line.\nSecond line'
    print(ss)

    # path
    print('C:\some\name')  # Windows
    print('/home/rares/test/python')  # Linux
    # never use absolute paths, always use relative (PROJECT, where it is installed)

    print(r'C:\some\name')

    # Python, Java, Ruby -> Cross Platform -> NT, Ubuntu

    print("""
        Usage:...
            -h
            -H
    """)

    # concatenation
    print(3 * 'un' + 'ium')

    a = 'Py'
    b = ' thon'
    print(a + b)

    prefix = 'Py'
    prefix += 'thon'  # increment the original value with another value
    # prefix = prefix + 'thon'
    print(prefix)

    # (1, 5) -> 2, 3, 4
    # [1, 5] -> 1, 2, 3, 4, 5
    # [n, m)
    word = 'Python'
    print(word[0])  # the String is kind of list, starting from index 0
    print(word[5])
    print(word[-1])  # start from right to left
    print(word[0:2])  # 0, 1, 2 (STOP -> excluded), 2-0 -> 2 elements
    print(word[:2])  # start from the beginning (which ever that is)
    print(word[4:])
    print(word[-2:])

    # 0  1  2  3  4  5
    # -6 -5 -4 -3 -2 -1
    # P  Y  T  H  O  N

    # print(word[42])
    value = word[4:42]
    print(f'Call from 4 to 42: {value}')

    args = f"Arguments: {value}"
    print(args)

    seconds_arguments = f"'Arguments': {value}"
    print(seconds_arguments)

    print(f'Last String command: {word[42:]}')
    print(len(word))  # 0 - (6-1)


def list_data_type_example():
    pass  # doesn't block the flow of the application, but it is non necessary if the function has body
    squares = [1, 4, 9, 16, 25]
    print(squares)

    print(squares[0])
    print(squares[-1])

    print(squares[-3:])
    print(squares[:])

    squares += [36, 49, 64, 81, 100]
    print(squares)

    cubes = [1, 8, 27, 65, 125]  # 1^3, 2^3, 3^3...
    print(f'Initial cubes: {cubes}')
    cubes[3] = 64
    print(f'Cubes after modification: {cubes}')

    cubes.append(216)
    print(cubes)
    cubes.append(7 ** 3)
    print(cubes)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters)

    letters[2:5] = ['C', 'D', 'E']
    print(letters)

    letters[2:5] = []
    print(letters)
    print(len(letters))

    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]  # will be 2 lists, 1 will be the information from "a" and one from "n"
    print(x)  # 2 elements
    print(x[0])


# 0, 1, 1, 2, 3, 5, 8, etc...
# if sequential
# a = 0
# b = 1
#
# a = 1
# b = 2
#
# a = 2
# b = 4
def fibonacci():
    a, b = 0, 1  # left side vs right side
    while b < 10:
        print(b)
        a, b = b, a + b  # parallel assignment

    a = 0
    b = 1


def flows_of_control():
    # if
    a_number = -1
    if a_number < 0:  # True / False
        print('Negative changed to 0')
    elif a_number == 0:
        print('Zero')
    elif a_number == 1:
        print('Single')
    else:
        print('More')

    # for
    word_example = 'abc'
    words = ['cat', 'dog', 'mouse']
    for word in words:  # local variable in for block -> word
        print(word_example)
        print(word, len(word))

    for index, word in enumerate(words):
        print(index)
        print(word, len(word))

    words.insert(0, 'abc')
    print(words)

    # while

    # range
    for i in range(5):
        print(i)

    for i in range(5, 10):
        print(i)

    # break
    # for all of the elements from 2 to 9 we check which numbers are PRIME (7, 2 - 6; 8, 2)
    # if the number if PRIME don't check it further
    for n in range(2, 10):  # 2, 9
        for x in range(2, n):  # 2-2, 2-3, 2-4, etc...
            if n % x == 0:
                print(n, 'equals', x, '*', n // x)
                break
            else:
                print(n, 'is a prime number')

    # continue
    for number in range(2, 10):
        if number % 2 == 0:
            print(f'Found an even number {number}')
            continue
        print(f'Found a number {number}')

    # pass

    # TODO(rflueras) switch, repeat, do while replacements when all data types are met


def data_models():
    # in Python -> everything is an object

    # every object has an identity, type, value
    a_number = 5
    print(id(a_number))

    b_number = 6
    print(id(b_number))

    print(type(a_number))
    print(a_number)

    # is
    # isinstance
    # ==
    # >, <, >=
    if a_number > b_number:
        print(a_number)

    if not a_number > b_number:
        print(a_number)


if __name__ == '__main__':
    number_data_type_examples()
    string_data_type_examples()  # we have 10 layers in this function
    list_data_type_example()
    fibonacci()
    flows_of_control()
    data_models()

# public static void main(String...) { }

# abc() {
#   logic
# }
