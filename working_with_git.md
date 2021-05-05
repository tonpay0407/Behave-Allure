Below steps to upload your local project in GitHub:

Prerequisites: 

Git Bash should be installed.

Existing GitHub account

 1. Right click in the project folder and click - Git bash here

2. Type command - git init

3. A folder would have appeared in the project folder : .git

4. Make a new repository for this project in GitHub

6. Add all project files to repository , using command:  git add . - which adds all the files in the folder

7.  Git status - command will show all files which are staged

8. Commit the files from your local repo - using command: git commit -m "some message"

9. Copy URL of Remote repository as shown below - 

10. Use - git remote add <name> <url>  - where name is the repo name and URL is the one u copied in above step

11. And then push using the remote name : git push <name>

12. After this you will get a prompt to enter user id and password. Once authenticated, project will get uploaded in GitHub.

13. Use git branch - to see the current branch- as we have only 1 branch, 'master' will come here

14. Go to GitHub - you should be able to see the uploaded files.




