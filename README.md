
# Py3Sh - Python Shell Script Generator

Py3Sh makes it easy to generate executable shell scripts for running Python programs.

## 🚀 Installation

```sh
git clone https://github.com/zimoshi/py3sh.git
cd py3sh
python3 py3sh-gem.py  # Install py3sh with the gem
```

## 🔥 Usage

Generate a shell script for a Python script:

```sh
py3sh my_script.py my_runner
```

Now, you can run `my_runner` directly:

```sh
my_runner
```

If you have some `argv`, just include it in the order you want!

```sh
py3sh my_script.py my_runner 1 2 3
```

Result:

```sh
#!/usr/bin/bash
python3 my_script.py $1 $2 $3
```
