def fruit_list_practice():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print("Length of the list:", len(fruit_list))
    
    fruit_list.append('mango')
    
    print("Updated fruit list:", fruit_list)

def index_game():
    game_list = [10, 'hello', 3.14, True, 42]
    
    def access_element(lst, index):
        try:
            return lst[index]
        except IndexError:
            return "Index out of range"
    
    def modify_element(lst, index, new_value):
        try:
            lst[index] = new_value
            return lst
        except IndexError:
            return "Index out of range"
    
    def slice_list(lst, start, end):
        try:
            return lst[start:end]
        except IndexError:
            return "Invalid slice indices"
    
    while True:
        print("\nCurrent List:", game_list)
        print("Operations:")
        print("1. Access Element")
        print("2. Modify Element")
        print("3. Slice List")
        print("4. Exit")
        
        choice = input("Choose an operation (1-4): ")
        
        if choice == '1':
            try:
                index = int(input("Enter index to access: "))
                result = access_element(game_list, index)
                print("Element at index", index, "is:", result)
            except ValueError:
                print("Please enter a valid integer index.")
        
        elif choice == '2':
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                result = modify_element(game_list, index, new_value)
                print("Updated list:", result)
            except ValueError:
                print("Please enter a valid integer index.")
        
        elif choice == '3':
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                result = slice_list(game_list, start, end)
                print("Sliced list:", result)
            except ValueError:
                print("Please enter valid integer indices.")
        
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Fruit List Practice:")
    fruit_list_practice()
    
    print("\nIndex Game:")
    index_game()

if __name__ == "__main__":
    main()