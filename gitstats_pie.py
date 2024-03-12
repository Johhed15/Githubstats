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
    sorted_languages = dict(sorted(languages.items(), key=lambda item: item[1], reverse=True)) # sorting
    return sorted_languages

# creating pie chart and saving it
def pie_chart(text_color='red',transparent=True):
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
    plt.figure(figsize=(12, 6), facecolor='#24292e') # githubs grey color as background
    # creating the pie chart
    plt.pie(sizes, labels=labels,colors=colors[:len(sizes)], autopct='%1.1f%%',explode=explode, shadow=False, textprops={'fontweight': 'bold', 'color': text_color,'fontsize': 16})
    plt.axis('equal')
    
    # Adding legend
    plt.legend(loc='best', labels=labels)

    plt.title(f'Distribution of Languages in {username}`s Repositories',fontweight='bold', fontsize=18, color=text_color)
    plt.savefig('lang-statistics.png', bbox_inches='tight',  transparens=transparent)
    plt.show()
    
pie_chart()




# Function to create a bar_chart of your languages
def bar_chart(text_color='black', transparent=True):
    # Getting our data
    rep = get_repositories()
    lang = get_languages(rep)

    # Picking out language and values
    labels = list(lang.keys())
    sizes = list(lang.values())

    # Filtering out small languages
    total = float(sum(sizes))
    sizes = [round((i / total) * 100, 1) for i in sizes]
    filtered_sizes = [s for s in sizes if s >= 0.01]
    filtered_labels =  labels[:len(filtered_sizes)]

    # Custom color palette with arbitrary number of colors
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b',
              '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#1a55FF', '#00FF00',
              '#FF00FF', '#FFFF00', '#00FFFF', '#FF6600', '#FF0066', '#0066FF']

    plt.figure(figsize=(12, 6))  
    bars = plt.bar(filtered_labels, filtered_sizes, color=colors[:len(filtered_sizes)])
    
    # Adding text labels in the middle of the bar
    for bar, size in zip(bars, filtered_sizes):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2,
                 f'{size}%', ha='center', va='bottom', color=text_color, fontweight='bold', fontsize=12)
    
    plt.xlabel('Languages', fontweight='bold', color=text_color, fontsize=14)
    plt.ylabel('Percentage', fontweight='bold', color=text_color, fontsize=14)
    plt.title(f'Distribution of Languages in {username}`s Repositories', fontweight='bold', fontsize=18, color=text_color)
    
    # Adjusting appearance
    plt.xticks(rotation=45, ha='right', fontsize=12, fontweight='bold', color=text_color)
    plt.yticks(fontsize=12, fontweight='bold', color=text_color)

    # Saving and showing the plot
    plt.savefig('lang-bar-chart.png', bbox_inches='tight', transparent=transparent)
    plt.show()


bar_chart()




