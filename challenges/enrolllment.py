def accept_input(name, enrolles):
    # prompt user to enter 15 names of trainers and number of enrolles for each using array
    print("Enter 15 names of trainers and number of enrolles for each using array")
    for i in range(15):
        name.append(input("Enter name of trainer: "))
        enrolles.append(int(input("Enter number of enrolles: ")))

def display(name, enrolles):
    # display the names of trainers and number of enrolles for each using array
    print("Names of trainers and number of enrolles for each using array")
    for i in range(15):
        print("Name of trainer: ", name[i])
        print("Number of enrolles: ", enrolles[i])

# three categories of trainers with enrolles in 0 - 5, 5-10, 10 - 15
def categorize(name, enrolles, category1, category2, category3):
    for i in range(15):
        if enrolles[i] >= 0 and enrolles[i] <= 5:
            category1.append(name[i])
        elif enrolles[i] >= 5 and enrolles[i] <= 10:
            category2.append(name[i])
        elif enrolles[i] >= 10 and enrolles[i] <= 15:
            category3.append(name[i])

# display trainers in each category
def display_category(category1, category2, category3):
    print("Trainers in category 1")
    for i in range(len(category1)):
        print(category1[i])
    print("Trainers in category 2")
    for i in range(len(category2)):
        print(category2[i])
    print("Trainers in category 3")
    for i in range(len(category3)):
        print(category3[i])

def main():
    name = []
    enrolles = []
    category1 = []
    category2 = []
    category3 = []
    accept_input(name, enrolles)
    display(name, enrolles)
    categorize(name, enrolles, category1, category2, category3)
    display_category(category1, category2, category3)

if __name__ == "__main__":
    main()