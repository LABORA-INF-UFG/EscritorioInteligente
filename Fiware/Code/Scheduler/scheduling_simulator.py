from datetime import datetime, date, timedelta
class SchedulingSimulator():
     
    def __init__(self):
        self.__msg = None

    def get_times(self):
        times = [{'i':datetime.strptime('2020-04-09 13:45:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-09 14:50:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, {'i':datetime.strptime('2020-04-07 15:40:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-07 16:20:15.158216', '%Y-%m-%d %H:%M:%S.%f')}, {'i':datetime.strptime('2020-04-07 16:30:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-07 17:00:15.158216', '%Y-%m-%d %H:%M:%S.%f')}, {'i':datetime.strptime('2020-04-07 17:10:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-04-07 17:40:15.158216', '%Y-%m-%d %H:%M:%S.%f')}]
        return times