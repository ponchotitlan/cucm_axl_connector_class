# -*- coding: utf-8 -*-
"""
Cisco Systems Inc.

Zeep Debug Plugin
This class enables a Zeep object to output logs containing the received and sent SOAP requests

This script is propierty of Cisco Systems. The license for usage is
valid only during the period stablished in the contract between Cisco Systems
and HCA. Removing the author and/or copyright information from the script
is a violation to the license agreement. Any derivative work from this script is
considered a violation to the license agreement.

@author: Alfonso Sandoval Rosas (alfsando@cisco.com)
"""

import logging
from zeep import Plugin
from lxml import etree

class ZeepDebugPlugin( Plugin ):
    def egress( self, envelope, http_headers, operation, binding_options ):
        """Output in console logs the sent SOAP request"""

        # Format the request body as pretty printed XML
        logging.basicConfig(level=logging.DEBUG)
        xml = etree.tostring( envelope, pretty_print = True, encoding = 'unicode')
        logging.debug( f'\nRequest\n-------\nHeaders:\n{http_headers}\n\nBody:\n{xml}' )

    def ingress( self, envelope, http_headers, operation ):
        """Output in console logs the received SOAP request"""

        # Format the response body as pretty printed XML
        logging.basicConfig(level=logging.DEBUG)
        xml = etree.tostring( envelope, pretty_print = True, encoding = 'unicode')
        logging.debug( f'\nResponse\n-------\nHeaders:\n{http_headers}\n\nBody:\n{xml}' )