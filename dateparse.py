import dateparser
import re

async def parse_date_time(message):
    # Remove extra words and keep date, time and timezone related words
    cleaned_msg = re.sub(r'(?i)\b(at|on|by|from|due|till)\b', '', message)
    
    date_time_obj = dateparser.parse(cleaned_msg, settings={'PREFER_DATES_FROM': 'future'})

    if date_time_obj:
        unix_timestamp = date_time_obj.timestamp()
        return unix_timestamp
    else:
        return "false"
