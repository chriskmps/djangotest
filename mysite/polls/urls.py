from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('votes/<int:choice_id>/', views.num_votes, name='num_votes'),
	path('dates_pub/<int:question_id>', views.dates_pub, name='dates_pub'),
]