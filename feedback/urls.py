from django.urls import include, re_path, path
from .views import update_feedback, FeedbackView


urlpatterns = [
    path('', FeedbackView.as_view),
    path('<int:id_feedback>', update_feedback),

]