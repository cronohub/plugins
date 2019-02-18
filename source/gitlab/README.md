# Gitlab Source Plugin

This plugin will download all the repositories, including private, of a given user.
The user is identified by the provided TOKEN. The files are timestamped and downloaded
in parallel with a thread count of 5.

# Configurations

```bash
Help:
            Gitlab config file under ~/.config/cronohub/configurations/gitlab/gitlab.cfg
            [Optional]: Environment Property: CRONOHUB_GITLAB_ID
```
