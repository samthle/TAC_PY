def domain_emails(emails):
    domains = set()

    for email in emails:
        domain = email.split('@')[-1]
        domains.add(domain)

    return sorted(domains)

def main():
    n = int(input("Enter the number of emails: "))
    emails = []

    for _ in range(n):
        email = input("Enter an email: ")
        emails.append(email)

    for domain in domain_emails(emails):
        print(domain)

if __name__ == "__main__":
    main()
