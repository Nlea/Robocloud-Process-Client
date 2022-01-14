# Robocloud-Process-Client
Run your [Robocloud Processes](https://robocorp.com/docs/courses/beginners-course/running-in-robocorp-cloud) in Python3.

The client connects to the [Robocorp process API](https://robocorp.com/docs/control-room/apis-and-webhooks/process-api). 

Requirement: In order to use the Robocorp Process API a [paid plan](https://robocorp.com/pricing) is needed


## Credentials
In order to connect to your Robocorp  account create a .env file in your project and include the following information: ''

```
AUTHORIZATION-TOKEN-ROBOCLOUD = 'RC-WSKEY xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
PROCESSID-ROBOCLOUD = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
WORKSPACEID-ROBOCLOUD = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
```

## Start a process in Robocloud

```python

RoboClient = robocloudClient.client()

State = RoboClient.startProcess()
print(State)

```

*Note: At the moment each process in Robocloud consist one RF-Task, so it returns the [State of one work-item](https://robocorp.com/docs/development-guide/control-room/work-items). 
