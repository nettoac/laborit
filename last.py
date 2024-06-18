import random

def digito_Verificador():
    random_numbers = [random.randint(1, 10) for _ in range(6)]
    powered_numbers = [number ** 0 for number in random_numbers]
    return powered_numbers[0]
