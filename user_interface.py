import url_module
import indicator_module
import signal_module
from datetime import datetime



def _input_path() -> str:
    """
    Takes a path to the api key and return a string
    :return: a string
    """
    path_string = input('Path:').strip()
    return path_string

def _input_symbol() -> str:
    """
    Takes a symbol of a company a returns a string
    :return: a string
    """
    symbol = input('Symbol: ').strip().upper()
    if symbol == '':
        return ''
    else:
        return symbol

def input_indicator() -> list:
    """
    Takes an input and returns indicator
    :return: indicator
    """

    indicator_input = input('Please enter the indicator and its threshold: ').split()

    if indicator_input[0] == 'TR':
        return indicator_input
    else:
        print('Please enter the right indicator which is TR')


def _data_list(json: 'a json'):
    """
    Returns a list of data to pass into the stock namedtuple
    :param json: a json
    :return: return a list
    """
    data = json['Time Series (Daily)']
    return list(data.items())

def _input_date(stock_list: 'a namedtuple') -> list:
    """get stock_info based on given date"""

    stock_info = stock_list

    format_date = '%Y-%m-%d'
    start_date = datetime.strptime(input('Start Date: ').strip(), format_date)
    end_date = datetime.strptime(input('End Date: ').strip(), format_date)

    result_stock_list = []
    for stock in stock_info:
        date = datetime.strptime(stock.date, format_date)
        if start_date <= date <= end_date:
            result_stock_list.append(stock)
            result_stock_list.sort()
    return result_stock_list


def _print_report(stock_info: list, symbol: str, indicator_symbol: str) -> None:
    print('\n\tSYMBOL: ', symbol)

    if indicator_symbol == 'TrueRange':
        print('\tSTRATEGY: True range')
    else:
        print(indicator_symbol)

    print('\n\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}\t\t{}\t\t{}\t\t{}'.format(
        'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Indicator', 'Signal'))

    for i in stock_info:
        print('\t{:10}\t{:6s}\t{:6s}\t{:6s}\t{:6s}\t{:8}\t{:.4f}\t\t\t{}'.format(
            i.date, i.open, i.high, i.low, i.close, i.volume, i.indicator, i.signal))


def _main_program() -> None:
    path = _input_path()

    symbol = _input_symbol()

    url = url_module.build_url(path, symbol)

    result = url_module.get_result(url)

    print(result)

    stock_list = _data_list(result)
    
    stock_namedtuple = indicator_module.stock_namedtuple(stock_list)
    
    print(stock_namedtuple)
    
    date_range_stock_list = _input_date(stock_namedtuple)

    indicator_symbol = 'TrueRange'
    
    indicator_info = indicator_module.run_indicator(eval('indicator_module.'+indicator_symbol+'(date_range_stock_list)'))

    signal_info = signal_module.run_signal(eval('signal_module.'+indicator_symbol+'(indicator_info)'))

    _print_report(indicator_info, symbol, indicator_symbol)

if __name__ == '__main__':
    _main_program()