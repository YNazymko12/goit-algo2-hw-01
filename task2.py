from colorama import Fore, init
import random

init(autoreset=True)

def quick_select(arr, k):
    """
    Знаходить k-й найменший елемент у несортованому масиві за допомогою Quick Select.

    :param arr: список чисел
    :param k: порядковий номер (1-індексація)
    :return: k-й найменший елемент
    """
    if not (1 <= k <= len(arr)):
        raise ValueError("k має бути в межах довжини масиву")

    def select(left, right):
        pivot = arr[random.randint(left, right)]
        lows = [x for x in arr if x < pivot]
        equals = [x for x in arr if x == pivot]
        highs = [x for x in arr if x > pivot]
        
        if k <= len(lows):
            return quick_select(lows, k)
        elif k <= len(lows) + len(equals):
            return pivot
        else:
            return quick_select(highs, k - len(lows) - len(equals))
    
    return select(0, len(arr) - 1)

if __name__ == "__main__":
    numbers = [12, 26, 4, 17, 21, 1, 22, 10]
    k = 3
    kth_smallest = quick_select(numbers, k)

    print(Fore.GREEN + "Масив чисел:", numbers)
    print(Fore.CYAN + f"{k}-й найменший елемент: {kth_smallest}")
