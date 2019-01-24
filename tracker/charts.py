from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from tracker.models import *
from school.models import *


class TopicScoreHBarChart(Chart):
    chart_type = 'horizontalBar'


class CohortGraph(Chart):
    chart_type = 'horizontalBar'

    scales = {
        'xAxes': [Axes(stacked=True)],
        'yAxes': [Axes(stacked=True)],
    }

    def get_labels(self, **kwargs):
        labels = []
        for point in self.syllabus_areas:
            labels.append(str(point))

        return labels

    def get_datasets(self, **kwargs):
        """ For each point, generate a new point in the correct range. """

        total_students = self.students.count()

        points_0_to_1 = []

        for point in self.syllabus_areas:
            # Need to include -1 here to catch the 0s.
            count = point.cohort_rating_number(self.students, -1, 1)
            points_0_to_1.append(count/total_students)

        points_1_to_2 = []

        for point in self.syllabus_areas:
            count = point.cohort_rating_number(self.students, 1, 2)
            points_1_to_2.append(count/total_students)

        points_2_to_3 = []

        for point in self.syllabus_areas:
            count = point.cohort_rating_number(self.students, 2, 3)
            points_2_to_3.append(count/total_students)

        points_3_to_4 = []

        for point in self.syllabus_areas:
            count = point.cohort_rating_number(self.students, 3, 4)
            points_3_to_4.append(count/total_students)

        points_4_to_5 = []

        for point in self.syllabus_areas:
            count = point.cohort_rating_number(self.students, 4, 5)
            points_4_to_5.append(count/total_students)

        return_data = []

        return_data.append(DataSet(label='0-1',
                                   data=points_0_to_1,
                                   borderWidth=2,
                                   color=(171, 9, 0),
                                   ))
        return_data.append(DataSet(label='1-2',
                                   data=points_1_to_2,
                                   borderWidth=2,
                                   color=(166, 78, 46),
                                   ))
        return_data.append(DataSet(label='2-3',
                                   data=points_2_to_3,
                                   borderWidth=2,
                                   color=(255, 190, 67),
                                   ))
        return_data.append(DataSet(label='3-4',
                                   data=points_3_to_4,
                                   borderWidth=2,
                                   color=(163, 191, 63),
                                   ))
        return_data.append(DataSet(label='4-5',
                                   data=points_4_to_5,
                                   borderWidth=2,
                                   color=(122, 159, 191),
                                   ))
        return return_data


class CohortPointGraph(CohortGraph):
    # Let's start by including no data
    # this can be overriden when declaring the chart, but having none to start with
    # will let us quickly see if we've forgotten anything.

    # IMPORTANT: These are 'areas' so we can either use points, sub topics, or topics
   #  syllabus_areas = SyllabusPoint.objects.none()
    students = Student.objects.none()

    data = []


class CohortSubTopicChart(CohortGraph):

   # syllabus_areas = SyllabusSubTopic.objects.none()
    students = Student.objects.none()

    data = []


class StudentChart(Chart):
    chart_type = 'horizontalBar'
    height = 50

    scales = {
        'xAxes': [Axes(stacked=True, display=False)],
        'yAxes': [Axes(stacked=True)],
    }

    responsive = True
    options = {'maintainAspectRatio': False,
               'height': 50}


    def get_labels(self, **kwargs):
        labels = []
        for point in self.syllabus_areas:
            labels.append(str(point))

        return labels

    def get_datasets(self, **kwargs):
        """ For each point, generate a new point in the correct range. """

        points_0_to_1 = []

        for point in self.syllabus_areas:
            # Need to include -1 here to catch the 0s.
            total_points = point.syllabus_points().count()
            count = point.cohort_rating_number(self.students, -1, 1)
            points_0_to_1.append(round(count / total_points*100, 0))

        points_1_to_2 = []

        for point in self.syllabus_areas:
            total_points = point.syllabus_points().count()
            count = point.cohort_rating_number(self.students, 1, 2)
            points_1_to_2.append(round(count / total_points*100, 0))

        points_2_to_3 = []

        for point in self.syllabus_areas:
            total_points = point.syllabus_points().count()
            count = point.cohort_rating_number(self.students, 2, 3)
            points_2_to_3.append(round(count / total_points*100, 0))

        points_3_to_4 = []

        for point in self.syllabus_areas:
            total_points = point.syllabus_points().count()
            count = point.cohort_rating_number(self.students, 3, 4)
            points_3_to_4.append(round(count / total_points*100, 0))

        points_4_to_5 = []

        for point in self.syllabus_areas:
            total_points = point.syllabus_points().count()
            count = point.cohort_rating_number(self.students, 4, 5)
            points_4_to_5.append(round(count / total_points*100, 0))

        return_data = []

        return_data.append(DataSet(label='0-1',
                                   data=points_0_to_1,
                                   borderWidth=2,
                                   color=(171, 9, 0),
                                   fillOpacity=1
                                   ))
        return_data.append(DataSet(label='1-2',
                                   data=points_1_to_2,
                                   borderWidth=2,
                                   color=(166, 78, 46),
                                   ))
        return_data.append(DataSet(label='2-3',
                                   data=points_2_to_3,
                                   borderWidth=2,
                                   color=(255, 190, 67),
                                   ))
        return_data.append(DataSet(label='3-4',
                                   data=points_3_to_4,
                                   borderWidth=2,
                                   color=(122, 159, 191),
                                   ))
        return_data.append(DataSet(label='4-5',
                                   data=points_4_to_5,
                                   borderWidth=2,
                                   color=(163, 191, 63),
                                   ))
        return return_data


class StudentSubTopicGraph(StudentChart):
    legend = False
    fillOpacity = 1

    def get_labels(self, **kwargs):
        labels = []
        for point in self.syllabus_areas:
            labels.append("")

        return labels