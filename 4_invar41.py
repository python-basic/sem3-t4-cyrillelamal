import re
import requests


URL = 'https://kodaktor.ru/j/users'

resp = requests.get(URL)
resp.raise_for_status()
json = resp.text


# Content of curly brackets
CB_PATTERN = re.compile(r'\{(.*)\}', re.DOTALL)
# Content of square brackets
SB_PATTERN = re.compile(r'\[(.*)\]', re.DOTALL)
# Key
KEY_PATTERN = re.compile(r'\"(.*?)\"')
# Value
VALUE_PATTERN = re.compile(r'[^:]+\s*(?=,|$)')

# Go to the nested objects
main_object = re.search(CB_PATTERN, json)
if main_object is not None:
    nested_objects = re.findall(SB_PATTERN, main_object.group(1))
    if not nested_objects:
        pass
