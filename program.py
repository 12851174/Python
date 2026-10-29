chore_list = []
choice = 0

while True:
    try: 
        choice = int(input("\n1. Add a Chore\n2. Check Off Chore\n3. Display List\n4. Quit\nMake a Choice (1, 2, 3, 4): "))
    
    except ValueError:
        print("Invalid Input")
        continue

        
    if choice == 1:
        chore = input("Enter a chore to add to the list: ")
        chore_list.append(chore)
    
    elif choice == 2:
        try:
            index = int(input("\nEnter an index from the list you'd like to delete: "))
        except ValueError:
            print("Invalid Input")
            continue

        if index <= len(chore_list) or index < 1:
            chore_list = chore_list[:index - 1] + chore_list[index:]
        else:
            print("Invalid Index\n")
            
    
    elif choice == 3:
        display = "\nList:\n"
        for i,chore in enumerate(chore_list):
            display += f"{i + 1}: {chore}\n"
        print(display)
        input("Press enter to continue")

    elif choice == 4:
        break

    else:
        print("Invalid Input")
        continue
        
        
print("\nProgram Finished")