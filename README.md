# Fish tracing

Scripts fro plotting fish traces

## Instalation

This step need to be done only first time using this script on the machine.

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
   
3. If Terminal (MacOS or Linux) or Command prompt (Windows) is not open yet
   open it:<br>
   
4. Install `virtualenv`:

       sudo pip install virtualenv
       
   While installing you will be asked for a password. Type your user account 
   password. 
   
   Create the virtual environment:
   
       virtualenv -p python3 ~/venv/fish_tracing
   
   `~/venv/fish_tracing` can be replaced with a custom path.
   
5. Activate the virtual environment:

       source ~/venv/fish_tracing/bin/activate
       
6. Move to the package directory:

       cd <path>
       
7. Install requirements

       pip install -r requirements.txt
       
## Usage

1. Mac or Linux: open the Terminal app. At MacOS: cmd+space, then type Terminal<br>
   Windows: open the command prompt.

2. Activate the virtual environment:

       source ~/venv/fish_tracking/bin/activate

3. Move to the package directory:

       cd <path>

   e.g.

       cd fish-tracking

5. Run the tracing script:

       python trace_fish_new.py --source <source dir>

   e.g.

       python trace_fish.py --source "data/input/12 Areana Trial 1.xlsx"

   `<source dir>` is the path to the directory with the excel files. <br>

   There are two additional arguments that can be used.

   `--start` defines the second when we start to plot traces (default 0).
   E.g. value 0 means that we start to plot traces 0 seconds after the start
   of the recording <br>
   `--end` defines the second when we end to plot traces (default 1000).
   E.g. value 10000 means that we end to plot traces 10000 seconds
   after the start of the recording.

6. Results are now available in `data/output` directory.


## Usage of old script `trace_fish.py`

1. Mac or Linux: open the Terminal app:  cmd+space, then type Terminal<br>
   Windows: open the command prompt.

2. Activate the virtual environment:

       source ~/venv/fish_tracking/bin/activate

3. Move to the package directory:

       cd <path>

   e.g.

       cd Downloads/Tracking\ Instructions\ and\ Script/fish-tracking
       
4. Copy excel files with traces to the package subdirectory (`<source dir>`).

5. Run the tracing script:

       python trace_fish.py --source <source dir> --destination <destination dir>

   e.g.

       python trace_fish.py --source 3-08-15\ Nicotine\ Experiment/Export\ Files/ --destination 3-08-15\ Nicotine\ Experiment/Orange_Generated_Tracings
       
   `<source dir>` is the path to the directory with the excel files. <br>
   `<destination dir>` is the path to the directory where results files will be saved
   
   There are two additional arguments that can be used when default settings
   are sufficient.
   
   `--start` defines the second when we start to plot traces (default 10).
   E.g. value 10 means that we start to plot traces 10 seconds after the start
   of the recording <br>
   `--end` defines the second when we end to plot traces (default 600).
   E.g. value 600 means that we end to plot traces 600 seconds (10 minutes) 
   after the start of the recording.
   
6. Results are now available at `<destination dir>`.    
