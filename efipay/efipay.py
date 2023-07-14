# encoding: utf-8
from .endpoints import Endpoints

class EfiPay(Endpoints):
    def __init__(self, options):
        super(EfiPay, self).__init__(options)
