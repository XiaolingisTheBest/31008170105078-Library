<p align="center">
    <img width="900" height="900" alt="image" src="https://github.com/user-attachments/assets/93b536c2-cb77-4699-b088-ef77df338807" />
</p>

<p align="center">
░▒█▀▀▄░▒█▀▀▀░▒█▀▀▄░▀█▀░░░█▀▀▄░▀█▀░░░▒█░░░░█▀▀░▄░░░▄░█▀▀░█░░░░█▀▀█
░▒█░▒█░▒█▀▀▀░▒█░░░░▒█░░░▒█▄▄█░▒█░░░░▒█░░░░█▀▀░░█▄█░░█▀▀░█░░░░░▒▀▄
░▒█▄▄█░▒█▄▄▄░▒█▄▄▀░▄█▄░░▒█░▒█░▄█▄░░░▒█▄▄█░▀▀▀░░░▀░░░▀▀▀░▀▀░░░█▄▄█
</p>

## Project Overview

This project analyzes a library database using SQL and Python data-processing techniques.
It focuses on library members, books, authors, and checkout transactions.

## Objectives

- Compare web pages and databases as data sources.
- Count checkouts for each library member.
- Find books written by authors whose names contain the letter `h`.
- Identify the five most borrowed books.
- Identify members with the highest number of borrowed books.
- Retrieve a selected set of recent checkout records.
- Clean duplicate records from the database tables.

## Data Cleaning

The database contained 383 checkout records after cleaning. Eight duplicate rows were
removed from the checkouts table. No duplicate rows were found in the books or members
tables.

## Results

The analysis produced checkout totals by member, filtered books by author name, the top
five most borrowed books, the top ten borrowing members, and the second set of ten most
recent checkout records.

## Technologies

- SQL for querying and aggregating relational data
- Python and pandas for data cleaning and analysis
- Text-based result documentation

## Project Structure
```
    31008170105078-Library/
    ╠═ City_API.json — city data source
    ╠═ City_Database.db — library database
    ╠═ City_Library.html — library web page
    ╠═ Task_1/
    ║  ╠═ 31008170105078-Library .ipynb — Python analysis notebook
    ║  ╚═ task1_sql_answers.txt — SQL analysis results and project documentation
    ╚═ Task_2/
        ╚═ task2_cleaned_data.csv — cleaned data output
```
## Conclusion

Relational databases provide structured, consistent, and efficient access to library
data. SQL queries combined with data cleaning make it possible to generate reliable
borrowing statistics and support library management decisions.
