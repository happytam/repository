from urllib import urlopen

html = urlopen("email.163.com")
print(html.read())
