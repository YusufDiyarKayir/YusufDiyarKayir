import requests

username = "YusufDiyarKayir"
url = f"https://api.github.com/users/{username}/repos"
repos = requests.get(url).json()

with open("README.md", "r") as f:
    content = f.read()

# Yeni projeleri ekle
projects_section = "## Projects\n\n"
for repo in repos:
    projects_section += f"### {repo['name']}\n{repo['description'] or 'No description'}\n\n"

# README güncelle
new_content = content.split("## Projects")[0] + projects_section
with open("README.md", "w") as f:
    f.write(new_content)
