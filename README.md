# errors management system

This repo help to manage all the errors we've got from our system or production environment. Each time you notice a new error, you can add it to the local DB managed by MongoDB. In addition, you can do other actions like fetch and delete.  
This project build contains three services (server-side, clienclient-sideDB) managed by docker-compose. 

requirements: 
  - having docker installed locally.
  - having git installed locally.

How to run the project?
1. clone the repo by the command "git clone https://github.com/EASS-HIT-2022/errors-management-system.git". 
2. move to the repo folder by "cd /errors-management-system." 
3. check the items you have inside the folder. You are in the correct folder if you have backend, frontend and docker-compose.yml and readme. 
4. send the command: "docker-compose up." In the logs, you can see that all the services are running well, and the UI is running on port:8501.
5. go to "http://localhost:8501" in your browser. 
6. On the left side, you can see a nav bar with three actions: Add a new error, fetch error and delete error. By tying the error name, you can manage the history of the errors you noticed. 
7. when you finished with the application you can close the server by: "Ctrl+C". 

The next video can illustrate how to run the application:
https://user-images.githubusercontent.com/86151424/175379676-725cef42-c707-486a-a6f5-609d4f1bb5be.mp4


