
# Py3Sh - Python Shell Script Generator


🚀 **Py3Sh** is a lightweight tool that generates executable shell scripts for running Python programs. It simplifies script execution by eliminating the need to manually type `python3 script.py`. 

### **✨ Features**
- ✅ **Automatic script generation** – Converts Python scripts into runnable shell scripts.  
- ✅ **No `./` required** – Generates globally executable commands.  
- ✅ **Easy installation** – One command setup.  
- ✅ **Supports arguments** – Pass parameters seamlessly to your Python scripts.  

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
py3sh my_script.py my_runner \$1 \$2 \$3
```

Result:

```sh
#!/usr/bin/bash
python3 my_script.py $1 $2 $3
```
