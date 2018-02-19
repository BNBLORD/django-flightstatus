# Flight status

Flight status allows you to make a simple API call to [FlightStats REST] to retrieve the status of a flight, based on a flight number.

## Quick start

 1. Add `flightstatus` to your `INSTALLED_APPS` setting like this:

```
INSTALLED_APPS = [
    ...
    'flightstatus',
]
```

 2. Add `FLIGHTSTATUS_APP_ID` and `FLIGHTSTATUS_APP_KEY` to your Django `settings.py`:

```
FLIGHTSTATUS_APP_ID = "your flighstatus app id"
FLIGHTSTATUS_APP_KEY = "your flighstatus app key"
```

<!-- Links -->
[FlightStats REST]: https://developer.flightstats.com/api-docs/
