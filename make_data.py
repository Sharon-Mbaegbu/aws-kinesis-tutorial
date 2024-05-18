import pandas as pd
import json
# Reading our data

romance_books = pd.read_csv('rom.csv')

new_book = pd.read_csv('book.csv')
new_book.rename(columns={'title': 'Title', 'author': 'Author(s)', 'price': 'Price', 'description': 'Description'}, inplace=True)

books = [romance_books, new_book]
amazon_books = pd.concat([romance_books, new_book], ignore_index=True)

# Convert DataFrame to a list of dictionaries
amazon_books_list = amazon_books.to_dict(orient='records')

# Convert the list of dictionaries to a JSON-formatted string
amazon_books_json_str = json.dumps(amazon_books_list, indent=2)

# Wrap the entire JSON data in square brackets
amazon_books_json_final = f'[{amazon_books_json_str}]'

# Saving the formatted JSON data to a file
json_file_path = 'amazon_books200.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(amazon_books_json_final)
