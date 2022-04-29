# input for event
event=input('enter the envent name ')
year=int(input(' please enter the year '))
month=int(input('enter the month of event 1-12 '))
day=int(input('enter the day of event 1-31 '))

#import library
import datetime,time
t=datetime.datetime(year,month,day,0,0)
total_event_second=time.mktime(t.timetuple())
event_secont=total_event_second%(60)
event_min=total_event_second//60
event_hr=total_event_second//(60*60)




from datetime import date

total_current_second=time.time()

# difference
total_time_diff=total_event_second-total_current_second


year_diff=int(total_time_diff//(365*24*60*60))
remainder_second_year=int(total_time_diff%(365*24*60*60))
day_diff=int(remainder_second_year//(24*60*60))
remainder_second_day=int(remainder_second_year%(24*60*60))
hour_diff=int(remainder_second_day//(60*60))
remainder_second_hour=int(remainder_second_day%(60*60))
min_dif=int(remainder_second_hour//60)
remainder_second_min=int(remainder_second_hour%60)
second_diff=int(remainder_second_min-min_dif%60)

print('the event title {} after {} year {} days {} hours,{}mins, {}second'.format(event,year_diff,day_diff,hour_diff,min_dif,second_diff))


