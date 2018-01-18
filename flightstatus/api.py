import requests
from datetime import date
from mysite.settings import FLIGHTSTATUS_APP_ID, FLIGHTSTATUS_APP_KEY


class RaiseForStatus(object):
    """
    Wrapper around request - built so each requests:
    - Automatically raise the exception if it fails
    - Return a json result
    """

    def __init__(self, f):
        self.request = f

    def __call__(self, *args, **kwargs):
        r = self.request(*args, **kwargs)
        try:
            r.raise_for_status()
        except Exception as e:
            raise e
        return r.json()


class DontRaiseForStatus(object):
    """
    Wrapper around request - built so each requests :
    - Automatically raise the exception if it fails
    - Return a json result
    """

    def __init__(self, f):
        self.request = f

    def __call__(self, *args, **kwargs):
        r = self.request(*args, **kwargs)
        return r.json()


@RaiseForStatus
def flight_status(flight_number, flight_date=date.today()):
    airline_id = flight_number[:2]
    flight_number = flight_number[2:]

    params = {
        "appId": FLIGHTSTATUS_APP_ID,
        "appKey": FLIGHTSTATUS_APP_KEY,
        "flightId": flight_number,
        "utc": False
    }

    return requests.get(
        "https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/{}/{}/arr/{}/{}/{}".format(
            airline_id, flight_number, str(flight_date.year), str(flight_date.month), str(flight_date.day)),
        params=params
    )
