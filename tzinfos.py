from dateutil.tz import gettz
from timezoneDict import timezones

tzinfos = {abbr: gettz(tz) for abbr, tz in timezones.items()}