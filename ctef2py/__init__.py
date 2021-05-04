# -*- coding: utf-8 -*-

"""
Package ctef2py
=======================================

Top-level package for ctef2py.
"""

__version__ = "0.1.0"

try:
    import ctef2py.getgauss
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'getgauss')
    if not msg:
        import ctef2py.getgauss
    else:
        click.secho(msg, fg='bright_red')

try:
    import ctef2py.fmohl
except ModuleNotFoundError as e:
    # Try to build this binary extension:
    from pathlib import Path
    import click
    from et_micc_build.cli_micc_build import auto_build_binary_extension
    msg = auto_build_binary_extension(Path(__file__).parent, 'fmohl')
    if not msg:
        import ctef2py.fmohl
    else:
        click.secho(msg, fg='bright_red')


def hello(who='world'):
    """'Hello world' method.

    :param str who: whom to say hello to
    :returns: a string
    """
    result = "Hello " + who
    return result

# Your code here...