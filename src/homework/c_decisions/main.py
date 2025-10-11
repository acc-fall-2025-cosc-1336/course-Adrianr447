from src.homework.c_decisions.decisions import get_letter_grade, get_letter_grade_switch

def main():
    print("MAIN MENU\n")
    print("1-Letter grade using if")
    print("2-Letter grade using switch")
    print("3-Exit")
    choice = input("\nEnter your choice: ")
    if choice == '1':
        try:
            num = int(input("Enter a numerical grade (0-100): "))
            if 0 <= num <= 100:
                print(f"Letter grade: {get_letter_grade(num)}")
            else:
                print("Number is out of range.")
        except ValueError:
            print("Invalid input.")
    elif choice == '2':
        try:
            num = int(input("Enter a numerical grade (0-100): "))
            if 0 <= num <= 100:
                print(f"Letter grade: {get_letter_grade_switch(num)}")
            else:
                print("Number is out of range.")
        except ValueError:
            print("Invalid input.")
    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid menu option.")

if __name__ == "__main__":
    main()