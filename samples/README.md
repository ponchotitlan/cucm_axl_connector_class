### Inheritance and flexibility
One of the main purposes of this class is to provide granularity for the creation of CUCM integrations. It is a good idea to use it as a base class for inheritance, where the child contains the specific AXL queries (GET, LIST, ADD, UPDATE, DELETE).

The class **CUCMOperator** bundled in this repository is an example of the mentioned granularity. This class contains usage examples for GET, ADD and LIST operations, as well as raw SQL queries to the InformixDB within CUCM:

```
class CUCMOperator(CUCMConnectorAXL):
    def get_devices_information(self):
        response = self._CLIENT.listPhone(
            searchCriteria = {'name':'%'},
            returnedTags = {
                'name':'',
                'product':'',
                'model':'',
                'class':''
                }
        )
        return [x['name'] for x in response['return'].phone]
```

With this level of granularity, the usage can be as simple as the following:

```
TARGET_CUCM = CUCMOperator(CUCM_IP,CUCM_USERNAME,CUCM_PASSWORD,debug=True)
if(TARGET_CUCM.isValid()):
    device_information = TARGET_CUCM.get_devices_information()
```

This repository contains one proposed in the * *app_example_createCSF.py* * file for creating a CSF (Jabber) device from scratch. 

This repository will be continuously updated with more examples for covering the usage of the different actions in AXL.

For more information about the latest AXL schema, visit [this page](https://developer.cisco.com/docs/axl-schema-reference/).

Crafted with :heart: by [Alfonso Sandoval - Ponchotitlán](https://www.linkedin.com/in/asandovalros)