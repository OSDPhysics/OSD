from django.test import TestCase
import datetime
from .functions import get_next_tt_week_year, get_monday_date_from_weekno
from osd.settings.base import CALENDAR_START_DATE, CALENDAR_END_DATE
# Create your tests here.

# Note: These require that the CALENDAR_XXX_DATES are the same


class GetMondayDateFromWeekNoTestCase(TestCase):
    def setUp(self):
        pass

    def test_first_week(self):
        expected_date = datetime.date(2018, 8, 20)
        week = 0
        year = 0
        monday_date = get_monday_date_from_weekno(week, year)
        self.assertEqual(expected_date, monday_date)

    def test_second_week(self):
        expected_date = datetime.date(2018, 8, 27)
        week = 1
        year = 0
        monday_date = get_monday_date_from_weekno(week, year)
        self.assertEqual(expected_date, monday_date)

    def test_second_year_first_week(self):
        expected_date = datetime.date(2019, 8, 19)
        week = 0
        year = 1
        monday_date = get_monday_date_from_weekno(week, year)
        self.assertEqual(expected_date, monday_date)

    def test_second_year_second_week(self):
        expected_date = datetime.date(2019, 8, 26)
        week = 1
        year = 1
        monday_date = get_monday_date_from_weekno(week, year)
        self.assertEqual(expected_date, monday_date)

class Get_next_TT_WW_TestCase(TestCase):
    def setUp(self):
        pass

    def test_no_year_change(self):
        start_week = 0
        start_year = 0
        next_week = get_next_tt_week_year(start_week, start_year)

        self.assertEqual(next_week, (1, 0))

    def test_end_of_year_change(self):
        start_week = 45 # There are 44 weeks in our school year
        start_year = 0

        next_week = get_next_tt_week_year(start_week, start_year)

        self.assertEqual(next_week, (0, 1))
