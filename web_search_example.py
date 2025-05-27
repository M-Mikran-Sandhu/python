import requests
from bs4 import BeautifulSoup

def get_google_title(search_term):
    """
    Searches Google for a term and returns the title of the first result page.
    Note: This is a simplified example and might be blocked by Google 
    if used excessively without proper headers or more sophisticated methods.
    Google's terms of service should be respected.
    """
    try:
        url = f"https://www.google.com/search?q={search_term}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Attempt to find the title of the page
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.string
        else:
            return "Title not found"

    except requests.exceptions.RequestException as e:
        return f"Error during request: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    search_query = "python programming"
    print(f"Searching Google for: '{search_query}'")
    title = get_google_title(search_query)
    print(f"Page Title: {title}")

    search_query_no_results = "supercalifragilisticexpialidociousnonexistentterm"
    print(f"
Searching Google for: '{search_query_no_results}'")
    title_no_results = get_google_title(search_query_no_results)
    print(f"Page Title: {title_no_results}")
