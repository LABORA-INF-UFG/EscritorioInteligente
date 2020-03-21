from datetime import datetime, date, timedelta
class SchedulingSimulator():
     
    def __init__(self):
        self.__msg = None

    def get_times(self):
        times = [{'i':datetime.strptime('2020-03-21 11:16:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-03-21 09:31:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, {'i':datetime.strptime('2020-03-20 16:16:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-03-20 16:16:00.158216', '%Y-%m-%d %H:%M:%S.%f')}]
        return times