# python-voice-recognition

## "Human-Computer Interaction" project to move on a grid using voice commands

### To run the project:

1. **Make sure you have Python and the pip dependency installed**.

2. **Install your virtual environment** with the following command:

   ```bash
   python -m venv venv
   ```

3. **Initialize the virtual environment**. On Windows, use the following command:

   ```bash
   .\venv\Scripts\activate
   ```

   **NOTE**: If on Windows you get an error mentioning that scripts cannot be run on the system, enter the following command in a PowerShell terminal with administrator privileges:

   ```bash
   Set-ExecutionPolicy Unrestricted -Scope CurrentUser
   ```

   To open PowerShell with administrator privileges, press `Windows + X` and select "Windows PowerShell (Admin)" or "Terminal (Admin)". Once this is done, initialize the virtual environment as mentioned in this step.

   Your terminal should have `(venv)` added at the beginning of the directory path:

   ```plaintext
   (venv) C:\path\
   ```

4. **Once the virtual environment is initialized, install the project** with the following command:

   ```bash
   pip install -e .
   ```

   *(Note the dot, it must be run exactly from the root of the directory)*

5. **Once the project is installed**, you can run it with the following command:

   ```bash
   run_ihc_app
   ```

