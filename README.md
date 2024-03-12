# How to get your own GitHub stats!!

## Current functions
- get_repositories() : Retrieve repositories and return a dictionary
- get_languages() : Extracst languages from the retrieved dictionary and return them where keys are the languages and the values are number of bits
- pie_chart() : Creates and saves a pie chart with the data from get_languages
- bar_chart() : Creates and saves a bar chart with the data from get_languages

Just Copy the code from the files above and follow the steps below to create your own GitHub-stats!! 

## Step 1:

First you need to create a .gitattributes file in every repository that calculates the statistics wrong.

In this file you can change how Github should calculate each file within each repository with the following code:

```Python
# example from jupyter notebook to python

*.ipynb linguist-language=Python 

# pdf to R(if you, like me, save reports as pdf)

*.pdf linguist-language=R

```
<br>

## Step 2:

### Go to settings on github and then click on developer settings and then generate a token, remember to save it!


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

### Functions to get your data!

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

## Step 3:

Now you just need to run these functions to download the data, or you could use my chart functions which does it for you to create the vizualisation!

When running the funtions you have the option to switch the text and label color to whatever you want, you also have the option to remove the transparent option for the saved png which then will be generated with a white background! The function have text_color='red'/'black' and transparent=True as default so you dont need to add any arguments if you want that combination. 

```Python
# Example of how to change it to black text with a white background
pie_chart('black', transparent=False)

```

Upload the image to your repository and use the code below with the link to your image in your README file.

```md
<img src="https://github.com/username/repository/blob/main/lang-statistics.png" alt="Graphic">	

```
<img src="https://github.com/Johhed15/Johhed15/blob/main/lang-statistics.png" alt="Graphic">	



Commit and now you are done!!
