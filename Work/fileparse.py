# fileparse.py
#
# Exercise 3.3


import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires a file with column headers")
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
        for i, row in enumerate(rows):
            if not row:   # Skip rows with no data
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:   # if types are given, convert values to types
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if silence_errors:
                        continue
                    else:
                        print(f"Row {i+1}: couldn't parse {row}")
                        print("Reason:", e)
                        continue
            if has_headers:
                record = dict(zip(headers,row))
            else:
                record = tuple(row)
            records.append(record)

    return records