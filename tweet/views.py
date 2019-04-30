from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from user.models import User
from tweet.models import Tweet
from django.core import serializers
import json

class TweetView(View):

    model = Tweet

    def get(self, request, id):
        data = serializers.serialize('json', Tweet.objects.filter(user_name=id))
        return HttpResponse(data, content_type='application/json')

    def post(self,request):
        tweet_input = json.loads(request.body)
        user_id = tweet_input['user_name']
        tweet_content = tweet_input['tweet']
        Tweet(tweet = tweet_content, user_name = User.objects.get(id=user_id)).save()
        return JsonResponse({ 'tweet_content': tweet_content })

class TweetAllView(View):

    model = Tweet

    def get(self, request):
        data = serializers.serialize('json', Tweet.objects.all())
        return HttpResponse(data, content_type='application/json')
