""" A module to hold all helper functions for Telephone number operations """
import re


def get_telephone_type(telephone):
    """ Gets telephone number as input, and returns type of the number """

    if telephone.startswith('140'):
        return 'telemarketers'
    elif telephone.startswith('('):
        return 'fixed'
    else:
        return 'mobile'


def get_fixed_location(telephone):
    """ Returns location of fixed line"""

    if telephone.startswith('(080)'):
        return 'Bangalore'

    return 'Unknown'


def get_area_code(telephone):

    code_type = get_telephone_type(telephone)

    if code_type == 'telemarketers':
        return '140'
    elif code_type == 'fixed':
        area_code = re.findall(r'\(.*?\)', telephone)
        return area_code[0]
    else:
        return telephone[:4]
