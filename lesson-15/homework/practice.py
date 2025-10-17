# 1 & 2 Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field. Populate your new table with the following values:
import sqlite3

with sqlite3.connect("test_database.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS species (
            name TEXT,
            species TEXT,
            age INTEGER
        )
    """)
    
    cursor.execute("""
        INSERT INTO species (name, species, age) VALUES
            ('Benjamin Sisko', 'human', 40),
            ('Jadzia Dax', 'Trill', 300),
            ('Kira Nerys', 'Bajoran', 29)
    """)
    
    cursor.execute("SELECT * FROM species")
    rows = cursor.fetchall()
    print(rows)



# 3 Update the Name of Jadzia Dax to be Ezri Dax


import sqlite3

with sqlite3.connect("test_database.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS species (
            name TEXT,
            species TEXT,
            age INTEGER
        )
    """)
    
    cursor.execute("DELETE FROM species")
    
    cursor.execute("""
        INSERT INTO species (name, species, age) VALUES
            ('Benjamin Sisko', 'human', 40),
            ('Jadzia Dax', 'Trill', 300),
            ('Kira Nerys', 'Bajoran', 29)
    """)
    
    cursor.execute("""
        UPDATE species
        SET name = 'Ezri Dax'
        WHERE name = 'Jadzia Dax'
    """)
    
    cursor.execute("SELECT * FROM species")
    rows = cursor.fetchall()
    print(rows)


# 4 Display the Name and Age of everyone in the table classified as Bajoran.

import sqlite3

with sqlite3.connect("test_database.db") as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT name, age
        FROM species
        WHERE species = 'Bajoran'
    """)
    
    rows = cursor.fetchall()
    print(rows)


