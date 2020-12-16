from rest_framework.serializers import ModelSerializer

from course.models import CourseCategory, Course, Teacher, CourseLesson, CourseChapter


class CourseCategoryModelSerializer(ModelSerializer):
    """课程分类"""

    class Meta:
        model = CourseCategory
        fields = ("id", "name")


class TeacherModelSerializer(ModelSerializer):
    """讲师"""

    class Meta:
        model = Teacher
        fields = ("id", "name", "title", "brief", "image", "signature")


class CourseLessonSerializer(ModelSerializer):
    """课程课时"""
    model = CourseLesson
    fields = ('id', 'name', 'duration', 'free_trail')


class CourseChapterSerializer(ModelSerializer):
    """课程章节"""
    course_lession = CourseLessonSerializer()
    model = CourseChapter
    fields = ('id', 'name', 'chapter', 'course_lession')


class CourseModelSerializer(ModelSerializer):
    """课程列表"""

    teacher = TeacherModelSerializer()

    class Meta:
        model = Course
        fields = ("id", "name", "course_img", "students", "lessons", "pub_lessons", "brief_html",
                  "price", "teacher", "lesson_list", "level_name", "chapter_list", 'discount_name',
                  'discount_price', 'active_time')
