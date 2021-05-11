# H.I.V.E: 1.0.4 BETA #
![up](https://user-images.githubusercontent.com/80300015/117555900-52d31100-b0b7-11eb-9775-94d4e947fae1.png)

Home-Assistant Intergrated Virtual Enviroment
https://natebrownprojects.github.io/TheHiveProject/

RELEASE NOTES ARE NOW AVAILABLE!
## Setup Step 1
Clone this repository using the following command:
``` cd Documents```
``` mkdir hive ```
``` cd hive ```
``` sudo git clone https://github.com/NateBrownProjects/TheHiveProject.git```

Then enter the repository by using the following command:
```cd TheHiveProject/```
## AUTOMATIC SETUP:
To automaticlly setup H.I.V.E, just simply type the following command:
``` sh setup.sh ```  

## MANUAL SETUP:
Setup a Python Virtual Environment by using the following command:
```pip install virtualenv```


Then Create the VENV:
```virtualenv TheHiveProject```

### Then activate the VENV: ###

MacOS/Linux: ```source TheHiveProject/bin/activate```

Windows: ``` TheHiveProject/Scripts/activate```


## Setup Step 2

Then, install all requirements by using the following command:
```"pip install -r requirements.txt"```

To Run H.I.V.E:
```sh hive.sh```



Please note that this is a very basic Assistant and will be developed heavily over the months
## Commands you can use! ##

- Tell me a joke!
- Who is...
- Whats the time
- exit / shutdown
- hello!
- Who are you?
- Play... 
- Whats the Date today?
- Manually Type in your Commands
- Use Calculator using the command: "calculator"
- Weather: "weather, rain, wind, temprature, cloud"


## UPDATING ##

### To update, use the following commands ##
``` cd hive/TheHiveProject ```
``` git pull ```

# USAGE
## TO use H.I.V.E, there are 2 ways to load and run H.I.V.E.
### 1st, ```sh hive.sh```
### 2nd, ```hive``` To use this, you must have V.1.0.4 BETA or later. If this doesnt work for you then run the 2 following commands.
###  Command 1. ``` chmod +x .hivec.sh ```
### Command 2. ``` source .hivec.sh ``` If this still doesnt work, please contact us or open an issue and we'll  be happy to help.