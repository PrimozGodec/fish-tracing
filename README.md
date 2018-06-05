# Fish tracing
Scripts fro plotting fish traces

## Instalation

1. Open the `Terminal` app

2. Install Python

   #### MacOS
   
   Check if `Homebrew` is installed with typing in the Terminal:
   
       brew help

   If you get `command not found` output then install brew:
   
       /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
       
   If not then install `Python`:
   
       brew install python3
       
   ### Windows
   
   Go to https://www.python.org/downloads/ and download and install the latest 
   version of `Python`.
   
3. Install `virtualenv`:

       sudo pip install virtualenv
       
   While installing you will be asked for a password. Type your user account 
   password. 
   
   Create the virtual environment:
   
       virtualenv -p python3 ~/venv/fish_tracing
   
   `~/venv/fish_tracing` can be replaced with a custom path.
   
4. Activate the virtual environment:

       source ~/venv/fish_tracing/bin/activate
       
5. Move to the package directory:

       cd <path>
       
6. Install requirements

       pip install -r requirements.txt
