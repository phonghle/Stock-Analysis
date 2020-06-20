import indicator_module
import user_interface

def run_signal(indicator_method: 'an indicator'):
    return indicator_method.signal()

class TrueRange(indicator_module.TrueRange):

    def signal(self):
        threshold = user_interface.input_indicator()


        # threshold = [TR, >2, <0.1]
                    # [buy, sell]

        check_value = ''

        for day in range(len(self.stock_info) + 1):
            if threshold[1][0] == '>' and (self.stock_info[day-1].indicator > float(threshold[1][1:])) and (check_value != 'BUY'):
                    self.stock_info[day-1] = self.stock_info[day-1]._replace(signal='BUY')
                    check_value = 'BUY'

            elif threshold[1][0] == '<' and (self.stock_info[day-1].indicator < float(threshold[1][1:])) and (check_value != 'BUY'):
                    self.stock_info[day - 1] = self.stock_info[day  - 1]._replace(signal='BUY')
                    check_value = 'BUY'

            elif threshold[2][0] == '<' and (self.stock_info[day-1].indicator < float(threshold[2][1:])) and (check_value != 'SELL'):
                    self.stock_info[day-1] = self.stock_info[day-1]._replace(signal='SELL')
                    check_value = 'SELL'

            elif threshold[2][0] == '>' and (self.stock_info[day - 1].indicator > float(threshold[2][1:])) and (check_value != 'SELL'):
                    self.stock_info[day- 1] = self.stock_info[day  - 1]._replace(signal='SELL')
                    check_value = 'SELL'
            else:
                pass

        return self.stock_info
