import xadmin

from course.models import CourseCategory, Course, Teacher, CourseChapter, CourseLesson, \
    CourseDiscountType, Activity, CoursePriceDiscount, CourseDiscount, CourseExpire


class CourseCategoryAdmin(object):
    """课程分类表"""
    pass


xadmin.site.register(CourseCategory, CourseCategoryAdmin)


class CourseAdmin(object):
    """课程信息表"""
    pass


xadmin.site.register(Course, CourseAdmin)


class TeacherAdmin(object):
    """讲师表"""
    pass


xadmin.site.register(Teacher, TeacherAdmin)


class CourseChapterAdmin(object):
    """章节表"""
    pass


xadmin.site.register(CourseChapter, CourseChapterAdmin)


class CourseLessonAdmin(object):
    """课时表"""
    pass


xadmin.site.register(CourseLesson, CourseLessonAdmin)


class CourseDiscountTypeAdmin(object):
    """课程优惠类型模型"""
    pass


xadmin.site.register(CourseDiscountType, CourseDiscountTypeAdmin)


class ActivityAdmin(object):
    """课程优惠时间表"""
    pass


xadmin.site.register(Activity, ActivityAdmin)


class CoursePriceDiscountAdmin(object):
    """课程与价格策略关系表"""
    pass


xadmin.site.register(CoursePriceDiscount, CoursePriceDiscountAdmin)


class CourseDiscountAdmin(object):
    """课程与价格策略关系表"""
    pass


xadmin.site.register(CourseDiscount, CourseDiscountAdmin)


class CourseExpireAdmin(object):
    """课程与价格策略关系表"""
    pass


xadmin.site.register(CourseExpire, CourseExpireAdmin)
