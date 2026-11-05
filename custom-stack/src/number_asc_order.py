from src.custom_stack_class import CustomStack, StackEmptyException


class NumberAscOrder:

    def sort(self, stack):
        if stack is None:
            raise ValueError("A pilha não pode ser None")
        if not isinstance(stack, CustomStack):
            raise TypeError("O parâmetro deve ser uma CustomStack")
        if stack.is_empty():
            raise StackEmptyException

        numbers = []
        while not stack.is_empty():
            numbers.append(stack.pop())

        return sorted(numbers)
