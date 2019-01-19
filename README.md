# Jenkins, Docker and Python pytest demo

This project demonstrates how to isolate a Python development environment
from the OS using Docker. As a bonus, this project also shows how to
run Python [pytests](http://doc.pytest.org/en/latest/)
in Jenkins.



## Demos

# Python demo

```
git remote -v show
tree
python -m maxsum.main.main
python3 -m maxsum.main.main
python3 -m pytest
```

# Docker demo

```
docker rmi maxsum:build
docker rmi maxsum:manual
docker images
docker build --tag maxsum:manual .
./run python --version
./run python -m maxsum.main.main
./run python -m pytest
```

# Jenkins demo

* Look at Jenkins configuration
* Build in Jenkins
* Look at Jenkins stages durations
* Build again in Jenkins
* Look at Jenkins stages durations

# Break a test demo

```
./run python -m pytest
git push origin master
```

* Build in Jenkins
* Look at tests results in Jenkins

