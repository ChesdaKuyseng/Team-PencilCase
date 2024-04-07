def chunking_by(numbers, chunck):
    if numbers:
        chunk_size = []
        for i in range(0, len(numbers), chunk):
            chunk_size.append(numbers[i:i + chunk])
        return chunk_size
    else:
        return []

def main():
    
    numbers_input = input("Enter numbers separated by commas: ")
    chunk_size_input = int(input("Please enter chunk size: "))
    
    numbers_str = numbers_input.replace('[', '').replace(']', '')
    numbers = [int(num.strip()) for num in numbers_str.split(',')]
    
    chunks = chunking_by(numbers, chunk_size_input)
    print(chunks)

if __name__ == "__main__":
    main()



