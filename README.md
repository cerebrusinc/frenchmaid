<p align="center">
    <img src="https://static.wixstatic.com/media/916fb4_88bd4d4d46e14f0c90f64213970c3a2d~mv2.png/v1/fill/w_750,h_750,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/916fb4_88bd4d4d46e14f0c90f64213970c3a2d~mv2.png" alt="frenchmaid logo" width="250" height="250" />
</p>

# frenchmaid v0.2.3

Are you a python developer who also/only uses windows and are sick and tired of constantly deteting those pesky `__pycache__` directories? Fear not, **frenchmaid** is here to help! frenchmaid is a CLI app written in pure python that will search your entire project directory and delete any `__pycache__` or other folders (and the files within) in your root directory. Now it can also add these folders to your ignore files!

**Supported Folders**

- \_\_pycache\_\_
- .mypy_cache

**Supported Ignores**

- git
- docker

## Installation

    pip install frenchmaid

or

    pip3 install frenchmaid

<details>
<summary><strong>Windows 10 PATH Error</strong></summary>
<br />
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
<br />

<details>
<summary><strong>Linux PATH Error</strong></summary>
<br />
If you encounter a "not on path" error after running `pip3 install frenchmaid` akin to:

    frenchmaid is installed in /home/<username>/.local/bin which is not on PATH...

Copy the relative path to frenchmaid from $HOME and add it to PATH. For this current example it would be:

    user@machine:~$ echo $HOME
    /home/<username>

    user@machine:~$ export PATH="$HOME/.local/bin:$PATH"

 </details>

## Update

    pip install --upgrade frenchmaid

or

    pip3 install --upgrade frenchmaid

## Example Usage

In any terminal window:

_Linux based machines:_

    user@machine:~/Documents/example-app$ frenchmaid clean

_Windows based machines:_

    C:\Users\<user>\Documents\example-app> frenchmaid clean

<br />
It's really that simple, just ensure that you are in your project's root directory! For clarity, the above example assumes that your project structure is something like this for example:
<br />
<br />

    example-app
    ├── LICENSE
    ├── requirements.txt
    └── src
         └── __init__.py
         └── app.py

If the root is `example-app` then you can see that the terminal should be in that dir.

## Commands

### clean

Run `frenchmaid clean` in your project's root directory without any arguments to remove all instances of supported folders. If you want to delete all instances of one type of folder and not any others, run the command with an option; For example, `frenchmaid clean mypy`.

For more information on which arguments are supported, run `frenchmaid clean --help`. If a folder you would like support for is not there, you can open a request [here](https://github.com/lewisjr/home-app/issues).

The currently supported arguments are:

- `pycache` which will only delete **\_\_pycache\_\_** folders
- `mypy` which will only delete **.mypy_cache** folders

### ignore

The ignore command (unlike the clean one) requires an argument to work. So to ignore all supported folders in your **.dockerignore** file, run `frenchmaid ignore docker` for example.

**Usage Notes**

- Ensure you run the command in the correct directory
- It will currently only add pycache and mypy cache folders toy our ignore file
- You do not have to create the ignore file before running the command. If one doesn't exist, it will create one
- If you already have an ignore file, it will append the folders to the file if they aren't already in the file

The currently supported arguments are:

- `git` which will add or append a **.gitignore** file
- `docker` which will add or append a **.dockerignore** file

For more information on which arguments are supported, run `frenchmaid ignore --help`. If a folder you would like support for is not there, you can open a request [here](https://github.com/lewisjr/home-app/issues).

## Options

### Version

In any terminal in any directory:

    frenchmaid -v

or

    frenchmaid --version

will return (for example):

    frenchmaid v0.2.3

### Help

In any terminal in any directory:

    frenchmaid --help

will return:

    Usage: frenchmaid [OPTIONS] COMMAND [ARGS]...

    A handy tool to delete all junk!

    Options:
    -v, --version               View the CLI app version
    --install-completion        Install completion for the current shell.
    --show-completion           Show completion for the current shell, to copy it or customize the installation.
    --help                      Show this message and exit.

    Commands:
    clean       Delete all instances of junk folders
    ignore      Add junk folders to ignore files

Note that this option can also be used in tandem with any command.

## Support and Reporting

You can report any bugs or improvements [here](https://github.com/lewisjr/home-app/issues), I will try to address them as soon as possible. Feel free to suggest any other files or folders you think it should delete (e.g .pytest_cache) with all context on how they appear. I will happily make it a possibility without breaking the current format! To the best of my abilities of course, and the github page will be updated on any changes.

# Changelog

## v0.2.x

<details open>
<summary><strong>v0.2.3</strong></summary>

- Codebase improvements
- Full parity between `windows` and `linux` systems; **Full Stability**
- Added .gitignore
- README structure changed
- Note added to v0.2.0 to denote it's instability
</details>

<details>
<summary><strong>v0.2.2</strong></summary>

- Updated README version history to include v0.2.1 updates
</details>

<details>
<summary><strong>v0.2.1</strong></summary>

- Fixed ignore format for **pycache** in git
</details>

<details>
<summary><strong>v0.2.0</strong></summary>

- Added a logo to the README
- Added instructions for a Linux PATH error
- Added ignore command and arguments
- Added support for mypy cache folders
- Added arguments to the clean command
- Added `--help` context to all commands
- Moved all functions to a modules folder
- Added a class switch
- Typed modules
- Unstable on linux bases systems

</details>
<br />

## v0.1.x

<details>
<summary><strong>v0.1.2</strong></summary>

- License has been updated to Apache from MIT effective from the date of this release
- Notes on potential path problems that can arise from installation on Windows have been added to the README

</details>

<details>
<summary><strong>v0.1.1</strong></summary>

- Issue on linux machines fixed with directory name post pycache delete
  - The package no longer displays the root directory's full absolute path (e.g Documents/example-app), but rather just the root directory's name (e.g example-app) on linux machines.

</details>

<details>
<summary><strong>v0.1.0</strong></summary>

- Initial Release; Stable version for use on all platforms

</details>
