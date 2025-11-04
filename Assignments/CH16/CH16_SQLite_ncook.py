"""
===========================================================
Program Name: Ingredient/Meal tool
Author: Noah Cook   
Date: 11/4/25
Description:
    This program performs a check on a users input and returns a meal or ingredient list of a meal.
    It is designed to tell the user what meals have what ingredients.
    
Usage:
    Run the script using Python 3.9. Ensure all dependencies
    are installed before execution.

===========================================================
"""

import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('meals.db', isolation_level=None)
cursor = conn.cursor()

# Create the tables
cursor.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT')
cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (name TEXT,
                  meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals
                  (rowid)) STRICT''')

# Main program loop
while True:
    user_input = input('> ')
    
    # Check if user wants to quit
    if user_input == 'quit':
        break
    
    # Check if user is adding a new meal (contains a colon)
    if ':' in user_input:
        # Split the meal name and ingredients
        meal_name, ingredients_str = user_input.split(':', 1)
        
        # Insert the meal into meals table
        cursor.execute('INSERT INTO meals (name) VALUES (?)', (meal_name,))
        meal_id = cursor.lastrowid  # Get the rowid of the meal we just inserted
        
        # Split ingredients by comma and insert each one
        ingredients_list = ingredients_str.split(',')
        for ingredient in ingredients_list:
            cursor.execute('INSERT INTO ingredients (name, meal_id) VALUES (?, ?)',
                         (ingredient, meal_id))
        
        print(f'Meal added: {meal_name}')
    
    else:
        # User is searching for a meal or ingredient
        search_term = user_input
        
        # First, check if it's a meal name
        cursor.execute('SELECT rowid FROM meals WHERE name = ?', (search_term,))
        meal_results = cursor.fetchall()
        
        if meal_results:
            # It's a meal! Show its ingredients
            meal_id = meal_results[0][0]
            cursor.execute('SELECT name FROM ingredients WHERE meal_id = ?', (meal_id,))
            ingredients = cursor.fetchall()
            
            print(f'Ingredients of {search_term}:')
            for ingredient in ingredients:
                print(f'  {ingredient[0]}')
        
        else:
            # Check if it's an ingredient
            cursor.execute('SELECT meal_id FROM ingredients WHERE name = ?', (search_term,))
            ingredient_results = cursor.fetchall()
            
            if ingredient_results:
                # It's an ingredient! Show all meals that use it
                print(f'Meals that use {search_term}:')
                for result in ingredient_results:
                    meal_id = result[0]
                    cursor.execute('SELECT name FROM meals WHERE rowid = ?', (meal_id,))
                    meal_names = cursor.fetchall()
                    print(f'  {meal_names[0][0]}')
            else:
                # Not found in either table
                print(f'"{search_term}" not found in meals or ingredients.')

# Close the database connection
conn.close()
