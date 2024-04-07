def index_power(array, n):
    if n < len(array):
        return array[n] ** n
    else:
        return -1
def main():
    n = int(input('Input n = '))
    array = [1, 0]
    print(index_power(array,n))
if __name__ == "__main__":
    main()
