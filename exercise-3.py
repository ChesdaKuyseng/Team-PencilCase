def remove_all_after(numbers, n):
    if numbers == []:
        return numbers  
    
    try:
        index_to_remove = numbers.index(n)  
        result = numbers[:index_to_remove + 1]  
        return result
    except ValueError:
        return numbers 

def main():
    numbers_input = input("Please enter your numbers in list by commas: ")
    n_input = int(input("Enter the number to remove all after: "))
    
    numbers_str = numbers_input.replace('[', '').replace(']', '')
    numbers = [int(num.strip()) for num in numbers_str.split(',')]
    
    result = remove_all_after(numbers, n_input)
    print("Result:", result)

if __name__ == "__main__":
    main()

