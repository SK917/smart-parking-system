# Welcome to the Smart Parking System project.

This repository contains a smart parking system implementation for the COE 892 project at TMU. A quick description of each folder:
- `client/`: Vue.js-based frontend. This is the web client.
- `database/`: The database for the project.
- `server/`: The Python-based backend server processes.

To set up this project on your local machine, follow the steps outlined below.

## Project Setup
### Prerequisites
This project requires the following:
- Python 3.12+
- Node.js 24.13.0+
- Vue Extension for VS Code
- gRPC Web Proxy Executable

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

 #### 4. gRPC Web Proxy Executable
 Visit the [grpc-web](https://github.com/improbable-eng/grpc-web/releases) repository and download the latest release that's compatible with your machine. Rename the file to `grpcwebproxy.exe`. Note it's location on your computer as you will need to migrate it into the cloned repository later.

### First Setup
1. Clone the repository to your intended directory:
```git bash
git clone https://github.com/SK917/smart-parking-system.git
```
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
6. Move `grpcwebproxy.exe` to the top level directory of the server. It should sit on the same level as `client_interface.py`, `database_interface.py`, etc..

7. The backend should now be setup. Now, switch to the `client` directory to setup the frontend:
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
It is recommended to have **8** terminal windows active - one for the frontend, then one for each backend service.

### 1. Run the Backend
For each step below, repeat the following prerequisite steps:
1. Open a new terminal instance.

2. Switch to the `server/` directory (ex. `cd server`)

3. Activate the venv by running `venv\Scripts\activate`

In total, you will need to do the above steps 7 times to have 7 terminal instances. After that, you can start running each backend service:

> Note: The Database Interface **MUST** be run first, but apart from that, the setup order for the backend services doesn't matter.

#### 1. Database Interface
This service facilitates database read and write requests and is available at port 50051.  To run it, use:

```bash
python database_interface.py
```

#### 2. Pricing Calculator
This service handles the parking lot's price calculations and is available at port 50054.  To run it, use:

```bash
python pricing_calculator.py
```

#### 3. Transaction Handler
This service handles transactions needed to make reservations and is available at port 50055.  To run it, use:

```bash
python transaction_handler.py
```

#### 4. Client Interface
This service handles any interactions with the frontend and is available at port 50052.  To run it, use:

```bash
python client_interface.py
```

#### 5. IoT Sensor Service
This service handles IoT sensor updates and is available at port 50053.  To run it, use:

```bash
python iot_sensor_service.py
```

#### 6. IoT Sensor Simulator
This service actually simulates the IoT sensors and communicates with the IoT Sensor Service.  The commands to use the simulator are as follows:

`iot_sensor_simulator.py --serial SERIAL [--occupied] [--free]`   

> For our purposes, the SERIAL = the lotID combined with the spotID. The lotID is always 1. Ex. if you want to affect spot ID 19, SERIAL = 119.

**TO OCCUPY A SPOT:**
```bash
python iot_sensor_simulator.py --serial SERIAL --occupied
```

**TO VACATE A SPOT:**
```bash
python iot_sensor_simulator.py --serial SERIAL --free
```

This is a user-operated service so it will need to be manually triggered during run time.

#### 7. Setting up the gRPC Proxy
The proxy service creates an endpoint at port 8080 to facilitate a connection between the frontend and the Client Interface.  To run it, use:

```bash
.\grpcwebproxy.exe --backend_addr=localhost:50052 --run_tls_server=false --allow_all_origins --server_http_debug_port=8080
```

> Note: Windows may ask you to grant permissions to the application for it to work: select "Allow" or whatever equivalent option exists. Additionally, if you run into errors, double check that the executable is in the right location. This is detailed in the Prequisites section [here]((#4-grpc-web-proxy-executable)).

### 2. Run the Frontend
1. Open a new terminal instance and navigate to `..\smart-parking-system\client`

2. Run the frontend:
```bash
npm run dev
```

The frontend uses the default Vue.js endpoint of http://localhost:5173. There are no additional endpoints to note.

### Stopping the Project
To shut down the project, simply:
1. Kill the frontend process by using `Ctrl + C` (then select Y to close the process) or close the terminal instance.

2. Kill each backend process by using `Ctrl + C` to interrupt each process or simply close each terminal instance. 
> Note: For backend processes, you **MUST** end the Database Interface service **LAST**. Apart from that, the order doesn't matter.

## Updating the Project
> Whenever the project is updated, if it affects this documentation, the README must be updated.

### Updating Frontend Plugins
Sometimes, new dependencies will be installed on the frontend. To adapt them into your local version, simply do the following:

1. Verify that the frontend isn't running and navigate to the frontend directory, `..\smart-parking-system\client`.

2. Run `npm install` to install the new plugins.

3. Run `npm run dev` to start up the site again.

That's it!

### Updating Backend Dependencies
Any new dependencies required for the venv must be noted in the `requirements.txt` file for teammates to easily install.

1. Verify that the backend ins't running, and activate your venv by using `venv\Scripts\activate`.

2. Use `pip freeze > requirements.txt` to update the requirements.txt file.

To install new dependencies noted by a team member, make sure the venv is activated and then:
```bash
python -m pip install -r requirements.txt
```

This installs any missing dependencies that are noted in `requirements.txt`.

### Updating gRPC proto files
When proto file updates are made in the backend, their corresponding backend services must be updated as well.  However, there is an additional step required in the frontend to generate new proto stubs in the `proto/` directory.

1. Navigate to the frontend directory: `..\smart-parking-system\client`

2. Run the following script to update the proto stubs:

```node
npm run gen-proto2
```

This generates new proto stubs. Make sure to update the relevant connecting services (`parking-service.ts` and `parking-store.ts`) to ensure proper connectivity.

> Note: You will need to setup protoc on your System PATH to run this script; it is not included in project pre-requisites since proto file updates are rare and not required for every developer.