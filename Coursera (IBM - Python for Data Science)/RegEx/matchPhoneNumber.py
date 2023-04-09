import re

pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten digits
text = "Phone Number of Customer: 5551239988"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("Phone number not found.")
