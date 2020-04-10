"""
A initial setup for the project
Running this script will install the required packages for this application
For more info for the packages used, check requirements.txt

"""
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

if __name__ == "__main__":
    initial_setup()
