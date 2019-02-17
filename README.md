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

# Contributions

Plugins as contributions are very welcomed and encouraged. These plugins are disaplyed on the web page at
https://cronohub.org/plugins. These are loaded dynamically so once a plugin is merged it will be visible on the website
and immediately usable by others. Thank you!
