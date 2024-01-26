import requests 

url ='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
result = requests.get(url,headers)
print(f"Status code:{result.status_code }")
#Just checks status code

#name of dict
response_dict = result.json()
#process results
# print(response_dict.keys())

# print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")


#examine first dict
repo_dict = repo_dicts[0]
# print(f"\nkeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(f"{key}")
print('\n Selected info about each repository: ')
#print("\n selected information about first repository: ")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

#summary of repositories

