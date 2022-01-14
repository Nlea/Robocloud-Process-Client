import robocloudClient

RoboClient = robocloudClient.client()

State = RoboClient.startProcess()
print(State)

