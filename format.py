import re

name = input("what's your name? ").strip()
#matches = re.search(r"^(.+), *(.+)$", name)
#if matches:
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
#    last = matches.group(1)
#    first = matches.group(2)
#    last, first = matches.group()
#    name = f"{first} {last}"
print(f"hello, {name}")


if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")