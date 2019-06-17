"""定义learnging_logs的URL模式"""

from django.conf.urls import url
from .views import index

urlpatterns = [
    # 主页
    url(r'^$', index, name='index'),
]