months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(),m) for m in months)

print month_abbvs

def valid_month(month):
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
    
def valid_day(day):
    
    if day and day.isdigit():
        d = int(day)
        if d > 0 and d < 32:
            return d
        
def valid_year(year):
    if year and year.isdigit():
        y = int(year)
        if y >=1900 and y <=2020:
            return y
"""
month_abbvs = {}
for m in months:
  month_abbvs(m[:3].lower()) = m
def valid_month(month):
    if month:
        cap_month = month.capitalize()
        if cap_month in months:
            return cap_month
"""
print valid_month("january")
print valid_month("January")
print valid_month("jan")
print valid_month("foo")
print valid_month("")
print
print valid_day('0')
print valid_day('1')
print valid_day('31')
print valid_day('500')
print valid_day('vivek')



