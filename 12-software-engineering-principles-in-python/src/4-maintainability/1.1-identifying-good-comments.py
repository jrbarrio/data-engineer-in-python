import re

def extract_0(text):
    # match and extract dollar amounts from the text
    return re.findall(r'\$\d+\.\d\d', text)

def extract_1(text):
    # return all matches to regex pattern
    return re.findall(r'\$\d+\.\d\d', text)

text = "Our competitor pricing is $10.50 an inch. Our price is $125.00 a foot."

# Print the text
print(text)

# Print the results of the function with better commenting
print(extract_1(text))