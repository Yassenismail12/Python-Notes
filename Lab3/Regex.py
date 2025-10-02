import re
from Decorators import log_time

def create_fake_log_file():
    fake_logs = [
        "2025-10-02 10:15:32 User john.doe@example.com accessed page /home",
        "2025-10-02 10:16:45 Invalid user admin@@ tried to login",
        "2025-10-02 10:18:12 User sarah_smith@company.org successfully authenticated",
        "2025-10-02 10:20:33 Failed login from user@invalid",
        "2025-10-02 10:22:54 User mike.wilson@subdomain.example.com downloaded file report.pdf",
        "2025-10-02 10:25:17 User notanemail accessed resource /api/data",
        "2025-10-02 10:27:42 User emma.jones123@test-server.co.uk updated profile",
        "2025-10-02 10:30:05 Malformed request from user@@domain.com",
        "2025-10-02 10:32:28 User contact@example.com sent message",
        "2025-10-02 10:35:51 User john.doe@example.com logged out"
    ]
    with open('access.log', 'w', encoding='utf-8') as file:
        for log in fake_logs:
            file.write(log + "\n")
    print("Created 'access.log' with 10 fake log lines")

def extract_valid_emails(log_file):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = []
    with open(log_file, 'r', encoding='utf-8') as file:
        for line in file:
            found_emails = re.findall(email_pattern, line)
            emails.extend(found_emails)
    return emails

def save_valid_emails(emails):
    unique_emails = list(dict.fromkeys(emails))
    with open('valid_emails.txt', 'w', encoding='utf-8') as file:
        file.write("VALID EMAIL ADDRESSES\n\n")
        for email in unique_emails:
            file.write(email + "\n")
        file.write(f"Total Unique Emails: {len(unique_emails)}\n")
    return unique_emails

@log_time
def process_logs():
    create_fake_log_file()
    print("Extracting valid email addresses from 'access.log'...")
    emails = extract_valid_emails('access.log')
    unique_emails = save_valid_emails(emails)
    return unique_emails

def execute_task():
    print("REGEX LOG CLEANER\n")
    unique_emails = process_logs()
    print("File 'valid_emails.txt' created successfully!")
    print(f"Found {len(unique_emails)} unique email addresses:")
    for i, email in enumerate(unique_emails, 1):
        print(f"{i}. {email}")
