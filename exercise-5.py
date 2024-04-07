def reverse_ascending(numbers):
    result = []
    subsequence = [] 

    for num in numbers:
        if not subsequence or num >= subsequence[-1]:
            
            subsequence.append(num)  
        else:
            
            result.extend(reversed(subsequence))  
            subsequence = [num]
    result.extend(reversed(subsequence))  

    return result


def main():
    numbers = input("Enter a list of numbers, separated by spaces: ").split()
    numbers = [int(num) for num in numbers]  
    return numbers

input_list = main()
output_list = reverse_ascending(input_list)
print("Reversed list of ascending subsequences:", output_list)
