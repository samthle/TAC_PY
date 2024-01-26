import re

def design_text(text):
    designed_text = text
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, designed_text)
    for email in emails:
        designed_text = designed_text.replace(email, '')  
    designed_text = " ".join(designed_text.split())
    designed_text = designed_text.replace("\\n", "\n")
    designed_text = "Formatted Text: " + designed_text
    return designed_text

text = input()
text_nahayee = design_text(text)
print(text_nahayee)

