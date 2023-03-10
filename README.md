# Task 1 - elevatus-selenium-pytest
## Selenium-Pytest-Automation-Framework Demo
### Objective:
Elevatus "https://automations.elevatus.io/" is an employee and candidate portal. The task given was to register as a candidate and apply for a job using the 'fill in manually' link.
Selenium automation with python is used to register user on Elevatus, verify registration through imaplib, login as a candidate andd then fill in the "Submit you CV form" with the required fields to complete the job application process.

### Installation:
You can use any IDE to implement and run automated script using python. VSCode and PyCharm are recommended.

#### First install python 
* For Windows:
Download python from this link https://www.python.org/ description of how to install python is mention in this page https://www.tutorialspoint.com/how-to-install-python-in-windows 

* For Linux:
Run this command into your terminal `sudo apt-get install python3`

* For MacOS:
Downloadd the latest stable release from https://www.python.org/downloads/macos/ and follow the installation instructions.

#### IDE: 
You can use any IDE to implement and run automated script using python. 
Download Pycharm https://www.jetbrains.com/pycharm/download/ or VSCode https://code.visualstudio.com/download. I have used VSCode for this project.

#### Install Dependencies:
* For Linux or Windows:
In the terminal of source code install requirement.txt file by running this command:
 `$ pip install -r requirement.txt`

* For MacOS:
In the terminal of source code install requirement.txt file by running this command:
 `$ pip3 install -r requirement.txt`
 
 ### Run
 Run project using this command into project terminal
`python3 -m pytest --browser=chrome --html=reports/report.html`

* `python -m pytest --browser=chrome --html=reports/report.html` to run on windows.
* The --browser flag tells which browser to run on. The three option are chrome, firefox and edge at the moment.
* The --html flag directs to the folder in which the report is to be saved and the report name.


# Task 2 - Running a Postman Collection with Newman
## Installing Newman

 `npm install -g newman` 

 - This will install Newman globally on your system.

 ## Running Postman Collection

 - Once you have Newman installed, you can run a Postman collection from the command line using the following command

`newman run JobTitles.postman_collection.json;`








