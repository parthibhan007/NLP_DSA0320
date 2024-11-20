import re

def main():
    # Sample text
    text = """
    John Doe: john.doe@example.com
    Jane Smith: jane_smith123@gmail.com
    Sam Brown: sam.brown@yahoo.com
    """

    # Pattern to match email addresses
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    # Find all email addresses in the text
    emails = re.findall(email_pattern, text)
    print("Emails found:")
    for email in emails:
        print(email)

    # Pattern to match names followed by email addresses
    name_email_pattern = r'(\w+\s\w+):\s([\w\.-]+@[\w\.-]+\.\w+)'

    # Search and extract names and emails
    matches = re.findall(name_email_pattern, text)
    print("\nNames and Emails found:")
    for name, email in matches:
        print(f"Name: {name}, Email: {email}")

    # Check if a specific email exists in the text
    specific_email = "sam.brown@yahoo.com"
    if re.search(re.escape(specific_email), text):
        print(f"\nThe email {specific_email} exists in the text.")
    else:
        print(f"\nThe email {specific_email} does not exist in the text.")

if __name__ == "__main__":
    main()
