from jchart import Chart
from jchart.config import Axes, DataSet, rgba
from tracker.models import *
from school.models import *

class TopicScoreHBarChart(Chart):
    chart_type = 'horizontalBar'


class BarChart(Chart):
    # Let's start by including all data
    # this can be overriden when declaring the chart
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    exams = Exam.objects.all()
    sitting = Sitting.objects.all()
    topics = SyllabusTopic.objects.all()
    chart_type = 'horizontalBar'

    scales = {
        'xAxes': [Axes(stacked=True)],
        'yAxes': [Axes(stacked=True)],
    }

    def get_labels(self, **kwargs):
        labels = []
        for topic in self.topics:
            labels.append(str(topic))

        return labels

    def get_datasets(self, **kwargs):
        data = []

        for topic in self.topics:
            data.append(topic.groupAverageRating(students=self.students))


        return [DataSet(label='Bar Chart',
                        data=data,
                        borderWidth=1,
                        ),
                DataSet(label='Bar Chart',
                        data=data,
                        borderWidth=1,
                        )
                        ]
