import re

def design_text(text):
    designed_text = text

    # Extract emails using regex
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, designed_text)

    # Remove emails from the text
    for email in emails:
        designed_text = designed_text.replace(email, '')

    # Remove extra whitespaces and format text
    designed_text = " ".join(designed_text.split())
    designed_text = designed_text.replace("\\n", "\n")

    # Add a prefix to indicate formatted text
    designed_text = "Formatted Text: " + designed_text

    return designed_text

def main():
    text = input("Enter the text: ")
    formatted_text = design_text(text)
    print(formatted_text)

if __name__ == "__main__":
    main()
