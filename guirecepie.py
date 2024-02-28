import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

class RecipeAppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Recipe App")

        self.recipes = {}
        self.note_filename = "recipe_notes.txt"

        self.create_widgets()

    def create_widgets(self):
        self.master.configure(bg='light green')
        # Recipe Name
        self.recipe_name_label = tk.Label(self.master, text="Recipe Name:", font=("Times New Roman", 12), bg='light grey')
        self.recipe_name_label.grid(row=0, column=0, sticky="e")
        self.recipe_name_entry = tk.Entry(self.master, font=("Times New Roman", 12))
        self.recipe_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Ingredients
        self.ingredients_label = tk.Label(self.master, text="Ingredients:", font=("Times New Roman", 14), bg='light grey')
        self.ingredients_label.grid(row=1, column=0, sticky="e")
        self.ingredients_entry = tk.Entry(self.master, font=("Times New Roman", 12))
        self.ingredients_entry.grid(row=1, column=1, padx=5, pady=5)

        # Instructions
        self.instructions_label = tk.Label(self.master, text="Instructions:", font=("Times New Roman", 14), bg='light grey')
        self.instructions_label.grid(row=2, column=0, sticky="e")
        self.instructions_entry = tk.Text(self.master, height=5, width=30, font=("Times New Roman", 12))
        self.instructions_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(self.master, text="Add Recipe", command=self.add_recipe, font=("Arial", 12), bg="green", fg="white")
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self.master, text="View Recipe", command=self.view_recipe, font=("Arial", 12), bg="green", fg="white")
        self.view_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.search_button = tk.Button(self.master, text="Search Recipe", command=self.search_recipe, font=("Arial", 12), bg="green", fg="white")
        self.search_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.notebook_button = tk.Button(self.master, text="Open Notebook", command=self.open_notebook, font=("Arial", 12), bg="green", fg="white")
        self.notebook_button.grid(row=6, column=0, columnspan=2, pady=5)

    def add_recipe(self):
        name = self.recipe_name_entry.get()
        ingredients = self.ingredients_entry.get()
        instructions = self.instructions_entry.get("1.0", tk.END)

        self.recipes[name] = {'ingredients': ingredients, 'instructions': instructions}

        messagebox.showinfo("Success", "Recipe added successfully!")

        # Clear the input fields after adding the recipe
        self.recipe_name_entry.delete(0, tk.END)
        self.ingredients_entry.delete(0, tk.END)
        self.instructions_entry.delete("1.0", tk.END)

    def view_recipe(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("All Recipes")

        if self.recipes:
            text_area = scrolledtext.ScrolledText(view_window, width=40, height=10, wrap=tk.WORD, font=("Arial", 12))
            text_area.grid(row=0, column=0, padx=10, pady=10)

            for name, recipe in self.recipes.items():
                text_area.insert(tk.END, f"Recipe: {name}\nIngredients: {recipe['ingredients']}\nInstructions: {recipe['instructions']}\n\n")
        else:
            no_recipes_label = tk.Label(view_window, text="No recipes available.", font=("Arial", 12))
            no_recipes_label.grid(row=0, column=0, padx=10, pady=10)

    def search_recipe(self):
        keyword = self.recipe_name_entry.get()
        found_recipes = []
        for name, recipe in self.recipes.items():
            if keyword.lower() in name.lower():
                found_recipes.append(name)
        if found_recipes:
            messagebox.showinfo("Search Result", f"Found {len(found_recipes)} recipes containing '{keyword}':\n{', '.join(found_recipes)}")
        else:
            messagebox.showerror("Error", "No recipes found containing the keyword.")

    def open_notebook(self):
        notebook_window = tk.Toplevel(self.master)
        notebook_window.title("Recipe Notebook")

        text_area = scrolledtext.ScrolledText(notebook_window, width=40, height=10, wrap=tk.WORD, font=("Arial", 12))
        text_area.grid(row=0, column=0, padx=10, pady=10)

        # Load notes from file if it exists
        if os.path.exists(self.note_filename):
            with open(self.note_filename, 'r') as f:
                notes = f.read()
                text_area.insert(tk.END, notes)

        # Save note to file function
        def save_note():
            with open(self.note_filename, 'w') as f:
                notes = text_area.get("1.0", tk.END)
                f.write(notes)
            messagebox.showinfo("Success", "Note saved successfully!")

        # Button to save note
        save_button = tk.Button(notebook_window, text="Save Note", command=save_note, font=("Arial", 12), bg="green", fg="white")
        save_button.grid(row=1, column=0, pady=5)

def main():
    root = tk.Tk()
    app = RecipeAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
