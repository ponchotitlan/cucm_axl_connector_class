from CUCMConnectorAXL import *
import logging

class CUCMOperator(CUCMConnectorAXL):
    def get_device_model(self,device_enum):
        """Returns the model of the input device enum"""

        response = self._CLIENT.executeSQLQuery(
            **{
                'sql': f'select name from typemodel where enum={device_enum}'
            })
        try:
            return response['return']['row'][0][0].xpath("string()")
        except Exception as e:
            if self._logger:
                self._logger.error(str(e))
            else:
                logging.error(str(e))
            return False

    def get_device_amount(self):
        """Returns the amount of devices in the node"""

        response = self._CLIENT.listPhone(
                searchCriteria = {'name':'%'},
                returnedTags = {'name':''}
            )
        return len(response['return']['phone'])

    def get_devices_information(self):
        """Returns a list with specific features of devices"""

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

    def add_csf_device(self, device_name, lines):
        """
            Creates a Jabber device with the specified settings
            This example takes as default many of the common settings, although it can be adjusted according to your needs
        """

        phone={
                    'name': device_name,
                    'product': 'Cisco Unified Client Services Framework',
                    'class': 'Phone',
                    'protocol': 'SIP',
                    'protocolSide': 'User',
                    'devicePoolName': 'Default',
                    'locationName': 'Hub_None',
                    'sipProfileName': 'Standard SIP Profile',
                    'commonPhoneConfigName': xsd.SkipValue,
                    'phoneTemplateName': xsd.SkipValue,
                    'primaryPhoneName': xsd.SkipValue,
                    'useTrustedRelayPoint': xsd.SkipValue,
                    'builtInBridgeStatus': xsd.SkipValue,
                    'packetCaptureMode': xsd.SkipValue,
                    'certificateOperation': xsd.SkipValue,
                    'deviceMobilityMode': 'Off',
                    'lines': {
                        'line': lines
                    }
                }

        try:
            return self._CLIENT.addPhone(phone)
        except Exception as e:
            if self._logger:
                self._logger.error(str(e))
            else:
                logging.error(str(e))
            return False