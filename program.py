chore_list = []
choice = 0

while choice != 3:
    try: 
        choice = int(input("Make a choice \n1. Add a Chore\n2. Check Off Chore\n3. Quit\n"))
    
    except ValueError:
        print("Invalid Input!")
        continue
        
        
         
    if choice == 1:
        print("You chose 1")
    elif choice == 2:
        print("You chose 2")
    else:
        print("Invalid Input")
        continue
        
        
print("Done!")