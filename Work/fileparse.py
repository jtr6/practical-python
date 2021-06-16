# fileparse.py
#
# Exercise 3.18


import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV iterable into a list of dicts
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires an input with column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns
    # & make corresponding headers
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for i, row in enumerate(rows):
        if not row:   # Skip rows with no data
            continue
        
        if select:
            row = [row[index] for index in indices]
        if types:   # if types are given, convert values to types
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {i+1}: couldn't parse {row}")
                    print("Reason:", e)
                continue
        if has_headers:
            record = dict(zip(headers,row))
        else:
            record = tuple(row)
        records.append(record)

    return records