"""
A initial setup for the project
Running this script will install the required packages for this application
For more info for the packages used, check requirements.txt
Arguments - "setup"

A script to run the flask application
Arguments - "run"

"""
import os
import sys
import subprocess

def initial_setup():
    try:
        file_object = open('requirements.txt')
        modules = file_object.read().split('\n')
        file_object.close()
        print(modules)
        for module in modules:
            subprocess.call(["pip", "install", module])

    except Exception:
        print("Error occured while setup")

def run_flask_app():
    # Executing the virtual environment
    os.chdir("venv/Scripts")
    os.system("activate")
    os.chdir("../..")
    # Running the flask application
    if os.name == 'nt':
        os.system("set flask_app=src")
        os.system("set flask_debug=true")
    else:
        os.system("export flask_app=src")
        os.system("export flask_debug=true")
    os.system("flask run")

if __name__ == "__main__":
    if sys.argv[1] == "setup":
        initial_setup()
    elif sys.argv[1] == "run":
        run_flask_app()
    else:
        print("Specify the operation in the argument")
