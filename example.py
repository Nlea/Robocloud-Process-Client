import robocorp_process_client

import os
from dotenv import load_dotenv 


load_dotenv()
workspace_robo = os.environ.get('WORKSPACEID-ROBOCLOUD')
process_robo = os.environ.get('PROCESSID-ROBOCLOUD')
authorization_robo = os.environ.get('AUTHORIZATION-TOKEN-ROBOCLOUD')


RoboClient = robocorp_process_client.client.Client(workspace = workspace_robo, process = process_robo, authorization = authorization_robo, endpoint ='https://api.eu1.robocorp.com/process-v1', pollingForRobocloud = 30)


State = RoboClient.startProcess()
print(State)