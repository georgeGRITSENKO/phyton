def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def main():
    max_sum = 0
    number_with_max_sum = None

    print("Введите целые числа (введите 0 для завершения):")

    while True:
        number = int(input())
        if number == 0:
            break

        current_sum = sum_of_digits(number)
        if current_sum > max_sum:
            max_sum = current_sum
            number_with_max_sum = number

    if number_with_max_sum is not None:
        print(f"Число с максимальной суммой цифр: {number_with_max_sum}")
        print(f"Сумма его цифр: {max_sum}")
    else:
        print("Не введено ни одного числа.")
        
if __name__ == "__main__":
    main()
    