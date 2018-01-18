# -*- coding: utf-8 -*-
import re
import logging

logger = logging.getLogger(__name__)


def validate_flight_number(flight_number):
    matching = re.match(r'([A-Z]{2}|[A-Z]\d|\d[A-Z])\s?\d{3,4}', flight_number)

    if matching:
        return re.match(r'([A-Z]{2}|[A-Z]\d|\d[A-Z])\s?\d{3,4}', flight_number).group() == flight_number
    else:
        return False
