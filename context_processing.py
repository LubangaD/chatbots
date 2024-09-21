
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def should_enrich_context(user_input):
    """
    Determines whether the input requires additional context enrichment.
    This can be based on specific keywords, length of the query, etc.
    """
    keywords_to_enrich = ['news', 'latest', 'update', 'information', 'current events', 'details', 'facts']
    for keyword in keywords_to_enrich:
        if keyword in user_input.lower():
            return True
    return False

def search_web(query):
    """
    Searches the web for additional context using Google Custom Search API.
    """
    api_key = "AIzaSyAjCjAfMI4CK5no_P6xF7GPWXVwjTmbGpA"  # Replace with your API key
    cx = "1445f2406662c475c"  # Replace with your Custom Search Engine ID

    try:
        service = build("customsearch", "v1", developerKey=api_key)
        result = service.cse().list(q=query, cx=cx).execute()

        # Return the snippet of the first result, if available
        if 'items' in result and len(result['items']) > 0:
            return result['items'][0]['snippet']
        else:
            return "No results found."
    
    except HttpError as e:
        return f"An error occurred during the API call: {e}"
    
    except Exception as e:
        return f"An unexpected error occurred: {e}"
