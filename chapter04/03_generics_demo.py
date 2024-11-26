from typing import Sequence, TypeVar, List, Any, Optional

T = TypeVar('T')
Number = TypeVar("Number", int, float)

def first(seq: Sequence[T]) -> T:
    if seq is None or len(seq) == 0:
        raise ValueError("Sequence is empty.")
    return seq[0]

def last(seq: Sequence[T]) -> T:
    if not seq:
        raise ValueError("Sequence is empty.")
    return seq[-1]

# def count_truthy(elements: List[any]) -> int:
#     if elements is None:
#         return 0
#     total = 0
#     for element in elements:
#         if element:
#             total += 1
#     return total

def count_truthy(elements: List[any]) -> int:
    return sum(1 for element in elements if element)

def len_str(s: Optional[str] = None):
    return len(s) if s is not None else 0

def main():
    # Demonstrations
    numbers = [10, 20, 30, 40, 50]
    print("First number", first(numbers))
    print("Last number", last(numbers))
    
    try:
        print("First num in empty list:", first([]))
    except ValueError as e:
        print(e)
    
    mixed_values = [0, True, False, 'hello', '', None, 100]
    print("Truthy count:", count_truthy(mixed_values))
    
    print("Length of 'Hello':", len_str("Hello"))
    print("Length of None:", len_str(None))

if __name__ == "__main__":
    main()
