# Installation Guide

## Prerequisites

- **Git** installed. [Download Git for Windows](https://git-scm.com/download/win)
- **Python 3** installed. [Download Python for Windows](https://www.python.org/downloads/windows/)

## 1. Setting Up the Repository

1. **Verify Installations for Requirements**

   ```cmd
   git --version
   python --version
   ```

   **Note: The actual command for running a python script may vary depending on the system configuration.**

   Ensure that versions are displayed to confirm proper installation.

2. **Clone the Repository**

   ```cmd
   git clone git@github.com:tabeatheunicorn/git-with-features-experiment.git
   ```

3. **Run the Python Script**

   ```
   cd git-with-features-experiment
   ```

   ```cmd
   python src\main.py
   ```

   Running the script will not be required during the experiment, but it can help you understand the project's functionality.

## 2. Setting Up the Tool

1. **Download the Tool**

   Download [git_tool](https://drive.google.com/uc?export=download&id=1GZ9QkY53TlQqfT6Ckz9QegmVk8Nuj0Gg).

2. **Install the Tool**

   ```cmd
   python -m pip install <prefix>/git_tool-<version>-py3-none-any.whl
   ```

   **Note: Please use the path where your file is stored. On Windows systems, this will usually be the Downloads Folder.
   For this command, the path of execution won't matter.**

   The installation process automatically places the scripts in a specific directory, and it's important that this directory is part of your system's PATH for Git to recognize the tool's commands.
   - **Linux**
     You may see a warning like this
     ```bash
     WARNING: The scripts git-feature-add, git-feature-blame, git-feature-commit, git-feature-commit-msg, git-feature-commits, git-feature-info, git-feature-pre-commit, and git-feature-status are installed in '/home/<user>/.local/bin' which is not on PATH.
     ```
     Please either copy all scripts starting with `git-` to a location in your `PATH` or add this folder to your `PATH`.
   - **Windows**
     The scripts are usually installed in the Scripts folder inside your Python installation directory (e.g., C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX\Scripts). Make sure this directory is included in your system’s `PATH`, or Git will not be able to recognize the installed commands.

4. **Test the Installation**

   - **Display Feature Commands**

     In the repository directory, type:

     ```cmd
     git feature-
     ```

     Press the **Tab** key to see available feature commands. If this does not work, your Git autocompletion may not be enabled. Try the next step. If it works, your installation is complete.

   - **Run Feature Info Command**

     ```cmd
     git feature-info
     ```

     You should see an output similar to:

     ```
     Branch feature-metadata successfully created.
     ```

5. **Set Up Git Hooks**
   
   The hooks are required to ensure that feature information is added before committing files. This step can be skipped if you plan to add feature information only to existing commits using the `git feature-commit` command, bypassing the need for `git feature-add` and its subcommands. Information about the subcommands can be found [here](https://docs.google.com/document/d/1BoQP8FSRB7vCYs05UdXBuX9dW5ALBMzp5diTdYCP7BM/edit?usp=drive_link).
   - **Find the Tool Path**

     ```cmd
     python -c "import git_tool; print(git_tool.__file__)"
     ```

     This will output a path ending with `__init__.py`.

   - **Locate the Hooks Directory**

     Remove `__init__.py` from the path and append `hook` instead. For example:

     ```
     C:\Users\YourName\AppData\Local\Programs\Python\Python39\Lib\site-packages\git_tool\hook
     ```

   - **Set the Hooks Path**

     In your repository directory, run:

     ```cmd
     git config core.hooksPath <path>
     ```

     Replace `<path>` with the path you found in the previous step.

   - **Check the Git Hooks Path**

     In your repository directory, run:

     ```cmd
     git rev-parse --git-path hooks
     ```

     This should display the path you set in the previous step.


## Notes
- **Potential Fix**: The requirement to have the `feature-metadata` branch locally may be addressed in future updates.

