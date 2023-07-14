# encoding: utf-8

class EfiPayError(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

class MissingParametersError(EfiPayError):

    def __init__(self, parameter):
        self.parameter = parameter
        message = 'Missing required parameter {parameter}'.format(parameter= self.parameter)
        super(MissingParametersError, self).__init__(message)


class UnauthorizedError(EfiPayError):

    def __init__(self, status):
        message = "{ 'Status': " + str(status) + ", 'Message': 'Could not authenticate. Please make sure you are using correct credentials and if you are using then in the correct environment.' } "
        super(UnauthorizedError, self).__init__(message)


class EndpointError(EfiPayError):

    def __init__(self, status):
        message = "{ 'Status': " + str(status) + ", 'Message': 'This method isn't available in sandbox.' } "
        super(EndpointError, self).__init__(message)

class CertificateError(EfiPayError):

    def __init__(self, status):
        message = "{ 'Status': " + str(status) + ", 'Message': 'Certificate not found.' }"
        super(CertificateError, self).__init__(message)