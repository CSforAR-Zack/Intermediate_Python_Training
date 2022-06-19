class Stack():
    """ LIFO Data Structure. """
    
    # Setup and Instance Variables
    def __init__(self):
        # __ means a private variable
        # keep in mind that nothing is truly private in Python
        self.__items = []

    # Methods
    def push(self, value):
        self.__items.append(value)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        if self.__items > 0:
            return self.__items[-1]
        else:
            return []

    # Magic Method that makes for a pretty print()
    def __str__(self):
        return str(self.__items)


class Queue():
    """ FIFO Data Structure. """

    # Setup and Instance Variables
    def __init__(self):
        self.__items = []

    # Methods
    def add(self, value):
        self.__items.append(value)

    def remove(self):
        return self.__items.pop(0)

    def peek(self):
        if self.__items > 0:
            return self.__items[0]
        else:
            return []

    # Magic Method that makes for a pretty print()
    def __str__(self):
        return str(self.__items)
