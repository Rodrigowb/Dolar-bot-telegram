# Create a group with the bot
# https://api.telegram.org/bot1974352465:AAEDfX7hlppFDknepdwu4-dL1U4O787HV7M/getUpdates
# Chat ID: -551925848
# Create a bot @BotFather
# Send_info_message
# https://api.telegram.org/bot1974352465:AAEDfX7hlppFDknepdwu4-dL1U4O787HV7M/sendMEssage?chat_id=-551925848&text='Hi, I am Mandalorian and this is the way!
# requests.get(base_url)
# Send_error_message
# https://api.telegram.org/bot1968918950:AAFnE98tE42nSaloofevSn6oFLlkWEPoKAs/sendMEssage?chat_id=-533397331&text=''

import requests
from pandas_datareader import data as pdr
from datetime import datetime, date
import holidays


class DolarUpdates:

    def __init__(self):

        self.sp_holidays = holidays.BR(state='SP')
        self.today_day = date.today()
        self.week_day = datetime.today().weekday()
        self.ticker = 'USDBRL=X'

    @staticmethod
    def send_error_message(text):
        """

        :param text: texto para ser enviado ao grupo de errors telegram
        :return: mensagem de erro no grupo de erro telegram
        """
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        requests.get(
            f'https://api.telegram.org/bot1968918950:AAFnE98tE42nSaloofevSn6oFLlkWEPoKAs'
            f'/sendMEssage?chat_id=-533397331&text={dt_string}\n{text}')
        return

    @staticmethod
    def send_info_message(text):
        """

        :param text: texto para ser enviado ao grupo de infos do telegram
        :return: mensagem de info no grupo de info do telegram
        """
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        requests.get(
            f'https://api.telegram.org/bot1974352465:AAEDfX7hlppFDknepdwu4-'
            f'dL1U4O787HV7M/sendMEssage?chat_id=-551925848&text={dt_string}\n\n{text}')
        return

    def get_df(self):
        """

        :return: retorna dolar dataframe
        """
        try:
            dolar_df = pdr.get_data_yahoo(self.ticker)
            return dolar_df
        except ConnectionError:
            DolarUpdates.send_error_message('!!!ERRO DE CONEXÃO!!!\n'
                                            'get_df')
            return
        except:
            DolarUpdates.send_error_message('!!!ERRO GERAL!!!\n'
                                            'get_df')
            return

    def execute(self, event=None, context=None):
        """

        :return: envia mensagem no telegram com o preço atual, abertura
        e variacao %
        """
        dolar_df = DolarUpdates.get_df(self)
        if (self.today_day not in self.sp_holidays) and (self.today_day.weekday() < 5):
            try:
                current_price = round(dolar_df.iloc[-1][-1], 3)
                open_price = round(dolar_df.iloc[-1][-4], 3)
                dif_price = round(((current_price/open_price)-1)*100, 3)
                DolarUpdates.send_info_message(f'NOW USD/BRL: R${current_price}\n\n'
                                               f'OPEN USD/BRL: R${open_price}\n\n'
                                               f'VARIAÇÃO %: {dif_price}%')
            except:
                DolarUpdates.send_error_message('!!!ERRO GERAL!!!\n'
                                                'execute')
        else:
            DolarUpdates.send_info_message('Hoje é feriado em SP!\n'
                                           'Mando te deseja um ótimo feriado\n'
                                           'This is the way!')
        return event, context


if __name__ == '__main__':
    DolarUpdates().execute()