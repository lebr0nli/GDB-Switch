# GDB Switch

GDB Switch is a GDB plug-in that can help you manage your GDB plug-ins effortlessly and gracefully with a single command and a JSON file.

## Features

- Turn on a gdb plug-in by directly passing the plug-in name to `gdbswitch`

- Turn on a gdb plug-in by passing the plug-in name inside an environment variable (`gdbswitch -e NAME`)

## How to install it?

Make sure you have GDB 8.0 or higher compiled with Python3.6+ bindings, then:

1. Download this plug-in:

```shell
git clone https://github.com/lebr0nli/GDB-Switch.git
```

2. Use `./install.sh` to install it or:

```shell
mkdir -p "$HOME/.gdb-switch/"
cp gdbinit-switch.py "$HOME/.gdb-switch/gdbinit-switch.py"
cp plugins.json "$HOME/.gdb-switch/plugins.json"
```

## Usage

First, you need to change `~/.gdb-switch/plugins.json` to fit your setup, for example:

```json
{
    "default": "pwndbg",
    "pwndbg": "/pwndbg/gdbinit.py",
    "gef": "~/.gdbinit-gef.py"
}
```

> Note: `"default"` is a default plug-in if you pass an empty env variable to `gdbswitch`, you can change its value to null if you want.

Add `source ~/.gdb-switch/gdbinit-switch.py` to the first line of `~/.gdbinit`.

## Example 1

This `~/.gdbinit` will turn on `gef`:

```shell
source ~/.gdb-switch/gdbinit-switch.py
gdbswitch gef
```

## Example 2

This `~/.gdbinit` will turn on GDB plug-in via an environment variable:

```shell
source ~/.gdb-switch/gdbinit-switch.py
gdbswitch -e GDB
```

By using this, you can quickly switch between `gef` and `pwndbg` by using `export GDB=pwndbg` or `export GDB=gef`.

Or, if you use `pwntools` for pwning, you can use `gef` to debug your binary file by writing:

```python
context.terminal = ["tmux", "splitw", "-h", "-e", "GDB=gef"]
io = gdb.debug([exe.path], gdbscript=GDB_SCRIPT)
```

If you want to switch to `pwndbg`:

```python
context.terminal = ["tmux", "splitw", "-h", "-e", "GDB=pwndbg"]
io = gdb.debug([exe.path], gdbscript=GDB_SCRIPT)
```

## Bugs, suggestions, and ideas

If you found any bug, or you have any suggestions/ideas about this plug-in, feel free to leave your feedback on the GitHub issue page or send me a pull request!

Thanks!
