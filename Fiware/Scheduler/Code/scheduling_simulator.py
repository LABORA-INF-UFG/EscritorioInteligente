from datetime import datetime, date, timedelta
class SchedulingSimulator():
     
    def __init__(self):
        self.__msg = None

    def get_times(self):
            {'i':datetime.strptime('2020-07-24 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},           
            {'i':datetime.strptime('2020-07-24 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-24 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-24 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-24 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-25 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-25 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-25 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-25 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-25 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-26 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-26 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-26 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-26 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-27 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-27 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-27 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-27 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-28 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 13:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 14:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-28 15:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 16:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 17:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 18:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 19:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 20:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 21:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 22:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-28 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-28 23:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 00:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 01:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 02:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 03:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 04:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 05:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 06:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 07:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 08:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 09:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')},
            {'i':datetime.strptime('2020-07-29 10:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}, 
            {'i':datetime.strptime('2020-07-29 11:00:00.158216', '%Y-%m-%d %H:%M:%S.%f'), 'f': datetime.strptime('2020-07-29 12:00:00.158216', '%Y-%m-%d %H:%M:%S.%f')}]
        return times
