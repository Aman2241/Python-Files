import re
normal_text="hello there, my email is aman25722@gmail.com"
pattern=re.compile("[a-zA-Z0-9]+\@[a-zA-z0-9]+\.[a-zA-Z]+")
email=pattern.findall(normal_text)
print(email)