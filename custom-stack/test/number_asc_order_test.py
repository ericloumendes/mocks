import random

import pytest

from src.custom_stack_class import CustomStack, StackEmptyException
from src.number_asc_order import NumberAscOrder


class TestNumberAscOrder:

    @pytest.fixture
    def cut(self):
        return NumberAscOrder()

    @pytest.fixture
    def stack_mock(self, mocker):
        stack = mocker.Mock(spec=CustomStack)
        stack.limit = 6
        return stack

    def test_sort_stack_with_six_drawn_numbers(self, cut, stack_mock):
        # 6 números sorteados aleatoriamente (1 a 60, sem repetição), na ordem do sorteio
        drawn = random.sample(range(1, 61), 6)
        remaining = list(drawn)

        stack_mock.is_empty.side_effect = lambda: len(remaining) == 0
        stack_mock.pop.side_effect = lambda: remaining.pop()

        result = cut.sort(stack_mock)

        assert isinstance(result, list)
        assert 6 == len(result)
        assert sorted(drawn) == result
        assert 6 == stack_mock.pop.call_count

    def test_sort_empty_stack_raises_exception(self, cut, stack_mock):
        stack_mock.is_empty.return_value = True

        with pytest.raises(StackEmptyException):
            cut.sort(stack_mock)

        stack_mock.is_empty.assert_called_once()
        stack_mock.pop.assert_not_called()

    def test_sort_none_raises_exception(self, cut):
        with pytest.raises(ValueError):
            cut.sort(None)

    def test_sort_invalid_type_raises_exception(self, cut):
        with pytest.raises(TypeError):
            cut.sort([3, 1, 2])
