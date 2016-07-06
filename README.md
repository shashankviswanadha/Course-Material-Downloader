ABOUT:

This script downloads all the course content from the Moodle page of Mahindra Ecole Centrale. It organises the files into their course directories. You can run the script whenever there are some new files uploaded on moodle and it will only download the newly added files. This way, you will never have to open the dull looking moodle page to go through each link and download each file. Enjoy!

REQUIREMENTS:

This application requires python version 2.7 and its some of its packages:

1. bs4
2. requests
3. os
4. getpass

INSTALLING PYTHON AND DEPENDENCIES:

-UBUNTU USERS:

 Run the following commands in a terminal
 
  $ sudo apt-get update
  $ sudo apt-get install python
  $ sudo apt-get install python-bs4
  $ sudo apt-get install python-requests
  $ sudo apt-get install python-getpass (ignore if already there)
            
-WINDOWS FREAKS:

  1. Installing git: Download git from this link (https://git-for-windows.github.io/) and install it
  2. Installing python: Follow the instructions on this page (the 1st answer) to download, install and set the path for python.
  3. Installing pip: Open a command prompt as adminstrator and run this command: python get-pip.py
  4. Installing dependencies: run the following commands:
                             1. python.exe -m pip install requests
                             2. python.exe -m pip install bs4
                             3. python.exe -m pip install getpass (ignore if already there)
  5. Now, you're actually ready to download the application. So, thats why I called you freaks (So many things to install!)


INSTALLING AND RUNNING THE 'Moodownloader':

-Both Ubuntu users and Windows freaks:

 Open a terminal/command prompt and run the following commands:
 
  $ git clone https://github.com/shashankviswanadha/Course-Material-Downloader.git
  $ cd Course-Material-Downloader
  $ cd src
  
 Now open the config.py file in your editor and set your path ,wherever you want it to be and save the file. (There is an example to guide you)
 Now run the application using the command:
  $ python main.py
  
 You will have to enter your moodle userid and password and also the semester number and your year of joining(2015/2014).
 Then you have to enter 'all' to download all courses in the semster or enter the precise course name to download a single course.
 You will find a folder named 'Moodownloader' in the path you set which has all your downloads.
 
 Enjoy and hope this helps.
 




         
