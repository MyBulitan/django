import re
from django import forms
from registration.forms import RegistrationForm


class RegistrationFormUtfUsername(RegistrationForm):
    '''
    Allowed UTF8 logins with space
    '''
    def __init__(self, *args, **kwargs):
        super(RegistrationFormUtfUsername, self).__init__(*args, **kwargs)
        self.fields['username'].regex = re.compile(r"^[\w ]+$", re.UNICODE)

