from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: .polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: .polls/5/result/
    path('<int:question_id>/result/', views.result, name='result'),
    # ex: .polls/5/result/vote/
    path('<int:question_id>/result/vote/', views.vote, name='vote'),
]

