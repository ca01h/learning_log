from django.shortcuts import render
from.models import Topic
import logging
# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    # context变量中字典的key与html模板函数中的变量对应
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    for entry in entries:
        print(entry.date_added)
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
