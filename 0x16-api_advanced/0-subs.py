import json

def number_of_subscribers_from_file(subreddit_file):
    """
    Return the total number of subscribers on a given subreddit from a local file.

    Args:
        subreddit_file (str): The path to the JSON file containing subreddit information.

    Returns:
        int: The total number of subscribers, or 0 if the subreddit is invalid or file read fails.
    """
    try:
        # Open the file in read mode
        with open(subreddit_file, 'r') as file:
            # Load JSON data from the file
            data = json.load(file)
            # Get the total number of subscribers
            subscribers = data.get("data").get("subscribers")
            return subscribers
    except FileNotFoundError:
        # If the file is not found, return 0
        return 0
    except json.JSONDecodeError:
        # If JSON decoding fails, return 0
        return 0
