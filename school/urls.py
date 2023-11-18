from django.urls import path

from school.apps import SchoolConfig
from rest_framework.routers import DefaultRouter

from school.views import KursViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionViewSet

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'kurs', KursViewSet, basename='kurs')
router.register(r'subscription', SubscriptionViewSet, basename='subscription')



urlpatterns =[
    path('lesson/create/',LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('pay/', PayListAPIView.as_view(), name='pay_list'),
             ] + router.urls