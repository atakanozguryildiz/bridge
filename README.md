<h2>Bridge</h2>
<p>Helper class to find naive dates between start and end date.</p>

```
import datetime as dt

from bridge import Bridge

>>> d1 = dt.date(2019, 2, 25)
>>> d2 = dt.date(2019, 2, 27)
>>> b = Bridge(d1, d2)
>>> b.days_between_dates()
[datetime.date(2019, 2, 25), datetime.date(2019, 2, 26), datetime.date(2019, 2, 27)]


>>> d1 = dt.date(2018, 11, 28)
>>> d2 = dt.date(2019, 2, 27)
>>> b = Bridge(d1, d2)
>>> b.months_between_dates()
[datetime.date(2018, 11, 1), datetime.date(2018, 12, 1), datetime.date(2019, 1, 1), datetime.date(2019, 2, 1)]

>>> d1 = dt.date(2018, 11, 28)
>>> d2 = dt.date(2019, 2, 27)
>>> b = Bridge(d1, d2)
>>> b.years_between_dates()
[datetime.date(2018, 1, 1), datetime.date(2019, 1, 1)]

>>> d1 = dt.date(2019, 2, 1)
>>> d2 = dt.date(2019, 2, 28)
>>> b = Bridge(d1, d2)
>>> b.weeks_between_dates()
[datetime.date(2019, 1, 28), datetime.date(2019, 2, 4), datetime.date(2019, 2, 11), datetime.date(2019, 2, 18), datetime.date(2019, 2, 25)]

```
