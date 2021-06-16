# fileparse.py
#
# Exercise 3.3


import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        # Read the file headers
        if has_headers:
            headers = next(rows)
        else:
            headers = []
        # If a column selector was given, find indices of the specified columns
        # & make corresponding headers
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        records = []
        for row in rows:
            if not row:   # Skip rows with no data
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:   # if types are given, convert values to types
                row = [func(val) for func, val in zip(types, row)]
            if has_headers:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)
            records.append(record)

    return records