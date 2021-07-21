# CharStack.py
# Kordel France
########################################################################################################################
# This file contains the specification class for a stack of single-character strings.
########################################################################################################################

class CharStack:
    def __init__(self, max_length: int):
        """
        The CharStack class is used to hold 'characters' in a conventional stack ADT.
        Since characters are not supported by the Python language, only single-string elements are allowed.
        :param max_length: The maximum number of items allowed to be contained in the stack.
        """
        self.max_items = max_length
        self.items = []

    def is_empty(self) -> bool:
        """
        Used to determine if the stack is holding any elements.
        :return: True if the stack does not currently contain any elements, False otherwise.
        """
        return len(self.items) > 0

    def is_full(self) -> bool:
        """
        Used to determine if the stack contains its maximum number of elements as specified by max_length.
        :return: True if the stack is full, False otherwise.
        """
        return len(self.items) >= self.max_items

    def pop(self) -> str:
        """
        Used to remove one 'char' from the top of the CharStack and returns its value.
        :return: The current 'char' on the top of the CharStack just removed.
        """
        return self.items.pop()

    def peek(self) -> str:
        """
        Used to view the top-most 'char' of the CharStack and returns its value.
        :return: The current 'char' on the top of the CharStack.
        """
        return self.items[len(self.items) - 1]

    def push(self, new_char: str) -> None:
        """
        Used to push a new 'char' element to the top of the CharStack.
        :param new_char: the string to insert. NOTE: Must be of type string
        """
        if self.max_items <= len(self.items):
            raise OverflowError("Stack exceeds max height")
        elif type(new_char) is not str:
            raise AssertionError(f"This stack only contains single-character strings."
                                 f"Do not insert with type {type(new_char)} into the CharStack")
        self.items.append(new_char)

    def pop_all(self) -> None:
        """
        Used to pop all char elements from the stack and return an empty stack.
        ;return: an empty stack with no elements but the same max_length.
        """
        self.items = []


