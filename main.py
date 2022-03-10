import requests
import os

token = os.environ["TOKEN"]

def api(method: str, endpoint: str, **kwargs) -> requests.Response:
    base_url = "https://api.github.com"
    headers = {
        "authorization": f"token {token}",
        "accept": "application/vnd.github.v3+json"
    }

    response = requests.request(method, base_url + endpoint, headers=headers, **kwargs)

    if response.status_code != 200:
        raise Exception(endpoint, response.json())

    return response

def get_user():
    return api("GET", "/user").json()

def get_repos_from_user(username: str):
    return api("GET", "/users/{username}/repos".format(username=username)).json()

def make_repo_private(owner: str, repo: str):
    api("PATCH", "/repos/{owner}/{repo}".format(owner=owner, repo=repo), json={"private": True})

if __name__ == "__main__":
    username = get_user()["login"]
    repos = get_repos_from_user(username)

    for repo in repos:
        fork = repo["fork"]
        private = repo["private"]

        if not fork and not private:
            owner = repo["owner"]["login"]
            repo_name = repo["name"]
            make_repo_private(owner, repo_name)
