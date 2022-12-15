from datetime import date

today = date.today().strftime("%y-%m-%d")
print(today)


date = '2022-12-01'

year = date.split('-')[0].split('0')[1]
month= date.split('-')[1]
day = date.split('-')[2]
date = year+'-'+month+'-'+day
print(date)

start =int("10:12".split(':')[0])
end = int("1:12".split(':')[0])
# 07:44 18:51
print(start,end)

if  7<= start<=18 and 7 <= end<=18:
    print('true')
else:
    print("false")

