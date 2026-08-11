def main():
    library_catalog = {}

    while True:
        print("\n=== Library Book Catalog System ===")
        print("1. Add a New Book (Create)")
        print("2. Search for a Book (Read)")
        print("3. Update Book Details (Update)")
        print("4. Display All Books (Display)")
        print("5. Remove a Book (Delete)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\n--- Add New Book ---")
            book_id = input("Enter Book ID (e.g., BK-001): ")
            
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            
            genres_input = input("Enter genres (comma-separated, e.g., Sci-Fi, Adventure): ")
            genres_list = [genre.strip() for genre in genres_input.split(',')]
            
            pub_input = input("Enter Publication Year and Page Count (comma-separated, e.g., 2021, 350): ")
            try:
                pub_tuple = tuple(int(val.strip()) for val in pub_input.split(','))
                if len(pub_tuple) != 2:
                    print("Please enter exactly two numbers. Defaulting to (0, 0).")
                    pub_tuple = (0, 0)
            except ValueError:
                print("Invalid format. Defaulting to (0, 0)")
                pub_tuple = (0, 0)

            library_catalog[book_id] = {
                "title": title,
                "author": author,
                "genres": genres_list,
                "pub_details": pub_tuple
            }
            print(f"'{title}' added successfully!")

        elif choice == '2':
            print("\n--- Search Book ---")
            book_id = input("Enter Book ID to search: ")
            
            if book_id in library_catalog:
                book = library_catalog[book_id]
                print(f"\nRecord for Book ID: {book_id}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Genres: {', '.join(book['genres'])}")
                print(f"Publication Year: {book['pub_details'][0]} | Pages: {book['pub_details'][1]}")
            else:
                print("Error: Book not found in the catalog.")

        elif choice == '3':
            print("\n--- Update Book ---")
            book_id = input("Enter Book ID to update: ")
            
            if book_id in library_catalog:
                print("Note: Leave a field blank and press Enter to keep the current value.")
                
                current_title = library_catalog[book_id]['title']
                new_title = input(f"Enter new Title ({current_title}): ")
                
                current_author = library_catalog[book_id]['author']
                new_author = input(f"Enter new Author ({current_author}): ")
                
                current_genres = ", ".join(library_catalog[book_id]['genres'])
                new_genres = input(f"Enter new genres ({current_genres}): ")
                
                current_pub = f"{library_catalog[book_id]['pub_details'][0]}, {library_catalog[book_id]['pub_details'][1]}"
                new_pub = input(f"Enter new Year and Pages ({current_pub}): ")

                if new_title.strip():
                    library_catalog[book_id]['title'] = new_title.strip()
                    
                if new_author.strip():
                    library_catalog[book_id]['author'] = new_author.strip()
                
                if new_genres.strip():
                    library_catalog[book_id]['genres'] = [g.strip() for g in new_genres.split(',')]
                
                if new_pub.strip():
                    try:
                        parsed_tuple = tuple(int(val.strip()) for val in new_pub.split(','))
                        if len(parsed_tuple) == 2:
                            library_catalog[book_id]['pub_details'] = parsed_tuple
                        else:
                            print("Need exactly Year and Pages. Publication details unchanged.")
                    except ValueError:
                        print("Invalid format. Publication details remain unchanged.")
                
                print("Book record updated successfully!")
            else:
                print("Error: Book not found in the catalog.")

        elif choice == '4':
            print("\n--- All Books in Catalog ---")
            if not library_catalog:
                print("The catalog is currently empty.")
            else:
                for b_id, data in library_catalog.items():
                    print(f"ID: {b_id} | Title: '{data['title']}' by {data['author']} | Genres: {data['genres']} | (Year, Pages): {data['pub_details']}")

        elif choice == '5':
            print("\n--- Remove Book ---")
            book_id = input("Enter Book ID to remove: ")
            
            if book_id in library_catalog:
                removed_book = library_catalog.pop(book_id)
                print(f"Success: '{removed_book['title']}' has been removed from the catalog.")
            else:
                print("Error: Book not found.")

        elif choice == '6':
            print("Closing the Library Catalog System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()