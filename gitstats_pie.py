# imports
import requests
import matplotlib.pyplot as plt

# GitHub API base URL
base_url = "https://api.github.com"

# Your GitHub username
username = "USERNAME"

# Authentication: Replace 'YOUR_TOKEN' with your actual token
headers = {
    "Authorization": "token YOUR_TOKEN"
}

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

# creating pie chart and saving it
def pie_chart():
    # getting our data
    rep=get_repositories()
    lang = get_languages(rep)

    # picking out language and values
    labels = list(lang.keys())
    sizes =tuple(lang.values())

    total = float(sum(sizes)) 
    # percentage
    sizes = [ round(i/total,3)*100 for i in sizes]

    # filtering out small languages

    sizes = filter(lambda x: x>=0.001, sizes)
    sizes = list(sizes)
    labels = labels[:len(sizes)]

    # Get colors from the tab20 colormap

    # Custom color palette with arbitrary number of colors
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', 
              '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55FF', '#00FF00', 
              '#FF00FF', '#FFFF00', '#00FFFF', '#FF6600', '#FF0066', '#0066FF']

    explode = (0.03,)*len(sizes)
    plt.figure(figsize=(14, 8), facecolor='#24292e') # githubs grey color as background
    # creating the pie chart
    plt.pie(sizes, labels=labels,colors=colors[:len(sizes)], autopct='%1.1f%%',explode=explode, shadow=False, textprops={'fontweight': 'bold', 'color': 'white','fontsize': 16})
    plt.axis('equal')
    
    # Adding legend
    plt.legend(loc='best', labels=labels)

    plt.title(f'Distribution of Languages in {username}`s Repositories',fontweight='bold', fontsize=18, color='white')
    plt.savefig('lang-statistics.png', bbox_inches='tight',  facecolor='#24292e')
    plt.show()
    
pie_chart()