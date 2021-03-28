from django.urls import path
from . import views

app_name='Question_Bank'

urlpatterns = [
    path('Question/create',views.CreateQs.as_view()),
    path('Question/list',views.ListQs.as_view()),
    path('Question/detail/<int:id>',views.DetailQs.as_view()),
    path('Option/create',views.CreateOptions.as_view()),
    path('Option/list/<int:id>',views.DetailOptions.as_view())
]