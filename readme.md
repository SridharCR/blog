# Blog with Flask
A simple blog with basic functionalities to register, login, post and to read blog posts. The goal is to create a wonderful fully functioning blog and to learn those concepts behind it. 

Flask is a light weight web framework based on python. It helps to create simple WSGI for requests and responses.

## Prerequisite
Run the python script to install the required modules for running the application. Run the python script with the 
specified args. This installs the packages in the requirements.txt file.
```sh
$ python setup.py setup
```
Now the required packages are installed now. Go ahead and run the application.
```shell script
$ python setup.py run
```
The flash application with the WSGI server is up and running.

## Design 
The application follows MVC pattern. The *Model-View-Controller* helps to design robust software. Blog application is currently evolving to MVC. 
The controllers owns the business logic, and does the computation, and written with the light weight flask framework.
The models owns the code which interacts with the database, the controllers directly imports model whenever they are needed.
The views owns the complete front end written in the react library. 

![MVC pattern](mvc.jpg)

## REST APIs
The rest apis carry out operations like, create post, update post, and delete post.

## Data
The data are being stored in the open source relational databases, Mysql. Though various ORMs such as SQLAlchemy are available, this application is written in the traditional way, inorder to have strong boundary between the data and code.

## Test
Unit test are yet to be done

## References:
1. Flask Documentation: https://flask.palletsprojects.com/en/1.1.x/
2. Martin Fowler, Design of Enterprise Application Architecture: http://ce.sharif.edu/courses/97-98/2/ce418-1/resources/root/Books/Patterns%20of%20Enterprise%20Application%20Architecture%20-%20Martin%20Fowler.pdf
3. CORS Issue: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
