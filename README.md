# CUCM AXL Connector class

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

Python connector class based on the Zeep library for CUCM deployments via AXL. This is an effort for facilitating the building of integration projects through a straightforward connector class.

This repository contains the main class **CUCMConnectorAXL.py** as well as some implementation examples which will be explained later on

### CUCM setup for AXL interaction
The target CUCM cluster must have an AXL-enabled Application user. This can be achieved by assigning the AXL API Access Group. The Cisco AXL Web Service must be enabled as well. This can be achieved in Cisco Unified Serviceability > Database and Admin Services > Cisco AXL Web Service. 

Once the service has been activated, it is possible to verify by navigating to the following address in a web browser:

```
https://<cucm_server>:8443/axl/
```

The legend * *The AXL Web Service is working and accepting requests. Use HTTP POST to send a request* * must be visible in the loaded page.

### Usage
In order to enable the usage of **CUCMConnectorAXL.py**, the attached requirements must be installed in the project root:

```
pip install -r requirements.txt 
```

The folder * *schema* * must be located in the same directory as CUCMConnectorAXL.py. This folder contains the required xsd files from CUCM in order to enable the creation of structured SOAP messages via AXL.

The **CUCMConnectorAXL** class requires the following parameters:

- AXL_Username (string. Required): AXL-enabled CUCM username
- AXL_Password (string. Required): AXL-enabled CUCM password
- CUCM_IP (string. Required): Target CUCM IP address    
- CUCM_Version (string. Optional): Default is 11.5. The version must match the name of the folder in "schema"
- debug (boolean. Optional): Default is False. Toggle debug plugin for seeing incoming/outgoing SOAP requests in console
- logger (logging instance. Optional): Default is False. Custom logger for ERROR-type messages handling

The raw Zeep connection handler is stored in the * *_CLIENT* * parameter. The successful connection of the created instance can be verified with the * *isValid():boolean* * method included.

This class only contains connection and validation mechanisms. It must be either modified or inherited (see "samples" folder) in order to execute AXL functions.

### Static method for prototyping
Additionally, the original CUCMConnectorAXL class contains a static method for raw client usage. This can come handy for quick prototyping and flexible AXL functions design:

```
from CUCMConnectorAXL import *

TARGET_CUCM = CUCMConnectorAXL.connector(CUCM_IP,AXL_Username,AXL_Password,CUCM_Version = '11.5',debug = False)
TARGET_CUCM.updateRouteList(**{
    'name’: 'MY_ROUTE_LIST’,
    'addMembers':{
        'member’:[
        {
            'routeGroupName’:’NEW_RG_1',
            'selectionOrder':1 
        }]
    }
})
```

Crafted with :heart: by [Alfonso Sandoval - Ponchotitlán](https://linkedin.com/in/asandovalros)
