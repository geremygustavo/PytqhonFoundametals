# Functions


def say_hello_word(name='Geremy'):
    """
    This Function say hello word
    :param name: name fo user

    """
    print(f'hello word by {name}')


say_hello_word('abel'.capitalize())
say_hello_word('gustavo'.capitalize())
say_hello_word('rodrigo'.capitalize())

# Default parameters
say_hello_word()

# keyword arguments
say_hello_word(name='bibi')


# Return

def sum(num1, num2):
    """
    This Function make a summatory  of two numbers
    :param num1:
    :param num2:
    :return: sum of two num1 and num2
    """
    return num1 + num2


print(sum(1, 7))


# function inside function

def sum(num1, num2):
    """

    :param num1:
    :param num2:
    :return:
    """
    def other_func(n1, n2):
        """

        :param n1:
        :param n2:
        :return:
        """
        return n1 + n2

    return other_func(num1, num2)


print(sum(9, 8))
