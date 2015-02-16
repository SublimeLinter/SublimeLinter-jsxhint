SublimeLinter-jsxhint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-jsxhint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-jsxhint)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [jsxhint](https://github.com/STRML/JSXHint). It will be used with files that have the “JSX” syntax.

JSX is a JavaScript XML syntax transform intended for use with [React.js](http://facebook.github.io/react/docs/jsx-in-depth.html).

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before using this plugin, you must ensure that `jsxhint` is installed on your system. To install `jsxhint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `jsxhint` by typing the following in a terminal:
   ```
   npm install -g jsxhint
   ```

1. Install a JSX syntax file. A syntax file is no longer included in this repo. Supported syntaxes are:

* [Babel-Sublime](https://github.com/babel/babel-sublime) (supports additional ES6 features)
* [Sublime-React](https://github.com/reactjs/sublime-react)


### Linter configuration
In order for `jsxhint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `jsxhint` is installed and configured, you can proceed to install the SublimeLinter-jsxhint plugin if it is not yet installed.


### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `jsxhint`. Among the entries you should see `SublimeLinter-jsxhint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

You can configure `jsxhint` options in the way you would from the command line, with `.jshintrc` files. For more information, see the [jshint docs](http://www.jshint.com/docs/). The linter plugin does this by searching for a `.jshintrc` file itself, just as `jsxhint` does from the command line. You may provide a custom config file by setting the linter’s `"args"` setting to `["--config", "/path/to/file"]`. On Windows, be sure to double the backslashes in the path, for example `["--config", "C:\\Users\\Aparajita\\jshint.conf"]`.

The path to the `.jshintrc` file is cached, meaning if you create a new `.jshintrc` that should have precedence over the previous one (meaning it is closer to the .js file) you need to clear the cache for the linter to use the new `.jshintrc` You can clear the cache by going to: Tools > SublimeLinter > Clear Caches.

You may want to provide separate linter settings for `jsxhint` vs `jshint`. To do that, use the option `config_filename`.

For example, you could put this configuration in `.sublimelinterrc`, or in your User settings for SublimeLinter:

```
{
    "linters": {
        "jsxhint": {
            "config_filename": ".jsxhintrc"
        }
    }
}

```

## Troubleshooting

* JSXHint is not linting!
  - Ensure you are using an appropriate syntax definition for the file you are editing. It must be a JSX-specific syntax
    so that SublimeLinter knows to use this package.
  - View the Sublime Text console by pressing `ctrl-tilde`. If you open an issue, please include this output.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
