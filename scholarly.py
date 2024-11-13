from scholarly import scholarly

def get_author_info(author_name):
    # Search for the author by name
    search_query = scholarly.search_author(author_name)
    
    # Get the first author in the search results
    author = next(search_query, None)
    
    if author:
        # Fetch the complete author information
        author = scholarly.fill(author)

        # Print author's h-index and total citations
        print(f"Author: {author['name']}")
        print(f"H-index: {author['hindex']}")
        print(f"Total Citations: {author['citedby']}")
        print("\nPublished Documents (in chronological order):")

        # Sort publications by year, handling missing or non-integer years
        sorted_publications = sorted(
            author['publications'],
            key=lambda x: int(x.get('bib', {}).get('pub_year', 9999))  # Use 9999 for missing years
        )

        # Print detailed information for each publication
        for pub in sorted_publications:
            title = pub.get('bib', {}).get('title', 'No title available')
            year = pub.get('bib', {}).get('pub_year', 'No year available')
            citations = pub.get('num_citations', 'No citation count available')
            
            print(f"- {title}")
            print(f"  Year: {year}")
            print(f"  Citations: {citations}")
            print()
    else:
        print("Author not found.")

# Replace 'Pallavi Dhade' with the author's name you're interested in
get_author_info("Pallavi Dhade")

