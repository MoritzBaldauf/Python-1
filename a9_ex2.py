
import re

def extract_emails(text: str) -> list[str]:
    pattern = r'\s([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})' # Pattern for Email Addresses
    matches = re.findall(pattern, text)

    return matches

