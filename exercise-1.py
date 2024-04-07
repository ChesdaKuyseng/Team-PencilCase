list = [1,2,3,4,]
def replace_last(list):
    new_list = list
    if len(new_list) < 1:
        return new_list
    else:
        first = new_list[-1]
        new_list.insert(0,first)
        del new_list[-1]
        return new_list        
def main():
    print(f'{list} --> {replace_last(list)}')

if __name__ == "__main__":
    main()
