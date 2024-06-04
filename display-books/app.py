import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('library.db')  
cursor = conn.cursor()

# Create Books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER PRIMARY KEY,
    name TEXT,
    total_count INTEGER
)
''')

# Insert initial data into Books table
books = [
    (34, 'King', 5),
    (123, 'Harry Potter', 3)
]

cursor.executemany('''
INSERT OR IGNORE INTO Books (id, name, total_count) 
VALUES (?, ?, ?)
''', books)

# Function to borrow a book
def borrow_book(book_id):
    cursor.execute('SELECT total_count FROM Books WHERE id = ?', (book_id,))
    result = cursor.fetchone()
    if result:
        total_count = result[0]
        if total_count > 0:
            cursor.execute('UPDATE Books SET total_count = total_count - 1 WHERE id = ?', (book_id,))
            conn.commit()
            print(f"Borrowed book with ID {book_id}.")
        else:
            print(f"No copies left to borrow for book ID {book_id}.")
    else:
        print(f"Book ID {book_id} not found.")

# Function to return a book
def return_book(book_id):
    cursor.execute('SELECT total_count FROM Books WHERE id = ?', (book_id,))
    result = cursor.fetchone()
    if result:
        cursor.execute('UPDATE Books SET total_count = total_count + 1 WHERE id = ?', (book_id,))
        conn.commit()
        print(f"Returned book with ID {book_id}.")
    else:
        print(f"Book ID {book_id} not found.")

# Display the contents of Books table
def display_books():
    cursor.execute('SELECT * FROM Books')
    books_results = cursor.fetchall()
    print("Books Table:")
    for row in books_results:
        print(row)

# Test the functions
display_books()
borrow_book(34)
borrow_book(123)
return_book(34)
display_books()

# Close the database connection
conn.close()
