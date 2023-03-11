# Library
import sqlite3

db = sqlite3.connect("python_programming")
cursor = db.cursor()

try:
    cursor.execute("""
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
    """)
    db.commit()
    print("\nTable created")
except:
    print("\nTable already created")

# Fill table
try:
    # Student 1
    id1 = 55
    name1 = "Carl Davis"
    grade1 = 61

    # Student 2
    id2 = 66
    name2 = "Dennis Fredrickson"
    grade2 = 88

    # Student 3
    id3 = 77
    name3 = "Jane Richards"
    grade3 = 78

    # Student 4
    id4 = 12
    name4 = "Peyton Sawyer"
    grade4 = 45

    # Student 5
    id5 = 2
    name5 = "Lucas Brooke"
    grade5 = 99

    # Insert student data into table
    cursor.execute("""INSERT INTO python_programming(id, name, grade)
    VALUES (?,?,?)""",
    (id1, name1, grade1))

    cursor.execute("""INSERT INTO python_programming(id, name, grade)
    VALUES (?,?,?)""",
    (id2, name2, grade2))

    cursor.execute("""INSERT INTO python_programming(id, name, grade)
    VALUES (?,?,?)""",
    (id3, name3, grade3))

    cursor.execute("""INSERT INTO python_programming(id, name, grade)
    VALUES (?,?,?)""",
    (id4, name4, grade4))

    cursor.execute("""INSERT INTO python_programming(id, name, grade)
    VALUES (?,?,?)""",
    (id5, name5, grade5))
    db.commit()
    print("\nStudents added to table")    
except:
    print("\nUnable to add data to table")


# Selects all records between 60 and 90
try:
    cursor.execute("""SELECT id, name, grade FROM python_programming WHERE grade > ? AND grade < ? """, (59,90))
    a = cursor.fetchall()
    print("\nAll records with grades between 60 and 90\n")
    for student in a:
        print(student)
except:
    print("\nIt is not possible to select all records between 60 and 90")

# Changes Carl Davis's grade to 65
try:
    name="Carl Davis"
    grade_change=65
    cursor.execute("""UPDATE python_programming SET grade = ? WHERE name= ? """, (grade_change,name))
    db.commit()
    print("\nCarl Davis's grade changed to 65")
except:
    print("\nIt is not possible to change Carl Davis's grade to 65")

# Delete Dennis Fredrickson's row
try:
    del_name="Dennis Fredrickson"
    cursor.execute("""DELETE FROM python_programming WHERE name= ? """, (del_name,))
    db.commit()
    print("\nDennis Fredrickson's data removed")
except:
    print("\nIt is not possible to delete Dennis Fredrickson's row")

## Changes grade to 65 for all people with id below 55
try:    
    id=55
    grade_change=65
    cursor.execute("""UPDATE python_programming SET grade = ? WHERE id< ? """, (grade_change,id))
    db.commit()
    print("\nGrade changed to 65 for all people with id below 55")
except:
    print("\nIt is not possible to changes grade to 65 for all people with id below 55")

finally:
    db.close()
