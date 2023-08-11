from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .runbot import getsubtitle, qna
from django.views.decorators.csrf import csrf_exempt
import asyncio

class VideoSubtitleView(APIView):
    @csrf_exempt
    def post(self, request):
        video_url = request.data.get('video_url')
        subtitles = getsubtitle(video_url)
        return Response({'subtitles': subtitles}, status=status.HTTP_200_OK)

class QuestionAnswerView(APIView):
    @csrf_exempt
    def post(self, request):
        question = request.data.get('question')
        answer = qna(question)
        return Response({'answer': answer}, status=status.HTTP_200_OK)
