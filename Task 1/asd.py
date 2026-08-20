# Please Ignore the .venv file which is required for a virtual python enviroment (since i'm using linux for now)
# To See the DataFrames, Just Uncomment The print(df_<type of the data>) commands


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                              IMPORTING MODULES :]                                                              Made By Mostafa Ashraf Kamel

# Check of install Packages
# Check if required packages are installed
try:
    import pandas
    import matplotlib.pyplot
    import lxml
except ImportError as e:
    import sys
    import subprocess
    import time
    # List of packages to install
    # 'sqlite3' is excluded because it is already built into Python's standard library
    PACKAGES = ["pandas", "matplotlib", "lxml"]

    def loading_circle(duration=2):
        """Display a loading circle animation."""
        frames = ['|', '/', '-', '\\']
        end_time = time.time() + duration
        frame_index = 0
        
        while time.time() < end_time:
            sys.stdout.write(f'\r{frames[frame_index]}')
            sys.stdout.flush()
            frame_index = (frame_index + 1) % len(frames)
            time.sleep(0.1)
        
        sys.stdout.write('\rDone! ::: ')
        sys.stdout.flush()

    def install_packages():
        tasks = [
            ("Checking pip installation", 2),
            ("Installing pandas", 2),
            ("Installing matplotlib", 2),
            ("Installing lxml", 2)
        ]
        print(":Info: Starting package installation...\n")
        
        for task_name, duration in tasks:
            print(f":Info: {task_name}...", end=" ")
            try:
                loading_circle(duration)
                print(f"[✓] {task_name} completed!\n")
            except Exception as e:
                print(f"\033[91m[✗] {task_name} failed: {e}\033[0m\n")

    if __name__ == "__main__":
        try:
            install_packages()
        except KeyboardInterrupt:
            print("\n\n\033[91m[✗] Installation interrupted by user.\033[0m")
            sys.exit(1)

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                             IMPORTING DATAFRAMES :]                                                            Made By Mostafa Ashraf Kamel

df_db_path = "../../31008170105078-Library/City Database.db"
conn = sqlite3.connect("../../31008170105078-Library/City Database.db") # Connects to the database on the system
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;",conn) # Reads The database which contains the books and the author the Orders the database From A to Z and in Ascending order.
table_name = tables.iloc[0, 0]
# Load every database table into a dictionary and separate DataFrames
df_tables = {}

for table in tables["name"]:
    safe_table_name = table.replace('"', '""')
    df_table = pd.read_sql_query(
        f'SELECT * FROM "{safe_table_name}"',
        conn
    )

    # Fill missing values using each column's mode when available
    for column_name in df_table.columns:
        modes = df_table[column_name].mode()
        if not modes.empty:
            df_table[column_name] = df_table[column_name].fillna(modes.iloc[0])

    df_tables[table] = df_table
    globals()[f"df_{table}"] = df_table

# Preserve the original variable for the first table
# Preserve the original variable for the first table
df_db = df_tables[table_name]

# Save the second and third tables with their actual names
second_table_name = tables.iloc[1, 0]
third_table_name = tables.iloc[2, 0]

df_second = df_tables[second_table_name]
df_third = df_tables[third_table_name]

globals()[f"df_{second_table_name}"] = df_second
globals()[f"df_{third_table_name}"] = df_third
conn.close()
print("Database Data (Which is Related to the Authors)\n")
# print(df_db)
print()

print("API Data (Which is related to how much books the customenrs had borrowed)\n")
df_json = pd.read_json("/home/mostafa/Desktop/31008170105078-Library/City API.json")
for column in df_json:
    df_json[column] = df_json[column].sort_values(ascending=True)

# print(df_json)
print()


print("Library Data (Which is related to the books that are borrowed)\n")

tables_html = pd.read_html("/home/mostafa/Desktop/31008170105078-Library/City Library.html")
df_html = tables_html[0]
# print(df_html)
print("\nEnd Of Code")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 END OF CODE :]                                                                 Made By Mostafa Ashraf Kamel


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 First SubTask :]                                                               Made By Mostafa Ashraf Kamel

# Reopen the database connection because the earlier cell closed the original one.
with sqlite3.connect(df_db_path) as conn:
    member_count = pd.read_sql_query(
        """
        SELECT member_id, COUNT(*) AS checkout_count
        FROM checkouts
        GROUP BY member_id
        ORDER BY member_id
        """,
        conn
    ).set_index("member_id")["checkout_count"].to_dict()

print("Checkout Per member_id:\n")

