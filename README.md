# Default Timezone for Country

**Version 0.1.0**

**Author: Rahul Gupta-Iwasaki**

## Summary

_Provides a reasonable default timezone for every country._

- For when you need to know approximately what time it probably is, but it
  doesn't need to be perfect.
- Uses the same timezones that
  [Microsoft](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones)
  does in Windows 10 when a user first logs in.
- Exposes UTC offset info ("+XX:YY") indexed by
  [ISO-3166](https://en.wikipedia.org/wiki/ISO_3166-2) country code.

Right now, the easiest way to use it is probably just to copy the json file at `//data/default_timezone_by_country_code.json`.

If using npm, you can also:

1.  `npm install https://github.com/rahulgi/default-timezones`
1.  and then in your Javascript code:

        // require the json object
        const defaultTimezoneByCountryCode = require("default-timezone-for-country/data/default_timezone_by_country_code.json")
        // get the default timezone info for the United States
        console.log(defaultTimezoneByCountryCode["US"])
        // {
        //   country_name: 'United States',
        //   timezone_name: 'Pacific Standard Time',
        //   timezone_description: 'Pacific Time (US & Canada)',
        //   utc_offset: '-08:00'
        // }
