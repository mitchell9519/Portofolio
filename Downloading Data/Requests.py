import requests 
from plotly.graph_objs import Bar
from plotly import offline




url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
result = requests.get(url,headers)
print(f"Status code:{result.status_code }")

#process results

response_dict = result.json()
repo_dicts = response_dict['items']
stars,labels,repo_links = [],[],[]

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url=repo_dict['html_url']
    repo_link= f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    print(f"\n{repo_name}")
    print(f"{repo_url}")
    print(F"{repo_link}")

    
    
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner} <br /> {description}"
    labels.append(label)

data = [{
    'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext':labels,
        'marker' :{
            'color':'blue',
            'line':{'width':1.5, 'color':'blue'}
        },
        

    }]



my_layout = {
    'title':'Most starred Python projects (Github)',
    'titlefont': {'size':24},

    'xaxis':{
        'title':'Repository',
        'titlefont':{'size':24},
        'tickfont':{'size':14},

    },
    'yaxis':{
        'title': 'Stars',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
    },
    
    }
    
fig = {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos2.html')
fig.show()



    
