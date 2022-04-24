# French Maid v0.1.2

Are you a python developer who also/only uses windows and are sick are tired of constantly deteting those pesky `__pycache__` directories? Fear not, **frenchmaid** is here to help! frenchmaid is a CLI tool written in pure python that will search your entire project directory and delete any `__pycache__` folders (and the files within) in your root directory.

## Installation

    pip install frenchmaid

or

    pip3 install frenchmaid

<details>
<summary>Windows 10 PATH Error</summary>

If you encounter a path error on your CMD after running one of the commands above (e.g one about not finding a frenchmaid.exe or the frenchmaid.exe not being on PATH), carry out the following steps:

1.  Uninstall frenchmaid

        pip uninstall frenchmaid

2.  Open a new terminal as admin

    1. Open the start menu (press the windows button)
    2. Search for CMD
    3. Right click and select run as administrator

3.  Install frenchmaid globally

        pip install frenchmaid

Remember not to use the `--user` flag unless you have set this option on path as well.

 </details>

## Update

    pip install --upgrade frenchmaid

or

    pip3 install --upgrade frenchmaid

## Usage

In any terminal window:

_Linux based machines:_

    <user>@<machine>:~/Documents/example-app$ frenchmaid clean

_Windows based machines:_

    C:\Users\<user>\Documents\example-app> frenchmaid clean

<br>
It's really that simple, just ensure that you are in you project's root directory! For clarity, the above example assumes that your project structure is something like this for example:
<br><br>

    example-app/
    |________ main.py
    |________ requirements.txt
    |________ src/
             |_________ __init__.py
             |_________ app.py

If the root is `example-app` then you can see that the terminal should be in that folder.

## Other Commands

#### Version

In any terminal in any directory:

    frenchmaid -v

or

    frenchmaid --version

will return (for example):

    French Maid v0.1.2

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

# Version History

## v0.1.2

Minor patch 2; License has been updated to Apache from MIT effective from the date of this release. Notes on potential path problems that can arise from installation on Windows have been added to the README.

## v0.1.1

Minor patch to codebase; Issue on linux machines fixed with directory name post pycache delete. The package no longer displays the root directory's full absolute path (e.g Documents/example-app), but rather just the root directory's name (e.g example-app) on linux machines.

## v0.1.0

Initial Release; Stable version for use on all platforms.
