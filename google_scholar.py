from scholarly import scholarly

def get_author_info_on_terminal(author_id):
    # Search for the author's detailed info by ID
    author_info = scholarly.search_author_id(author_id)
    
    if author_info:
        # Fetch the complete author information
        author_info = scholarly.fill(author_info)
        
        # Print the author's details to the terminal
        print("Author Information:")
        print(f"Author Name: {author_info.get('name', 'No name')}")
        print(f"Affiliation: {author_info.get('affiliation', 'No affiliation')}")
        print(f"Interests: {', '.join(author_info.get('interests', []))}")
        print(f"Scholar ID: {author_info.get('scholar_id', 'No ID')}")
        print(f"H-index: {author_info.get('hindex', 'No h-index')}")
        print(f"Total Citations: {author_info.get('citedby', 'No citation count')}")
        print("\nPublications:")

        # Sort publications by year, handling missing or non-integer years
        sorted_publications = sorted(
            author_info['publications'],
            key=lambda x: int(x.get('bib', {}).get('pub_year', 9999))  # Use 9999 for missing years
        )

        # Print each publication's details to the terminal
        for pub in sorted_publications:
            title = pub.get('bib', {}).get('title', 'No title available')
            year = pub.get('bib', {}).get('pub_year', 'No year available')
            citations = pub.get('num_citations', 'No citation count available')
            
            print(f"- Title: {title}")
            print(f"  Year: {year}")
            print(f"  Citations: {citations}")
        
    else:
        print("Author not found.")

# Example usage
get_author_info_on_terminal("T4Uue_EAAAAJ")
