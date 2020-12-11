from django.shortcuts import render

# Create your views here.
import logging

from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from course.models import Course
from edu_api.settings.constants import IMG_SRC

log = logging.getLogger('django')


class CartViewSet(ViewSet):
    """购物车相关"""
    # 身份认证
    permission_classes = [IsAuthenticated]

    def add_cart(self, request):
        """
        将用户提交的课程信息保存至购物车
        :param request: 课程id 课程有效期 勾选状态  用户id
        :return:
        """
        course_id = request.data.get('course_id')
        user_id = request.user.id
        # 勾选状态
        select = True
        # 有效期
        expire = 0
        # 前端参数校验
        try:
            Course.objects.get(is_show=True, is_delete=False, id=course_id)
        except Course.DoesNotExist:
            return Response({'message': '您添加的课程不存在'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # 获取redis链接
            redis_connection = get_redis_connection('cart')
            # 使用管道操作redis
            pipeline = redis_connection.pipeline()
            # 开启管道
            pipeline.multi()
            # 将数据保存到redis 购物车商品的信息 以及 该商品对应的有效期
            pipeline.hset('cart_%s' % user_id, course_id, expire)
            # 被勾选的商品
            pipeline.sadd('selected_%s' % user_id, course_id)
            # 执行操作
            pipeline.execute()
            # 获取购物车商品总数量
            course_len = redis_connection.hlen('cart_%s' % user_id)
        except:
            log.error('购物存储数据失败')
            return Response({'message': '参数有误，添加购物车失败！'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        return Response({
            'message': '添加课程成功',
            'cart_length': course_len
        }, status=status.HTTP_200_OK)

    def list_cart(self, request):
        """展示购物车"""
        user_id = request.user.id
        redis_connection = get_redis_connection('cart')
        cart_list_bytes = redis_connection.hgetall('cart_%s' % user_id)
        select_list_bytes = redis_connection.smembers('selected_%s' % user_id)
        # 循环从mysql中查询商品信息
        data = []
        for course_id_byte, expire_id_byte in cart_list_bytes.items():
            course_id = int(course_id_byte)
            expire_id = int(expire_id_byte)
            try:
                course = Course.objects.get(is_show=True, is_delete=False, pk=course_id)
            except Course.DoesNotExist:
                continue
                # 将购物车所需的信息返回
            data.append({
                'selected': True if course_id_byte in select_list_bytes else False,
                'course_img': IMG_SRC + course.course_img.url,
                'name': course.name,
                'id': course.id,
                'price': course.price,
                'exprie_id': expire_id
            })
        return Response(data)

    def select_change(self, request):
        """切换购物车商品的状态"""
        course_id = request.data.get('course_id')
        select = request.data.get('selected')
        print(select)
        user_id = request.user.id
        redis_connection = get_redis_connection("cart")
        if select:
            try:
                redis_connection.sadd('selected_%s' % user_id, course_id)
                return Response({'message': "状态切换成功"}, status=status.HTTP_200_OK)

            except:
                return Response({"message": "该课程不存在"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            redis_connection.srem('selected_%s' % user_id, course_id)
            return Response({'message': "取消成功"}, status=status.HTTP_200_OK)

    def delete_course(self, request):
        """从购物车中删除某个课程"""
        course_id = request.data.get('course_id')
        user_id = request.user.id
        select = request.data.get('selected')
        redis_connection = get_redis_connection("cart")

        try:
            redis_connection.hdel('cart_%s' % user_id, course_id)
            redis_connection.srem('selected_%s' % user_id, course_id)
            cart_length = redis_connection.hlen("cart_%s" % user_id)
            return Response({'message': "删除成功", "cart_length": cart_length}, status=status.HTTP_200_OK)

        except:
            return Response({"message": "该课程不存在"}, status=status.HTTP_400_BAD_REQUEST)

    def expire_change(self, request):
        """改变redis的课程有效期"""
        course_id = request.data.get('course_id')
        user_id = request.user.id
        expire_id = request.data.get("expire")
        redis_connection = get_redis_connection("cart")

        try:
            redis_connection.hset('cart_%s' % user_id, course_id, expire_id)
            return Response({'message': "修改有效期成功"}, status=status.HTTP_200_OK)

        except:
            return Response({"message": "该课程不存在"}, status=status.HTTP_400_BAD_REQUEST)
