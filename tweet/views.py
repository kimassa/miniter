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
        data = serializers.serialize('json', Tweet.objects.filter(pk=id))
        return HttpResponse(data, content_type='application/json')

    def post(self,request):
        tweet_input = json.loads(request.body)
        user_id = tweet_input['user_id']
        tweet_content = tweet_input['tweet']
        Tweet(tweet = tweet_content, user_id = User.objects.get(id=user_id)).save()
        return JsonResponse({ 'tweet_content': tweet_content })

    def put(self,request):
        front_input = json.loads(request.body)
        tweet_pk = front_input['pk']
        tweet_update = front_input['tweet_update']
        Tweet.objects.filter(pk = tweet_pk).update(tweet = tweet_update)
        # data = serializers.serialize('json', Tweet.objects.filter(pk=tweet_pk))
        # return HttpResponse(data, content_type='application/json')
        return JsonResponse({ 'tweet_update': tweet_update })


    def delete(self,request):
        front_input = json.loads(request.body)
        tweet_pk = front_input['pk']
        deleted_tweet = Tweet.objects.filter(pk = tweet_pk)
        Tweet.objects.filter(pk = tweet_pk).delete()
        return HttpResponse(status=200)



class TweetAllView(View):

    model = Tweet

    def get(self, request):
        data = serializers.serialize('json', Tweet.objects.all())
        return HttpResponse(data, content_type='application/json')

# class TweetSearchView(View):
#
#     model = Tweet
#
#     def post(self, request):
#         search_input = json.loads(request.body)
#         search_result = search_input['search_text']
#         data = serializers.serialize('json', Tweet.objects.filter(tweet = search_result))
#         return HttpResponse(data, content_type='application/json')
