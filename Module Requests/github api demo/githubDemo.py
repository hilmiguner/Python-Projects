import requests

class GitHub:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"
        self.auth = {'Authorization': 'token ' + self.token}

    def getUser(self, userName):
        response = requests.get(self.api_url + "/users/" + userName)
        if response.status_code == 200:    
            return response.json()

    def getRepos(self, userName):
        response = requests.get(self.api_url + "/users/" + userName + "/repos")
        if response.status_code == 200:
            return response.json()

    def createRepo(self, name):
        self.json = {
            "name" : name,
            "description" : "This is a new repository.", 
            "homepage" : "https://github.com",
            "private" : True
        }
        response = requests.post(self.api_url + "/user/repos", json=self.json, headers=self.auth)
        return response.json()

objGitHub = GitHub()

while True:
    secim = int(input("1-Find user.\n2-Get Repositories\n3-Create Repository\n4-Exit\nSelection: "))
    if secim == 4:
        break
    else:
        if secim == 1:
            userName = input("Write the username: ")
            user = objGitHub.getUser(userName)
            if user == None:
                print("Failure")
            else:
                print(" USER INFO ".center(50, "*"))
                print(f"Name: {user['login']}\nPublic repos: {user['public_repos']}\nFollowers: {user['followers']}")
                print(50*"*")
        elif secim == 2:
            userName = input("Write the username: ")
            repos = objGitHub.getRepos(userName)
            if  repos == None:
                print("Failure")
            else:
                print(" REPOSITORIES ".center(50, "*"))
                for repo in repos:
                    print(f"Repository Name: {repo['name']}")
                print(50*"*")
        elif secim == 3:
            repoName = input("Enter the repository name: ")
            newRepo = objGitHub.createRepo(repoName)
            print(" NEW REPO INFO ".center(50, "*"))
            print(f"Name: {newRepo['name']}\nPrivate Status: {newRepo['private']}\nOwner: {newRepo['owner']['login']}")
            print(50*"*")
        else:
            print("Wrong choice.")
