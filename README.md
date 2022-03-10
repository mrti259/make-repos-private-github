# Make Repos Private

Hide all your Github's repositories with this simple script.

## Prerrequisites

You need Python3. Dependencies can be installed running

> pip install -r requirements.txt

Also, you can use Nix and all dependencies will be available. Simply run:

> nix-shell shell.nix # shell.nix can be omitted

To connect to Github's API you need to provide a personal access token with `repo` permissions.
Create one [following this instructions](https://docs.github.com/es/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

For more information [read the documentation](https://docs.github.com/es/rest/overview/resources-in-the-rest-api#authentication)

## Run

First, remember to load your personal access token to the env

> export TOKEN=token

Then, run `python main.py`.

If nothings went wrong, the script will successfully exit.
