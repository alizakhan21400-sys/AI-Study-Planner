subjects = int(input("Enter number of subjects: "))

for i in range(subjects):
    name = input("Enter subject name: ")
    modules = int(input(f"Enter number of modules in {name}: "))
    
    print(f"{name} has {modules} modules")

print("Study planner will be generated...")
