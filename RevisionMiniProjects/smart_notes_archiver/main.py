import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

NOTES_DIR = os.path.join(BASE_DIR, "notes")
ARCHIVE_DIR = os.path.join(BASE_DIR, "archive")

def save_to_archive(category, title, content):
    today_date = datetime.now().strftime("%Y-%m-%d")

    archive_file = today_date + ".txt"
    archive_path = os.path.join(ARCHIVE_DIR, archive_file)

    try:
        with open(archive_path, "a") as file:
            file.write("\n")
            file.write("==========\n")
            file.write(f"Category: {category}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Content: {content}\n")
            file.write("==========\n")

    except Exception as e:
        print("Error while saving archive:", e)

def show_categories():      #helper function
    category_list = os.listdir(NOTES_DIR)
    print("Available categories:")
    for i in range(len(category_list)):
        print(i + 1, ":", category_list[i])

def add_note():
    show_categories()

    category = input("Enter category of note: ").lower().strip()
    title = input("Enter title of note: ").lower().strip()
    content = input("Enter note content: ")

    category_path =os.path.join(NOTES_DIR, category)

    #creating category folder if folder does'nt exist
    if not os.path.exists(category_path):
        os.makedirs(category_path)

    filename = title + ".txt"
    file_path = os.path.join(category_path, filename)

    try:
        with open(file_path,'w') as file:
            file.write(content)

        save_to_archive(category, title, content)
        print("Notes saved successfully")

    except Exception as e:
        print("Error while saving note:",e)

def view_note():
    show_categories()

    chosen_category = input("Enter category: ").strip().lower()
    category_path = os.path.join(NOTES_DIR, chosen_category)
   
    notes_list = os.listdir(category_path)
    print(f"\nNotes in {chosen_category}:")

    for note in notes_list:
        print(note)

    chosen_note = input("Enter note to view:").strip()
    if not chosen_note.endswith(".txt"):
        chosen_note += ".txt"
    file_path = os.path.join(category_path, chosen_note)

    try:
        with open(file_path,'r') as file:
                    content = file.read()

        print("------VIEW YOUR NOTE-----")
        print(content)

    except FileNotFoundError:
        print("Note not found.")

def search_note():
    found = False
    keyword = input("Enter keyword to search: ").strip().lower()
    categories = os.listdir(NOTES_DIR)

    for category in categories:
        category_path = os.path.join(NOTES_DIR, category)
        notes = os.listdir(category_path)
        for note in notes:
            file_path = os.path.join(category_path, note)
            with open(file_path, "r") as file:
                content = file.read().lower()
            
            if keyword in content:
                found = True
                print(f"Match found in: {category}/{note}")
    if not found:
        print("No matching notes found.")
    

def menu():
    print("\n===== SMART NOTES ARCHIVER =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Exit")

while True:
    menu()
    choice = input("\n Enter your choice: ")

    if choice =="1":
        add_note()
        
    elif choice == "2":
       view_note()

    elif choice == "3":
        search_note()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")


