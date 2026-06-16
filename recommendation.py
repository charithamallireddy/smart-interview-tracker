def recommend_topic():
    solved = int(input("How many total problems have you solved? "))

    if solved < 20:
        print("Recommended topic: Arrays")
    elif solved < 40:
        print("Recommended topic: Strings")
    else:
        print("Recommended topic: Dynamic Programming")