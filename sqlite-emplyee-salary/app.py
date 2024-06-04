import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employee.db')  
cursor = conn.cursor()

# Create a single table for employees
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT,
    BasicSalary REAL,
    Category TEXT,
    TaxPercentage REAL,
    DearnessAllowancePercentage REAL
)
''')

# Insert data into Employees table
employees = [
    (1, 'John Doe', 50000.00, 'A', 30.00, 80.00),
    (2, 'Jane Smith', 40000.00, 'B', 20.00, 50.00),
    (3, 'Robert Brown', 30000.00, 'C', 10.00, 30.00)
]

cursor.executemany('''
INSERT OR IGNORE INTO Employees (EmployeeID, Name, BasicSalary, Category, TaxPercentage, DearnessAllowancePercentage) 
VALUES (?, ?, ?, ?, ?, ?)
''', employees)

# Display the contents of Employees table
cursor.execute('SELECT * FROM Employees')
employees_results = cursor.fetchall()
print("Employees Table:")
for row in employees_results:
    print(row)

# Compute the net salary for each employee
cursor.execute('''
SELECT 
    EmployeeID,
    Name,
    BasicSalary,
    Category,
    (BasicSalary + (BasicSalary * DearnessAllowancePercentage / 100)) AS GrossSalary,
    ((BasicSalary + (BasicSalary * DearnessAllowancePercentage / 100)) * TaxPercentage / 100) AS TaxDeducted,
    ((BasicSalary + (BasicSalary * DearnessAllowancePercentage / 100)) - ((BasicSalary + (BasicSalary * DearnessAllowancePercentage / 100)) * TaxPercentage / 100)) AS NetSalary
FROM 
    Employees
''')

# Fetch and display results
results = cursor.fetchall()
print("\nComputed Salaries:")
for row in results:
    print(f"Employee ID: {row[0]}, Name: {row[1]}, Basic Salary: {row[2]}, Category: {row[3]}, "
          f"Gross Salary: {row[4]:.2f}, Tax Deducted: {row[5]:.2f}, Net Salary: {row[6]:.2f}")

# Close the database connection
conn.close()
