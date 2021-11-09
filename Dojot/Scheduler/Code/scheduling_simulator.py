from datetime import datetime, date, timedelta
class SchedulingSimulator():
     
    def __init__(self):
        self.__msg = None

    def get_times(self):
        times = [{'i':datetime.strptime('2020-09-17 11:43:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-09-17 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'id': '203', 'solicitante': 'fran', 'nome': 'reuniao'}]
        return times
