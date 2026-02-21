# Welcome to the Smart Parking System project.

This repository contains a smart parking system implementation for the COE 892 project at TMU. A quick description of each folder:
- `client/`: Vue.js-based frontend. This is the web client.
- `server/`: The Python-based backend server. (TO BE ADDED)
- `database/`: The database for the project. (TO BE ADDED)

To set up this project on your local machine, follow the steps outlined below.

> Note: This project is currently ongoing. Setup / running steps will continuously be updated throughout the project's duration.

## Project Setup
### Prerequisites
This project requires the following:
- Python 3.12+
- Node.js 24.13.0+
- Vue Extension for VS Code

If you do not have the required dependencies, follow the steps below, otherwise skip to [First Setup](#first-setup).

> Note: The steps below assume you are running Windows, and using VS Code to edit.

#### 1. Python Installation
Python can be installed from the official downloads page [here](https://www.python.org/downloads/). Select the appropriate version from the list and follow the instructions on the installer.

#### 2. Node.js Installation
The frontend uses Vue.js as its framework, which requires npm (and Node.js) to run. There are multiple ways to install Node.js, but the easiest is through the Node Version Manager:
 
 > Detailed steps about this process can be found on [Microsoft Learn](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows). The steps below are a summary of this process.

 1. The NVM installer can be found [here](https://github.com/coreybutler/nvm-windows/releases). Follow the steps on the installer to complete the process.
 2. Open up a new Terminal window (CMD Prompt, Powershell, etc.) with administrative permissions.
 3. Enter `nvm install lts` to install the latest long-term-support version of Node.js. Wait for it and its corresponding version of npm to install.
 4. Enter `nvm ls`. You should see your Node.js and npm installations listed- if yes, then the installation was successful.

 #### 3. Vue Extension Installation
 Go to the extension panel on VS Code and look for `Vue (Official)`. The publisher is vue.js.org. Alternatively, you can find the link to the extension [here](https://marketplace.visualstudio.com/items?itemName=Vue.volar). Click install, and you should be good to go. This extension is required for TypeScript to recognize the .vue files in the project.

### First Setup
1. Clone the repository to your intended directory:
```git bash
git clone https://github.com/SK917/smart-parking-system.git
```
> Note: Ignore server setup steps for now, since this portion has not been implemented.
2. We will setup the backend first. Go to the `server` directory:
```bash
cd server
```
3. Create a virtual environment (venv) to manage the requirements for the project; this ensures that the project remains stable in case different team members have different Python setups.
```bash
python -m venv venv
```
4. Activate the venv:
```bash
venv\Scripts\activate
```
5. Install the required plugins with this command:
```bash
python -m pip install -r requirements.txt
```
6. The backend should now be setup. Now, switch to the `client` directory to setup the frontend:
```bash
deactivate #deactivates the venv
cd ..\client

#Or open a new terminal instance and:
cd client
```
7. Install the required dependencies and plugins by using the following command:
```bash
npm install
```

After completing these steps, you have successfully setup the project! We can now try and run it.

## Running the Project
It is recommended to have two terminal windows active - one for the frontend and one for the backend.

### 1. Run the Backend
> When the Python server is implemented, steps will be shared here.

### 2. Run the Frontend
1. Navigate to `..\smart-parking-system\client`

2. Run the frontend:
```bash
npm run dev
```

The frontend uses the default Vue.js endpoint of http://localhost:5173. Currently, there are no additional endpoints, but we are looking to add some in the future.

### Stopping the Project
To shut down the project, simply:
1. Kill the frontend process by using `Ctrl + C` (then select Y to close the process) or close the terminal instance.

## Updating the Project
> Whenever the project is updated, if it affects this documentation, the README must be updated.

### Updating the Frontend
Sometimes, new dependencies will be installed on the frontend. To adapt them into your local version, simply do the following:

1. Verify that the frontend isn't running.

2. Run `npm install` to install the new plugins.

3. Run `npm run dev` to start up the site again.

That's it!

### Updating the Backend
Any new dependencies required for the venv must be noted in the `requirements.txt` file for teammates to easily install.

1. Verify that the backend ins't running, and activate your venv by using `venv\Scripts\activate`.

2. Use `pip freeze > requirements.txt` to update the requirements.txt file.

To install new dependencies noted by a team member, make sure the venv is activated and then:
```bash
python -m pip install -r requirements.txt
```

This installs any missing dependencies that are noted in `requirements.txt`.