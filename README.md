# Cronohub Plugins

These are a collection of source and target plugins that are used by cronohub to perform work.

The structure of a plugin is as follows:

# Requirements

Each plugin is like a simple Python project. It needs to encapsulate everything that it requires in it's own.

It needs to have a requirements.txt so that anyone using the plugin can easily install the required modules.

One of those requirements must be `cronohub`. Cronohub also requires `colors` so that must also be part of it's package list.

# Structure

The entry to the plugin must be the name of the plugin as folder name and the name of the plugin as `name.py`. For example
for github as source the directory structure looks like this:

```
plugins-
       |
       - source-
               |
               - github-
                       |
                       - github.py
                       - requirements.txt
```

# Class

The plugins must not contain a main method. It's entry point will be class named either `SourcePlugin` if it's a source plugin
or `TargetPlugin` if it's a target plugin.

These classes must have the base `target_plugin.CronohubTargetPlugin` or `source_plugin.CronohubSourcePlugin` respectively.
For example for github the class declaration would look like this:

```python
class SourcePlugin(source_plugin.CronohubSourcePlugin):
```

# Installing

These plugins are meant to be downloaded as is and copied into a folder under `~/.config/cronohub/plugins/{source|target}/<plugin_name>`.

For now, you can use git's sparese checkout to get only the plugin you desire. (until I setup the site and have proper releases).

To do that, follow these steps:

```bash
# init the repository
git init
# enable sparse checkout
git config core.sparsecheckout true
# tell it which folder you would like to check out
echo source/github/ >> .git/info/sparse-checkout
# add the remote
git remote add -f origin https://github.com/cronohub/plugins.git
# fetch
git pull origin master
```

This will only checkout the github source plugin.

Or, alternatively, checkout the whole repository under `~/.config/cronohub/` to have access to all plugins.

For more information about the requirements of each plugin look under their respective
folder's README file.

# Configuration

If a plugin requires configuration files to be present, it could use Python's `site-packages` folder
or, cronohub provides a directory, `~/.config/cronohub/configurations/<plugin_name>`. This folder
can containe all the files that a given plugin needs. This, of course, means that each plugin's name
must be unique across cronohub. Otherwise, it would overwrite another plugin's configuration files.

# Contributions

Plugins as contributions are very welcomed and encouraged. These plugins are disaplyed on the web page at
https://cronohub.org/plugins. These are loaded dynamically so once a plugin is merged it will be visible on the website
and immediately usable by others. Thank you!
