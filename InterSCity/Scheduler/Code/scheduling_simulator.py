from datetime import datetime, date, timedelta
class SchedulingSimulator():
     
    def __init__(self):
        self.__msg = None

    def get_times(self):
        times = [{'i':datetime.strptime('2020-04-29 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-29 13:30:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, {'i':datetime.strptime('2020-04-29 10:30:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-29 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, {'i':datetime.strptime('2020-04-29 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-29 11:30:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, {'i':datetime.strptime('2020-04-29 11:30:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-29 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}]
        return times