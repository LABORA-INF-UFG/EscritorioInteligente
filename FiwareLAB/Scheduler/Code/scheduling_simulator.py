from datetime import datetime, date, timedelta
class SchedulingSimulator():
     
    def __init__(self):
        self.__msg = None

    def get_times(self):
        times = [{'i':datetime.strptime('2020-12-29 11:40:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 12:10:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 12:30:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 12:30:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},           
            {'i':datetime.strptime('2020-12-29 13:15:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-29 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-29 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-25 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-25 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-25 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-25 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-25 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-26 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-26 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-26 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-26 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-27 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-27 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-27 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-27 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-28 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-12-28 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-12-28 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-12-28 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}]
        return times
