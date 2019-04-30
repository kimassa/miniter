from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from user.models import User
from tweet.models import Tweet
from django.core import serializers
import json

class UserView(View):

    model = User

    def get(self, request, id):
        data = serializers.serialize('json', User.objects.all())
        return HttpResponse(data, content_type='application/json')

    def post(self,request):
        user_input = json.loads(request.body)
        user_id = user_input['user_id']
        tweet_content = user_input['tweet']
        User(user = User.objects.get(id=user_id)).save
        return HttpResponse(status = 200)
