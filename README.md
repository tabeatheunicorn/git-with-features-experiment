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

1. **Clone the Repository**

   ```cmd
   git clone https://github.com/tabeatheunicorn/git-with-features-experiment.git
   ```

1. **Run the Python Script**

   ```
   cd git-with-features-experiment
   ```

   ```cmd
   python src\main.py
   ```

   Running the script will not be required during the experiment, but it can help you understand the project's functionality.

## 2. Setting Up the Tool

1. **Fetch Required Branch**

   The `feature-metadata` branch must be available locally:

   ```cmd
   git fetch origin feature-metadata
   ```

1. **Download the Tool**

   Download [git_tool](https://drive.google.com/uc?export=download&id=1GZ9QkY53TlQqfT6Ckz9QegmVk8Nuj0Gg).

1. **Install the Tool**

   ```cmd
   python -m pip install <prefix>/git_tool-<version>-py3-none-any.whl
   ```

   **Note: Please use the path where your file is stored. On Windows systems, this will usually be the Downloads Folder.
   For this command, the path of execution won't matter.**

1. **Test the Installation**

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

1. **Set Up Git Hooks**
   The Hooks are needed for

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

