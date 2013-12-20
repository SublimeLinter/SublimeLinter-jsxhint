#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# SublimeLinter-jshint written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# Forked for JSXHint by Samuel Reed (STRML)
#
# License: MIT
#

"""This module exports the JSXHint plugin linter class."""

import os
from SublimeLinter.lint import Linter, util

class JSXHint(Linter):

    """Provides an interface to the jshint executable."""

    syntax = ('jsx', 'javascript_jsx', 'javascript (jsx)')
    executable = 'jsxhint'
    regex = r'^.+?: line (?P<line>\d+), col (?P<col>\d+), (?P<message>.+) \((?:(?P<error>E)|(?P<warning>W))\d+\)$'

    def cmd(self):
        """
        Return a string with the command line to execute.

        We define this method because we want to use the .jshintrc files,
        and we can't rely on jsxhint to find them, because we are using stdin.

        """

        command = [self.executable_path]
        jshintrc = util.find_file(os.path.dirname(self.filename), '.jshintrc')

        if jshintrc:
            command += ['--jshintrc', jshintrc]

        return command + ['--verbose', '--stdin']
