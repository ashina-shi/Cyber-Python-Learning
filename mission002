import requests

url = 'http://192.168.56.101'

directories = [
    "/admin",
    "/login",
    "/uploads",
    "/backup",
    "/config",
    "/images",
    "/css",
    "/js",
    "/test",
    "/dvwa",
    "/mutillidae",
]

found = []

try:

    for directory in directories:

        target = url + directory
        response = requests.get(target)

        if response.status_code == 200:         
            print(target, response.status_code)
            found.append(target)

        elif response.status_code == 403:
            print(f'[!] Forbidden: {target}')
            found.append(target)

        elif response.status_code == 404:
            print(f'[-] Not Found: {target}')

except Exception as e:
    print(e)

print('\nSuccess?200?')
for a in found:
    print(a)
