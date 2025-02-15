from colorama import Fore, init

init(autoreset=True)

def find_min_max(arr):
    """
    Знаходить мінімальний та максимальний елементи в масиві за допомогою підходу «розділяй і володарюй».

    :param arr: список чисел
    :return: кортеж (мінімальне значення, максимальне значення)
    """
    def min_max_helper(left, right):
        if left == right:
            return arr[left], arr[left]
        
        if right - left == 1:
            return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
        
        mid = (left + right) // 2
        left_min, left_max = min_max_helper(left, mid)
        right_min, right_max = min_max_helper(mid + 1, right)
        
        return min(left_min, right_min), max(left_max, right_max)
    
    if not arr:
        raise ValueError("Array cannot be empty")
    
    return min_max_helper(0, len(arr) - 1)

if __name__ == "__main__":
    numbers = [12, 26, 4, 17, 21, 1, 22, 10]
    min_val, max_val = find_min_max(numbers)

    print(Fore.GREEN + "Масив чисел:", numbers)
    print(Fore.CYAN + f"Мінімальне значення: {min_val}")
    print(Fore.MAGENTA + f"Максимальне значення: {max_val}")
