"""
link: https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
"""


def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case('the stealth warrior'))
print(to_camel_case('The-Pippi_Was_pippi'))
print(to_camel_case('a-Cat-Was-Hungr'))
print(to_camel_case('the-Pippi-Is-cute'))
print(to_camel_case('An empty string was provided but not returned'))
print(to_camel_case(' '))

