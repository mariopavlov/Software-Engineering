""" A module to hold all helper functions for Telephone number operations """
import re


def get_telephone_type(telephone):
    """ Gets telephone number as input, and returns type of the number """

    if telephone.startswith('140'):
        return 'telemarketers'
    elif telephone.startswith('(0'):
        return 'fixed'
    elif telephone.startswith(('7', '8', '9')):
        return 'mobile'
    else:
        return 'unknown'


def get_fixed_location(telephone):
    """ Returns location of fixed line"""

    if telephone.startswith('(080)'):
        return 'Bangalore'

    return 'Unknown'


def get_area_code(telephone):
    """ Returns area code from a telephone number
    :param telephone: single telephone number
    :return: Area code
    """

    code_type = get_telephone_type(telephone)

    if code_type == 'telemarketers':
        return '140'
    elif code_type == 'fixed':
        area_code = re.findall(r'\(.*?\)', telephone)
        return area_code[0]
    else:
        return telephone[:4]


def extract_duration(single_call, phone_calls):
    """ Receives single row from the raw data,
    and extracts duration for both receivers and callers """

    caller = single_call[0]
    receiver = single_call[1]
    duration = int(single_call[3])

    if caller in phone_calls:
        phone_calls[caller] += duration
    else:
        phone_calls[caller] = duration

    if receiver in phone_calls:
        phone_calls[receiver] += duration
    else:
        phone_calls[receiver] = duration

