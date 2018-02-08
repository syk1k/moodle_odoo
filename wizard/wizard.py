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
                return "Ok"
        elif 'exception' in request:
            if request['exception']=="moodle_exception":
                if request['errorcode']=='invalidtoken':
                    print(request['message'])
            elif request['exception']=="webservice_access_exception":
                if request['errorcode']=='accessexception':
                    print(request['message'])


class moodle_category(models.TransientModel):
    """This module will be used to manage courses"""
    _name = 'moodle.category'

    categories = []

    parent_category = fields.Selection(selection=categories, string="Parent Category")
    category_name = fields.Char("Category name", required=True)
    category_id_number = fields.Integer("Category ID number")
    category_description = fields.Text("Description")

class moodle_courses(models.TransientModel):
    _name = 'moodle.courses'

    #General settings
    categories = [

    ]
    course_full_name = fields.Char("Full name", required=True)
    course_short_name = fields.Char("Short name", required=True)
    course_category = fields.Selection(selection=categories, string="Category", required=True)
    course_start_date = fields.Date("Start date")
    course_end_date = fields.Date("End date")

    #Description settings
    course_summary = fields.Text("Summary")

    # #Appearance settings
    # course_force_language = fields.Selection("Force language")
    # course_number_announcement = fields.Selection("Number of announcement")
    # course_show_activity_report = fields.Selection()
    #
    #
    # #Groups settings
    # course_group_mode = fields.Selection()
    # course_force_group_mode = fields.Selection()
    # course_default_grouping = fields.Selection()



    def get_courses_categories(self):
        """This methods return all categories available for courses"""
        domain = "http://localhost:8888"
        webservice_url = "/webservice/rest/server.php?"
        parameters = {
            "wstoken": self.token,
            'wsfunction': 'core_course_get_categories',
            'moodlewsrestformat': 'json'
        }
        request = requests.get(url=domain + webservice_url, params=parameters)
        request = request.json()

        self.categories = []

        if type(request) == list:
            for req in request:
                category = req["id"], req["name"]
                self.categories.append(category)

        elif type(request) == dict:
            if 'exception' in request:
                if request['exception'] == "moodle_exception":
                    if request['errorcode'] == 'invalidtoken':
                        print(request['message'])
                        print('Make sure you enter the correct token')
                        print("If you don't have any token yet refer to moodle"
                              + "administrator to find out how to get one ")
                elif request['exception'] == "webservice_access_exception":
                    if request['errorcode'] == "accessexception":
                        print(request['message'])
                        print("Check wether your token has the access to view the site info")
                        print("For more information about token accesses refer to your moodle "
                              + "administrator")



    def get_courses(self):
        """The method return a list of courses only if the user's token has the access to view courses"""
        domain = 'http://localhost:8888'
        webservice_url = '/webservice/rest/server.php?'
        parameters = {
            'wstoken': self.moodle_token,
            'wsfunction': 'core_course_get_courses',
            'moodlewsrestformat': 'json'
        }

        request = requests.get(url=domain + webservice_url, params=parameters)
        request = request.json()

        if type(request) == list:
            result = request
            return result
        elif type(request) == dict:
            if 'exception' in request:
                if request['exception'] == "moodle_exception":
                    if request['errorcode'] == 'invalidtoken':
                        print(request['message'])
                        print('Make sure you enter the correct token')
                        print("If you don't have any token yet refer to moodle"
                              + "administrator to find out how to get one ")
                elif request['exception'] == "webservice_access_exception":
                    if request['errorcode'] == "accessexception":
                        print(request['message'])
                        print("Check wether your token has the access to view the site info")
                        print("For more information about token accesses refer to your moodle "
                              + "administrator")

