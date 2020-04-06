from datetime import datetime, date, timedelta
class SchedulingSimulator():
     
    def __init__(self):
        self.__msg = None

    def get_times(self):
        times = [{'i':datetime.strptime('2020-04-06 15:41:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-06 15:45:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, {'i':datetime.strptime('2020-04-06 15:46:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-06 15:50:00.158216', '%Y-%m-%d %H:%M:%S.%f')}]
        return times