# Github Source Plugin

This plugin will download all the repositories, including private, of a given user.
The user is identified by the provided TOKEN. The files are timestamped and downloaded
in parallel with a thread count of 5.

# Configuration

```
Help (github source plugin):
    - Environment Property:
        CRONO_GITHUB_TOKEN: a token with access to listing repositories for a given user.
    - File that filters the list of repositories to archive. If not present, all will be archived.
        ~/.config/cronohub/configurations/github/.repo_list
```
