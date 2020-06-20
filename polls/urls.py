from django.urls import path

from .views import index, detail, results, vote, create_question

app_name = 'Polls'


urlpatterns = [
        # ex: /polls/
        path('', index, name='index'),
        # ex: /polls/5/
        path('<int:question_id>/', detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:question_id>/results/', results, name='results'),
        # ex: /polls/5/vote/
        path('<int:question_id>/vote/', vote, name='vote'),
        path('create_question/', create_question, name='create_question'),
        ]
