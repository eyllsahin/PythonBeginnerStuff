'''Why do we use virtual environments at all?
Problem Without venv:

If you install packages with pip install globally:
All projects share the same environment.
One project may require Django==3.2, another Django==5.0 → conflicts happen.
Upgrading a package for one project might break another.
You may accidentally overwrite or delete packages required by the system.

What venv Does:

venv creates a project-specific Python environment:
Isolated from global packages.
Lets you install exactly what that project needs.
Keeps dependencies organized (like numpy, requests, etc.).
Prevents version conflicts between different projects.
Allows reproducibility: your requirements.txt works the same everywhere.

So how do we install it,run it?
Since I used Windows, I wrote wsl in cmmd
pip install virtualenv
I tried this command, but it gave me an error

error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

So the right way to do it as follows:
 sudo apt install virtualenv

 it will give you this:

 Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  virtualenv
0 upgraded, 1 newly installed, 0 to remove and 61 not upgraded.
Need to get 1978 B of archives.
After this operation, 13.3 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu noble/universe amd64 virtualenv all 20.25.0+ds-2 [1978 B]
Fetched 1978 B in 1s (1727 B/s)
Selecting previously unselected package virtualenv.
(Reading database ... 64138 files and directories currently installed.)
Preparing to unpack .../virtualenv_20.25.0+ds-2_all.deb ...
Unpacking virtualenv (20.25.0+ds-2) ...
Setting up virtualenv (20.25.0+ds-2) ...

Then,
sudo apt install pip

Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'python3-pip' instead of 'pip'
python3-pip is already the newest version (24.0+dfsg-1ubuntu1.2).
0 upgraded, 0 newly installed, 0 to remove and 61 not upgraded.

if you want to see all the packages and their version
pip list

Make a directory for keeping all the venvs in an organized place
mkdir Environments
cd Environments /you will be inside the dir now
virtualenv projest1_env /create the first venv, it will install setup tools and pip for you
source projest1_env/bin/activate /to activate, you will be in the venv now
pip list
pip install numpy /or whatever package you want to install in the venv

When you install packages you want, you can say  'pip list' to see them
pip list
Package Version
------- -------
numpy 2.3.1
pip   25.1.1
psutil  7.0.0
pytz    2025.2


pip freeze --local /Takes only the local dependencies you have on your python venv
numpy==2.3.1
psutil==7.0.0
pytz==2025.2


If you want to get out of the venv
deactivate
this command will get you out


If you want to delete it
rm -rf project1_env/


'''