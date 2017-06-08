# Getting Started Guide

## 1. Login to the server.
Make sure you have your login info from the following [sheet](https://docs.google.com/spreadsheets/d/1jaO4wKREauvJv2t1zXtVZVfQBuz0PbJpl1yyv3FgEnA/edit?usp=sharing). Now with your credentials open a new terminal and write:

    ssh -l username -p 207 cc3201.dcc.uchile.cl
    
Where username is your own username. You will be asked for your password, write it and click enter.

## 2. How to set your own branch.
A branch is a environment where you can try your own ideas whitout affecting the modifications of your partners. So when you're logged into the server make sure you are working in your own branch. Just write:


      sudo su
    
You will be asked for your password, is the same you used to login to the server. Then to check if you are in your own branch, write:
  
      git branch
 
 If you are in your branch skip the next step. To change to your branch you must use:
 
      git checkout username
      
 where username is the same user you used to login to the server.
 
 ## 3. Save changes with git.
 Before starting doing something, make sure you are working with the last version of the project, to do that just write:
 
      git pull
      
 Now you can make all the modifications you want. When you finish something you can save your changes writting:
  
      git add .
      git commit -m 'write here a message'
      git push
      
Where git add update your local git repository. git commit prepare your changes to be uploaded and git push upload your changes.

## 4. Test your modifications.
Once you finish something, you can test your modifications by writting:

      uwsgi --ini lolapp.ini
      
And then go to [here](http://cc3201.dcc.uchile.cl/grupo07/).
