import re

def clean_name(name):
    name = str(name).lower()
    name = re.sub(r"[^\w\s]", "", name)
    return " ".join(name.split())