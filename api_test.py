import requests

#1 Make GET Request
url = "https://api.github.com/users/octocat"
response = requests.get(url)

# 2. Check the status code (did it work?)
print(f"Status code: {response.status_code}")

# 3. Parse the JSON response into a Python dictionary
data = response.json()

# 4. Pull out and print a few fields
print(f"Username: {data['login']}")
print(f"Name: {data['name']}")
print(f"Public repos: {data['public_repos']}")
print(f"Bio: {data['bio']}")

