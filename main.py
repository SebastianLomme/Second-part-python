import requests

def fetch_user_snippets():
    user = requests.get('https://run.mocky.io/v3/3b7fdcfc-53b9-43e7-9042-53d1870c8693').json()
    # breakpoint() # halt execution and open a shell
    snippets = requests.get('https://run.mocky.io/v3/7f76961a-58b0-4ee2-b6a0-3c4faf90f4ed').json()
    snippets = [s['snippet'] for s in snippets if s['user_id'] == user['user_id']]
    print("snippets", snippets)
    return snippets

print(fetch_user_snippets())
