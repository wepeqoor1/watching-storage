# Bank security console

Watch bank security panel.  
The application shows: 
> Active passcards  
User visits  
Who is in bank storage  
How much time visitors spent in storage    
Shows visits for suspicion

## Environment requirements
Python3.10+

## How to install
```bash
$ pip install -r requirements.txt
```

## Environment variables
Create `.env` file and put database connections:  
HOST=<`HOST`>  
PORT=<`PORT`>  
NAME=<`NAME`>  
USER=<`USER`>  
PASSWORD=<`PASSWORD`>  
>A boolean that turns on/off debug mode.  
Never deploy a site into production with DEBUG turned on.  
One of the main features of debug mode is the display of detailed error pages.  
If your app raises an exception when DEBUG is True, Django will display a detailed traceback,  
including a lot of metadata about your environment,  
such as all the currently defined Django settings (from settings.py).`  

DEBUG=<`DEBUG`>  


## How to use
```bash
$ python3 manage.py runserver
```

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.