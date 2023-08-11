from django.urls import path
from .views import VideoSubtitleView, QuestionAnswerView

urlpatterns = [
    path('subtilte/', VideoSubtitleView.as_view(), name='get_subtitles'),
    path('question/', QuestionAnswerView.as_view(), name='get_answer'),
]