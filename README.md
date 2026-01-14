## IEEE-2026
Robot code for the 2026 IEEE competition. Details about the status of the project can be found here: https://github.com/orgs/Gold-Rush-Robotics/projects/8



## Getting Started

The easiest way to contribute to this repository is using the DevEnv, which will have installation instructions below.
If you'd rather use a native ROS2 install or some other method, I trust you can figure it out :)

1. Download Docker: https://docs.docker.com/engine/install/

2. Run this command in your terminal to pull the docker image (it will take a while): `docker pull ghcr.io/roboeagles4828/developer-environment:8` 

3. Run this command to clone the repo. Make sure you do this in a place you can find, such as a projects folder: `git clone https://github.com/Gold-Rush-Robotics/DevEnv.git --branch jazzy`
3.a if you get something like "command not found git" then you need to install git first: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

4. Install vs code: https://code.visualstudio.com/download

5. Install the dev containers extension: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

6. Open the repo you cloned earlier in vs code

7. open the command pallete 
    -all platforms: f1 
    -mac: cmd+shift+p 
    -windows/Linux: ctrl+shift+p

8. run `>dev containers: Rebuild and Reload in container` or something similar they like to change the name arround

9. you should see something like this when it is done, hit enter and then open a new terminal
![alt text](https://github.com/Gold-Rush-Robotics/IEEE-2026/raw/main/images/rebuild_and_reload.png "rebuild_and_reload")

10. run `ros2 wtf` in the terminal, you should see an output like this
![alt text](https://github.com/Gold-Rush-Robotics/IEEE-2026/raw/main/images/ros2_wtf.png "ros2_wtf.png")

