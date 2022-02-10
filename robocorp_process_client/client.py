import requests
import json
import time


class Client:
    def __init__(self, workspace, process, authorization, endpoint ='https://api.eu1.robocorp.com/process-v1', pollingForRobocloud = 30): 
        self.workspace = workspace
        self.process = process
        self.authorization = authorization
        self.endpoint = endpoint
        self.pollingForRobocloud = pollingForRobocloud
        
    def startProcess (self, **payload):
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': self.authorization
        }
        print('header: ' + str(headers))
        
        #parse payload if payload is not empty 
        
        url_startRobo = str(self.endpoint) + '/workspaces/' + str(self.workspace) + '/processes/'+ str(self.process) +'/runs'
        print('url: ' +  url_startRobo)
        
        robocloud = True
        
        try:
            req_startRobo = requests.post(url_startRobo, headers = headers, data =payload)
            print('start Robot: '+ str(req_startRobo.status_code))
            
        except:
            robocloud = False
            print('Error StartProcessRobocorp')
       
       
                
        if(robocloud == True):
            body_startRobo = json.loads(req_startRobo.text)
            workItem =str(body_startRobo['workItemIds'][0])
            print('Workitem: ' + workItem)
            
            
            url_getWorkItem = str(self.endpoint) + '/workspaces/' + str(self.workspace) + '/processes/'+ str(self.process) + '/work-items/' + workItem
          
            req_getWorkItem = requests.get(url_getWorkItem, headers = headers, data=payload)         
            state = "IN_PROGRESS"
            
            while(state == 'IN_PROGRESS'):
                print('waiting for Robot to finish')
                time.sleep(self.pollingForRobocloud)
                
                try:
                    req_getWorkItem = requests.get(url_getWorkItem, headers = headers, data=payload)
                    print('Get work item: ' + str(req_getWorkItem.status_code))
                    body_getWorkItem = json.loads(req_getWorkItem.text)
                    state = str(body_getWorkItem['state'])
                    
                    if(state != 'IN_PROGRESS'):
                        return state 
                
                except:
                    print("Error GetWorkItem")

