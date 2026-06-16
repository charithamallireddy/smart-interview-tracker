from db import save_progress

def show_progress():
    solved = int(input("How many problems solved? "))
    confidence = int(input("Confidence score (1-10): "))

    save_progress(solved, confidence)