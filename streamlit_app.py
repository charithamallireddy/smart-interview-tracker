import streamlit as st
from db import save_progress, view_history

# Title
st.title("Smart Interview Tracker")

# Input fields
solved = st.number_input("Problems Solved", min_value=0, step=1)
confidence = st.slider("Confidence Score", 1, 10)

# Save Progress Button
if st.button("Save Progress"):
    save_progress(solved, confidence)
    st.success("Data Saved!")

    # Recommendation
    if solved < 20:
        st.info("Recommended Topic: Arrays")
    elif solved < 40:
        st.info("Recommended Topic: Strings")
    else:
        st.info("Recommended Topic: Dynamic Programming")

# View History Button
if st.button("View History"):
    rows = view_history()
    
    st.write("## Saved History")
    
    for row in rows:
        st.write(f"ID: {row[0]} | Solved: {row[3]} | Confidence: {row[4]}/10")