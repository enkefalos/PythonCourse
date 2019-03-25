def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """
    current_number = 100_000
    number_list = []
    while current_number < 1_000_000:
        if check_if_palindrome(str(current_number)[2:]):
            temp_number = current_number + 1
            if check_if_palindrome(str(temp_number)[1:]):
                temp_number = temp_number + 1
                if check_if_palindrome(str(temp_number)[1:-1]):
                    temp_number = temp_number + 1
                    if check_if_palindrome(str(temp_number)):
                        number_list.append(current_number)
        current_number += 1
    
    return number_list

def check_if_palindrome(number: str):
    return number == number[::-1]

if __name__ == '__main__':
    # Question 2
    print('The numbers between 100000 and 999999 that fulfill the required conditions are:')
    number_list = check_palindrome()
    for number in number_list:
        print(str(number))
