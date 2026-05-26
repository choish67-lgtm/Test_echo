import re

url = input("URL: ").strip()

#username = re.sub(r"^(http|https)://twitter\.com/", "", url)
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/([a-z0-9_]+)$", url, re.IGNORECASE):
    if matches.group(1) == "com":
        print(f"Username:", matches.group(2))

#matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
#if matches:
#    print(f"Username:", matches.group(1))

#username = url.replace("https://twitter.com/", "")
#username = url.removeprefix("https://twitter.com/", "")
#print(f"Username: {username}")