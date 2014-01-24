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

from SublimeLinter.lint import Linter


class JSXHint(Linter):

    """Provides an interface to the jsxhint executable."""

    syntax = ('jsx', 'javascript_jsx', 'javascript (jsx)')
    cmd = 'jsxhint --verbose * -'
    regex = (
        r'^(?:(?P<fail>ERROR: .+)|'
        r'.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?P<message>.+) \((?:(?P<error>E)|(?P<warning>W))\d+\))'
    )
    config_file = ('--config', '.jshintrc', '~')

    def split_match(self, match):
        """
        Return the components of the match.

        We override this to catch linter error messages and place them
        at the top of the file.

        """

        if match:
            fail = match.group('fail')

            if fail:
                # match, line, col, error, warning, message, near
                return match, 0, 0, True, False, fail, None

        return super().split_match(match)
