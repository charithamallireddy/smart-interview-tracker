import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="charitha@18@",   # Your MySQL password
    database="interview_tracker"
)

# Save progress into database
def save_progress(solved_count, confidence):
    cursor = conn.cursor()

    query = """
    INSERT INTO progress (solved_count, confidence_score)
    VALUES (%s, %s)
    """

    cursor.execute(query, (solved_count, confidence))
    conn.commit()
    print("Data saved successfully!")

# Show all saved history
def view_history():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM progress")
    rows = cursor.fetchall()
    return rows