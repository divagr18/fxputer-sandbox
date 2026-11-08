import re


def slugify(text):
    """Convert text to a slug.
    
    Args:
        text: The text to convert to a slug.
        
    Returns:
        A slugified version of the text.
    """
    # Lowercase the text
    text = text.lower()
    # Replace every run of characters that are not a-z or 0-9 with a single hyphen
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Strip hyphens from both ends
    text = text.strip('-')
    return text
