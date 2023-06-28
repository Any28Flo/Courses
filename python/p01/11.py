# Personal Message
"""
 Use a variable to represent a person's name, and print a message to that person.
 Your message should be simple , suh as,
 ' Hello Eric, would you like to learn some Python today'

"""
name = input('Insert your name: ')
message = f'Hello {name.title()}, would you like to learn some Python today'
print(message)

# Name Cases
"""
Use a variable to represent a person's name, and then print that person's name 
in lowercase, uppercase and title case
"""
lower = name.lower()
print(lower)
upper = name.upper()
print(upper)
title = name.title()
print(title)

# Famous Quote
"""
Find a quote from a famous person you admire. Print the quote and the name of its author.
Your output should look something like the following, including the quotation marks.

"""
person = ""
quote = f"{person.title()} Albert EINstein once said 'A person who never made a mistake never tried anything new'"
print(quote)

"""
Repeat the exercise, but this time, represent the famous person's  name using a variable called
famous_person. Then compose your message and represent it with a new variable called message. Print
your message
"""
famous_person = "Albert EINsTEin"
quote = "A person who never made a mistake never tried anything new"
message = f'{famous_person.title()} once said "{quote}"'
print(message)

# Stripping name
"""
Using a variable to represent a person's name and include some whitespace
characters at the beginning and end of the name. Make sure you use each character combination.

"""
email = " foglzerika@gmail.com "
print(f'\t {email}')
print(f'\n{email}')
print(f'{email.lstrip()}')
print(f'{email.rstrip()}')
print(f'{email.strip()}')
