from collections import namedtuple

Stock = namedtuple('Stock', 'date open high low close volume indicator signal change')


# data = result['Time Series (Daily)']
# data = list(data.items())


def stock_namedtuple(data: list) -> [Stock]:
    """
    Returns a list of namedtuple
    :param data:
    :return:
    """

    stock_list = []
    for day in range(len(data) - 1):
        data_date = data[day][0]
        data_dict = data[day][1]
        stock_list.append(Stock(date=data_date,
                                open=data_dict['1. open'],
                                high=data_dict['2. high'],
                                low=data_dict['3. low'],
                                close=data_dict['4. close'],
                                volume=data_dict['5. volume'],
                                indicator=0.0,
                                signal='',
                                change=0))
    return stock_list


def run_indicator(indicator_method: 'an indicator') -> list:
    return indicator_method.calculate()


class TrueRange:

    def __init__(self, stock_info: [Stock]):

        self.stock_info = stock_info  # self.stock_info is a list that we want to return

    def calculate(self) -> list:

        for day in range(len(self.stock_info)):  # n day
            if day != 0:

                if self.stock_info[day].high > self.stock_info[day - 1].close > self.stock_info[day].low:
                    self.stock_info[day] = self.stock_info[day]._replace(
                        indicator=((float(self.stock_info[day].high) - float(self.stock_info[day].low))
                                   / float(self.stock_info[day - 1].close) * 100))

                elif self.stock_info[day].high < self.stock_info[day - 1].close:
                    self.stock_info[day] = self.stock_info[day]._replace(
                        indicator=((float(self.stock_info[day - 1].close) - float(self.stock_info[day].low))
                                   / float(self.stock_info[day - 1].close) * 100))

                else:
                    self.stock_info[day] = self.stock_info[day]._replace(
                        indicator=((float(self.stock_info[day].high) - float(self.stock_info[day - 1].close))
                                   / float(self.stock_info[day - 1].close) * 100))
            else:
                self.stock_info[day] = self.stock_info[day]._replace(indicator=0)

        return self.stock_info


