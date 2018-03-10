# Create a Github repo from the command line


Replace USER with your github user name, replace REPO with the name of your new 
repo. 

```console
$ curl -u 'USER' https://api.github.com/user/repos -d '{"name":"REPO"}'
$ touch README.md
$ git init
$ git add .
$ git commit -am "initial"
$ git remote add origin https://github.com/username/Hello-World.git
$ git push origin master
```
