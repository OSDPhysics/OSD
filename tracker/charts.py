from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from tracker.models import *
from school.models import *


class TopicScoreHBarChart(Chart):
    chart_type = 'horizontalBar'


class BarChart(Chart):
    # Let's start by including no data
    # this can be overriden when declaring the chart, but having none to start with
    # will let us quickly see if we've forgotten anything.

    syllabus_points = SyllabusPoint.objects.none()
    students = Student.objects.none()

    data = []


    chart_type = 'horizontalBar'

    scales = {
        'xAxes': [Axes(stacked=True)],
        'yAxes': [Axes(stacked=True)],
    }

    def get_labels(self, **kwargs):
        labels = []
        for point in self.syllabus_points:
            labels.append(str(point))

        return labels

    def get_datasets(self, **kwargs):
        """ For each point, generate a new point in the correct range. """

        total_points = self.syllabus_points.count()

        points_0_to_1 = []

        for point in self.syllabus_points:
            count = point.cohort_rating_number(self.students, 0, 1)
            points_0_to_1.append(count/total_points * 100)

        points_1_to_2 = []

        for point in self.syllabus_points:
            count = point.cohort_rating_number(self.students, 1, 2)
            points_1_to_2.append(count / total_points * 100)

        points_2_to_3 = []

        for point in self.syllabus_points:
            count = point.cohort_rating_number(self.students, 2, 3)
            points_2_to_3.append(count / total_points * 100)

        points_3_to_4 = []

        for point in self.syllabus_points:
            count = point.cohort_rating_number(self.students, 3, 4)
            points_3_to_4.append(count / total_points * 100)

        points_4_to_5 = []

        for point in self.syllabus_points:
            count = point.cohort_rating_number(self.students, 0, 1)
            points_4_to_5.append(count / total_points * 100)

        return_data = []

        return_data.append(DataSet(label='0-1',
                                   data=points_0_to_1,
                                   borderWidth=1,
                                   ))
        return_data.append(DataSet(label='1-2',
                                   data=points_1_to_2,
                                   borderWidth=1,
                                   ))
        return_data.append(DataSet(label='2-3',
                                   data=points_2_to_3,
                                   borderWidth=1,
                                   ))
        return_data.append(DataSet(label='3-4',
                                   data=points_3_to_4,
                                   borderWidth=1,
                                   ))
        return_data.append(DataSet(label='4-5',
                                   data=points_4_to_5,
                                   borderWidth=1,
                                   ))
        return return_data
