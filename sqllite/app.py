import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Create the Employee table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employee (
    emp_ssn INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    emp_category TEXT NOT NULL,
    gross_sal REAL NOT NULL,
    basic_sal REAL NOT NULL
)
''')

# Insert sample data into the Employee table
cursor.execute('''INSERT INTO Employee (emp_ssn, emp_name, emp_category, gross_sal, basic_sal)
                  VALUES (1, 'Alice', 'A', 10000, 8000)''')
cursor.execute('''INSERT INTO Employee (emp_ssn, emp_name, emp_category, gross_sal, basic_sal)
                  VALUES (2, 'Bob', 'B', 9000, 7000)''')
cursor.execute('''INSERT INTO Employee (emp_ssn, emp_name, emp_category, gross_sal, basic_sal)
                  VALUES (3, 'Charlie', 'C', 8000, 6000)''')

# Commit the changes
conn.commit()

print("Table created and data inserted successfully.")

# Close the database connection
conn.close()
