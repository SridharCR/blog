# Blog with Flask
A simple blog with basic functionalities to register, login, post and to read blog posts. The goal is to create a wonderful fully functioning blog and to learn those concepts behind it. 

Flask is a light weight web framework based on python. It helps to create simple WSGI for requests and responses.

## Prerequiste
Run the python script to install the required modules for running the application.
```sh
$ python setup.py
```
This installs the packages in the requirements.txt file.

## Design 
The application follows MVC pattern. The *Model-View-Controller* helps to design robust softwares. Blog application is currently evolving to MVC. 


## Data
The data are being stored in the open source relational databases, Mysql. Though various ORMs such as SQLAlchemy are available, this application is written in the traditional way, inorder to have strong boundary between the data and code.

## References:
1. Flask Documentation: https://flask.palletsprojects.com/en/1.1.x/
2. Martin Fowler, Design of Enterprise Application Architecture: http://ce.sharif.edu/courses/97-98/2/ce418-1/resources/root/Books/Patterns%20of%20Enterprise%20Application%20Architecture%20-%20Martin%20Fowler.pdf
