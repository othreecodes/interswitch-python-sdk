class Sender(object):
    def __init__(self, lastname, othernames, email=None, phone=None):
        self.last_name = lastname
        self.other_names = othernames
        self.email = email
        self.phone = phone


class Beneficiary(object):
    def __init__(self, lastname, othernames, email=None, phone=None):
        self.last_name = lastname
        self.other_names = othernames
        self.email = email
        self.phone = phone
