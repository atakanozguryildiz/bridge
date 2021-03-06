import datetime as dt


class Bridge:
    """Helper class to find naive dates between start and end date.

    Methods:

    days_between_dates()
    month_between_dates()
    year_between_dates()

    Properties:

    start_date
    end_date
    """

    def __init__(self, start_date, end_date):
        self._check(start_date, end_date)
        self.start_date = start_date
        self.end_date = end_date
        self._convert_types()

    def days_between_dates(self):
        """Find a day date objects between dates.

        Return date object list
        """
        days = [self._start_date]
        delta = dt.timedelta(days=1)
        next_day = self._start_date + delta
        while next_day <= self._end_date:
            days.append(next_day)
            next_day += delta
        return days

    def months_between_dates(self):
        """Find a month date objects between dates.

        It set 1 for day property.

        Return date object list
        """
        start_date = self._start_date.replace(day=1)
        end_date = self._end_date.replace(day=1)
        temp_date = start_date
        months = [temp_date]
        while temp_date < end_date:
            temp_month = temp_date.month
            temp_year = temp_date.year
            if temp_month == 12:
                temp_month = 1
                temp_year += 1
            else:
                temp_month += 1
            temp_date = temp_date.replace(year=temp_year, month=temp_month)
            months.append(temp_date)
        return months

    def years_between_dates(self):
        """Find a year date objects between dates

        It set 1 for day and month properties

        Return date object list
        """
        start_date = self._start_date.replace(month=1, day=1)
        end_date = self._end_date.replace(month=1, day=1)
        temp_date = start_date
        years = [temp_date]
        while temp_date < end_date:
            next_year = temp_date.year + 1
            temp_date = temp_date.replace(year=next_year)
            years.append(temp_date)
        return years

    def weeks_between_dates(self):
        """Find week start date objects between dates

        It uses ISO 8601 format.
        It includes start of week. For example;

        Start date set 28.02.2019. This day is thursday, start of this
        week is 25.02.2019 so returning week list start from 25.02.2019.

        Return date object list

        """
        iso_first_day = 1
        start_date = self._start_date
        weekday = start_date.isoweekday()
        difference = weekday - iso_first_day
        difference_delta = dt.timedelta(days=difference)
        start_week = start_date - difference_delta

        weeks = [start_week]
        one_week_delta = dt.timedelta(days=7)
        end_date_week_number = self._end_date.isocalendar()[1]

        next_week = start_week + one_week_delta
        next_week_number = next_week.isocalendar()[1]
        while next_week_number <= end_date_week_number:
            weeks.append(next_week)
            next_week += one_week_delta
            next_week_number = next_week.isocalendar()[1]
        return weeks

    def _convert_types(self):
        if isinstance(self.start_date, dt.datetime):
            self._start_date = self.start_date.date()
        elif isinstance(self.start_date, dt.date):
            self._start_date = self.start_date
        if isinstance(self.end_date, dt.datetime):
            self._end_date = self.end_date.date()
        elif isinstance(self.end_date, dt.date):
            self._end_date = self.end_date

    def _check(self, start_date, end_date):
        if not (isinstance(start_date, dt.date) or
                isinstance(start_date, dt.datetime)):
            raise TypeError("`start_date` type must be `datetime` or `date`")
        if not (isinstance(end_date, dt.date) or
                isinstance(end_date, dt.datetime)):
            raise TypeError("`end_date` type must be `datetime` or `date`")
        if start_date > end_date:
            raise ValueError("`end_date` must be bigger than `start_date`")
