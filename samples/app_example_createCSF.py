from CUCMOperator import *

CUCM_IP = 'CUCM_IP'
CUCM_USERNAME = 'CUCM_USERNAME'
CUCM_PASSWORD = 'CUCM_PASSWORD'
DEVICE_NAME = 'TestCSF'
DEVICE_LINES=[
    {
        'index':'1',
        'dirn':{
            'pattern':'1001',
            'routePartitionName':'Test_Partition'
        }
    },
    {
        'index':'2',
        'dirn':{
            'pattern':'1002',
            'routePartitionName':'Test_Partition'
        }
    }
]

def main():
    TARGET_CUCM = CUCMOperator(CUCM_IP,CUCM_USERNAME,CUCM_PASSWORD,debug=True)
    if(TARGET_CUCM.isValid()):
        TARGET_CUCM.add_csf_device(DEVICE_NAME,DEVICE_LINES)

if __name__ == "__main__":
    main()