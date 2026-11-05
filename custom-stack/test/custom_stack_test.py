import pytest

from src.custom_stack_class import *


def test_new_stack_is_empty():
    cut = CustomStack(5)
    assert cut.is_empty() == True
    assert 0 == cut.size()
    assert 5 == cut.limit


def test_push_one_elementinstack():
    element_value = 5.0

    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()


def test_push_many_elements_keeps_lifo_order():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)
    cut.push(3)
    assert 3 == cut.size()
    assert 3 == cut.top()


def test_push_on_full_stack_raises_exception():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)
    with pytest.raises(StackFullException):
        cut.push(3)
    assert 2 == cut.size()
    assert 2 == cut.top()


def test_top_does_not_remove_element():
    cut = CustomStack(5)
    cut.push(10)
    assert 10 == cut.top()
    assert 10 == cut.top()
    assert 1 == cut.size()


def test_top_on_empty_stack_raises_exception():
    cut = CustomStack(5)
    with pytest.raises(StackEmptyException):
        cut.top()


def test_pop_returns_and_removes_elements_in_lifo_order():
    cut = CustomStack(5)
    cut.push(1)
    cut.push(2)
    assert 2 == cut.pop()
    assert 1 == cut.size()
    assert 1 == cut.pop()
    assert cut.is_empty() == True


def test_pop_on_empty_stack_raises_exception():
    cut = CustomStack(5)
    with pytest.raises(StackEmptyException):
        cut.pop()


def test_push_after_pop_on_full_stack():
    cut = CustomStack(1)
    cut.push(1)
    cut.pop()
    cut.push(2)
    assert 2 == cut.top()
