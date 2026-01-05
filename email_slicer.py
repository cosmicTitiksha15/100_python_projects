# This program prints username and domain upon email input by user + Validation + domain formatting + batch processing
# | **Beginner** | **Console/CLI** | **4. Email Slicer** | String manipulation, finding/splitting substrings. |
try : 
    num = int(input("Number of email entries you have to slice : "))
    # batch processing
    list_emails = []
    for i in range(num):
        query = input("Enter the email address : ").strip()
        list_emails.append(query)

    for entry in list_emails:
    # Validation
        if '@' in entry and '.' in entry:
            entry = entry.split('@')
            username = entry[0]
            domain = entry[1]
            # Domain formatting
            # if domain == 'gmail.com':
            #     print('Ah...a google mail user.')
            print(f"Username : ({username}) and domain name : ({domain})")
            
        else:
            print(f"Invalid Email : {entry}")
except ValueError:
    print("Please enter a positive integer.")