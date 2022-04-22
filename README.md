# French Maid v0.1.0

Are you a python developer who also/only uses windows and are sick are tired of constantly deteting those pesky `__pycache__` directories? Fear not, **frenchmaid** is here to help! frenchmaid is a CLI tool written in pure python that will look in your entire project directory and delete any `__pycache__` folders (and the files within) in your app directory.

## Installation

    pip install frenchmaid

or

    pip3 install frenchmaid

## Usage

In any terminal window:

    C:\Users\<username>\Documents\example-app> frenchmaid clean

<br>
It's really that simple, just ensure that you are in you project's root folder! For clarity, the above example assumes that your project structure is something like this for example:
<br><br>

    example-app/
    |________ main.py
    |________ requirements.txt
    |________ src/
             |-------- __init__.py
             |-------- app.py

If the root is `example-app` then you can see that the terminal should be in that folder.

## Other Commands

#### Version

In any terminal in any directory:

    frenchmaid -v

or

    frenchmaid --version

will return (for example):

    French Maid v0.1.0

#### Help

In any terminal in any directory:

    frenchmaid --help

will return:

    Usage: French Maid [OPTIONS] COMMAND [ARGS]...

    Options:
      -v, --version                   View the CLI version and stuff... maybe
      --install-completion [bash|zsh|fish|powershell|pwsh]
                                      Install completion for the specified shell.
      --show-completion [bash|zsh|fish|powershell|pwsh]
                                      Show completion for the specified shell, to
                                      copy it or customize the installation.
      --help                          Show this message and exit.

    Commands:
      clean

## Support and Reporting

You can report any bugs or improvements [here](https://github.com/lewisjr/home-app/issues), I will try to address them as soon as possible. Feel free to suggest any other files or folders you think it should delete (e.g .pytest_cache) with all context on how they appear. I will happily make it a possiblity without breaking the current format! To the best of my abilites of course, and the github page will be updated on any changes.
