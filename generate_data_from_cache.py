#!/usr/bin/env python3

import collections
import csv
import json

CACHE_DATA = "cache/default_timezones.tsv"
OUTPUT = "data/default_timezone_by_country_code.json"

def standardize_utc_offset(utc_offset):
    """utc_offset format is either '(UTC)' or '(UTC+xx:xx)."""
    if utc_offset == "(UTC)":
        return "+00:00"
    else:
        return utc_offset[4:10]


def main():
    # Ensure that ordering stays the same across runs on the same cache data.
    default_timezone_by_country_code = collections.OrderedDict()

    with open(CACHE_DATA) as cache:
        cache_reader = csv.reader(cache, delimiter="\t")
        skipped_header = False
        for row in cache_reader:
            if not skipped_header:
                skipped_header = True
                continue
            country, iso3116, timezone, utc, timezone_description = row
            default_timezone_by_country_code[iso3116] = {
                "country_name": country,
                "timezone_name": timezone,
                "timezone_description": timezone_description,
                "utc_offset": standardize_utc_offset(utc),
            }
    with open(OUTPUT, "w") as output:
        json.dump(default_timezone_by_country_code, output, indent=4)


if __name__ == "__main__":
    main()
