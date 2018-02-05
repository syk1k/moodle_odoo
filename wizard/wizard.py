# This module define the wizard that makes the the connection to moodle possible

from odoo import models, fields, api
import requests

class moodle_wizard(models.TransientModel):
    """This class is the one for configuring the moodle connection"""
    _name = 'moodle.wizard'

    moodle_token = fields.Char(string="Moodle Token", require=True)

    def make_connection(self):
        '''The method makes a test to get the site info'''
        #self.moodle_token = self.moodle_token
        domain = 'http://localhost:8888'
        webservice_url = '/webservice/rest/server.php?'
        parameters = {
            'wstoken':self.moodle_token,
            'wsfunction':'core_webservice_get_site_info',
            'moodlewsrestformat':'json'
        }
        request = requests.get(url=domain+webservice_url, params=parameters)
        request = request.json()

        if 'siteurl' in request:
            if request['siteurl']==domain:
                print('Hello')
        elif 'exception' in request:
            if request['exception']=="moodle_exception":
                if request['errorcode']=='invalidtoken':
                    print(request['message'])
            elif request['exception']=="webservice_access_exception":
                if request['errorcode']=='accessexception':
                    print(request['message'])
