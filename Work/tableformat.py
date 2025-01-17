# tableformat.py 

from typing import Text


class TableFormatter:
    def headings(self, headers):
        '''
        Function to emit table headings.
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter:
    '''
    Output portfolio data in CSV format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter:
    '''
    Output portfolio data in HTML format
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('<tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('<tr>')


class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')
    return formatter

def print_table(objects, attr, formatter):
    '''
    Print a fomratted table that takes arbitrary attributes from objects
    '''
    formatter.headings(attr)
    for obj in objects:
        rowdata = [str(getattr(obj, name)) for name in attr]
        formatter.row(rowdata)


