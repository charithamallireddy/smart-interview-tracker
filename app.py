from analytics import show_progress
from recommendation import recommend_topic
from db import view_history

while True:
    print("\nMenu:")
    print("1. View Progress")
    print("2. Get Recommendation")
    print("3. View History")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_progress()

    elif choice == "2":
        recommend_topic()

    elif choice == "3":
        view_history()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")