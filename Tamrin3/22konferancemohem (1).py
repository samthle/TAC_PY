def domain_emails (emails):
    domains = set()
    for email in emails:
        domain = email.split('@')[-1] 
        domains.add(domain)  
    return sorted(domains) 
n = int(input())
emails = []
for _ in range(n):
    email = input()
    emails.append(email)
for domain in domain_emails(emails):
    print(domain)
