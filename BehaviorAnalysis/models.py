from django.db import models
from BehaviorAnalysis.managers import UserTypeManager, UserInfoManager


# Create your models here.
class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'


class UserType(BaseTable):
    class Meta:
        verbose_name = '用户类型'
        db_table = 'UserType'

    type_name = models.CharField(max_length=20)
    type_desc = models.CharField(max_length=50)
    objects = UserTypeManager()


class UserInfo(BaseTable):
    class Meta:
        verbose_name = '用户信息'
        db_table = 'UserInfo'

    username = models.CharField('用户名', max_length=20, unique=True, null=False)
    password = models.CharField('密码', max_length=20, null=False)
    email = models.EmailField('邮箱', null=False, unique=True)
    status = models.IntegerField('有效/无效', default=1)
    # user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    objects = UserInfoManager()