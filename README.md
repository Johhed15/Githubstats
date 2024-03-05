# How to get your own GitHub stats!!

Just Copy the code from the files above and follow the steps below to create your own GitHub-stats!! 

```Python

"""
First you need to create a .gitattributes file in every repository that calculates the statistics wrong.
In this file you can change how Github should calculate each file with the following code:
"""

# example from jupyter notebook to python

*.ipynb linguist-language=Python 

```
<br>

## Go to settings on github and then click on developer settings to generate a token and save it!


In the following code you should add your Github username and the created token
<br>
```Python

# GitHub API base URL
base_url = "https://api.github.com"

# Your GitHub username
username = "USERNAME"

# Authentication: Replace 'YOUR_TOKEN' with your actual token
headers = {
    "Authorization": "token YOUR_TOKEN"
}

```
<br>

When the first steps are done you can then use the following functions to get your data!! 

<br>

```Python

# Fetch repositories
def get_repositories():
    url = f"{base_url}/users/{username}/repos"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Parse languages from repository data
def get_languages(repos):
    languages = {}
    for repo in repos:
        repo_name = repo["name"]
        url = f"{base_url}/repos/{username}/{repo_name}/languages"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repo_languages = response.json()
            for lang, bytes in repo_languages.items():
                if lang in languages:
                    languages[lang] += bytes
                else:
                    languages[lang] = bytes
    sorted_languages = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True))
    return sorted_languages

```
