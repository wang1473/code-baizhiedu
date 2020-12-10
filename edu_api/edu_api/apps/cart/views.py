from django.shortcuts import render

# Create your views here.
import logging

from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from course.models import Course

log = logging.getLogger('django')


class CartViewSet(ViewSet):
    # 身份认证
    permission_classes = [IsAuthenticated]

    def add_cart(self, request):
        course_id = request.data.get('course_id')
        user_id = request.user.id
        # 勾选状态
        select = True
        # 有效期
        expice = 0
        # 前端参数校验
        try:
            Course.objects.get(is_show=True, is_delete=False, id=course_id)
        except Course.DoesNotExist:
            return Response({
                'message': '您添加的课程不存在'
            }, status=status.HTTP_400_BAD_REQUEST)
        try:
            redis_connection = get_redis_connection('cart')
            pipeline = redis_connection.pipeline()
            pipeline.multi()
            pipeline.hset('cart_%s' % user_id, course_id, expice)
            pipeline.sadd('selected_%s' % user_id, course_id)
            pipeline.excute()
            course_len = redis_connection.hlen('cart_%s' % user_id)
        except:
            log.error('购物存储数据失败')
            return Response({
                'message': '参数有误，添加购物车失败！'
            }, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        return Response({
            'message': '添加课程成功',
            'CART_LENGTH': course_len
        }, status=status.HTTP_200_OK)
