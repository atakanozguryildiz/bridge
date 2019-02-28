<h2>Bridge</h2>
Helper class to find naive dates between start and end date.

```
import datetime as dt

import bridge


d1 = dt.date(2019, 2, 25)
d2 = dt.date(2019, 2, 27)

b = Bridge(d1, d2)
b.days_between_dates()

[datetime.date(2019, 2, 25),
 datetime.date(2019, 2, 26),
 datetime.date(2019, 2, 27)]


d1 = dt.date(2018, 11, 28)
d2 = dt.date(2019, 2, 27)

b = Bridge(d1, d2)
b.months_between_dates()

[datetime.date(2018, 11, 1),
 datetime.date(2018, 12, 1),
 datetime.date(2019, 1, 1),
 datetime.date(2019, 2, 1)]

b.years_between_dates()
[datetime.date(2018, 1, 1), datetime.date(2019, 1, 1)]

```