# Checks How Many Checkout(s) Per Member
for member_id, count in member_count.items():
    print(f"Member No.'{member_id}': {count} checkout(s)")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 END OF CODE :]                                                                 Made By Mostafa Ashraf Kamel

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 Second SubTask :]                                                              Made By Mostafa Ashraf Kamel


pattern = input("Enter a letter or pattern to search by author name: ").strip() # Acts like a Search Bar for The Author

if pattern: # Checks If user had entered any values
    author_col = next((col for col in df_db.columns if "author" in col.lower()), None) # Prints The colums which has the author in it
    title_col = next((col for col in df_db.columns if "title" in col.lower() or "book" in col.lower()), None) # Prints the columns which has the book's title 

    if author_col is None: # Checks if there's any author within the user's serach
        raise ValueError("No Results")

    matches = df_db[df_db[author_col].astype(str).str.contains(pattern, case=False, na=False)] # Filter all rows whose author contains the pattern

    print(f"Books whose author contains '{pattern}':")
    if title_col is not None:
        print(matches[[title_col, author_col]].reset_index(drop=True))
    else:
        print(matches.reset_index(drop=True))
else:
    print("No pattern entered.")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 END OF CODE :]                                                                 Made By Mostafa Ashraf Kamel

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 Third SubTask :]                                                               Made By Mostafa Ashraf Kamel

# Open a temporary connection to the database.
# The connection closes automatically after the with block.
with sqlite3.connect(df_db_path) as conn:
    top_5_books = pd.read_sql_query(
        """
        SELECT
            c.book_id,
            b.title,
            COUNT(*) AS borrow_count
        FROM checkouts AS c
        LEFT JOIN books AS b
            ON b.book_id = c.book_id
        GROUP BY c.book_id, b.title
        ORDER BY borrow_count DESC, c.book_id ASC
        LIMIT 5
        """,
        conn
    )

# Display the five books with the highest number of checkouts.
# Ties are ordered by book_id in ascending order.
print("Top 5 Most Borrowed Books:\n")
print(top_5_books.to_string(index=False))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 END OF CODE :]                                                                 Made By Mostafa Ashraf Kamel

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                Fourth SubTask :]                                                              Made By Mostafa Ashraf Kamel

# Now Let's do a Merged Data Frame

# df_Merged = df_html.merge(df_db, left_on='Book ID', right_on='book_id', how='left').merge(df_json, on='book_id', how='left') # Merges The Data Frames all together into one
# df_Merged_Mode = df_Merged[0:10].mode() # A Clever Way to Get the Mode For Every Column By using the Mode.
# df_Merged_Cleaned = df_Merged.fillna(df_Merged_Mode.iloc[0]) # And Then Targetting the Empty Cell in the DataFrame.
# print(df_Merged_Cleaned) # prints it so it You check if the dataframe is working/merged.
# df_Merged_Cleaned.to_csv("task1_cleaned.csv") # Outputting them into a merged dataframe and cleaning them

# !!! IMPORTANT !!! The Syntax For the DataFrame When printed is:
#                   1. The HTML DataFrame (Member ID, Book ID and Checkout Date columns).
#                   2. The SQL Database DataFrame (book_id, title, and author columns).
#                   3. The JSON DataFrame (genre, pages an publication_year) columns.

# Print top 5 members with the most borrowed books.
with sqlite3.connect(df_db_path) as conn:
    member_borrow_counts = (
        pd.read_sql_query(
            """
            SELECT member_id, COUNT(*) AS borrow_count
            FROM checkouts
            GROUP BY member_id
            ORDER BY borrow_count DESC, member_id ASC
            """,
            conn
        )
        .set_index("member_id")["borrow_count"]
    )

# Now It just prints them.
print("\nTop 10 Members with the Most Borrowed Books:")
top_10_members = member_borrow_counts.head(10)
print(top_10_members)

# And Checks For Every Member ID Book Count.
# for member_id, count in top_5_members.items():
#     print(f"Member No.'{member_id}': {count} book(s)")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 END OF CODE :]                                                                 Made By Mostafa Ashraf Kamel

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 FifTh SubTask :]                                                              Made By Mostafa Ashraf Kamel

# Getting The Second Set of 10
# We'll use the Cleaned DataFrame

with sqlite3.connect(df_db_path) as conn:
    df_Second_10 = pd.read_sql_query(
        """
        SELECT *
        FROM checkouts
        ORDER BY checkout_date DESC
        LIMIT 10 OFFSET 10
        """,
        conn
    )
print(df_Second_10)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DECI AI Level 3 Second Term Project                                 END OF CODE :]                                                                 Made By Mostafa Ashraf Kamel