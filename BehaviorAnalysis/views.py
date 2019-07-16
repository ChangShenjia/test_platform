from django.shortcuts import render
import json
import logging
from django.http import HttpResponse, HttpResponseRedirect
from BehaviorAnalysis.models import UserInfo
from django.shortcuts import render_to_response
from BehaviorAnalysis.utils.common import get_ajax_msg, register_info_logic, init_filter_session


logger = logging.getLogger('BehaviorAnalysis')

# Create your views here.

def login_check(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('login_status'):
            return HttpResponseRedirect('/login/')  # ('/api/login/')
        return func(request, *args, **kwargs)

    return wrapper


def login(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('account')
        password = request.POST.get('password')

        if UserInfo.objects.filter(username__exact=username).filter(password__exact=password).count() == 1:
            logger.info('{username} 登录成功'.format(username=username))
            request.session["login_status"] = True
            request.session["now_account"] = username
            return HttpResponseRedirect('/index/')  # ('/api/index/')
        else:
            logger.info('{username} 登录失败, 请检查用户名或者密码'.format(username=username))
            request.session["login_status"] = False
            return render_to_response("login.html")
    elif request.method == 'GET':
        return render_to_response("login.html")


def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.is_ajax():
        user_info = json.loads(request.body.decode('utf-8'))
        msg = register_info_logic(**user_info)
        return HttpResponse(get_ajax_msg(msg, '恭喜您，账号已成功注册'))
    elif request.method == 'GET':
        return render_to_response("register.html")


@login_check
def log_out(request):
    """
    注销登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        logger.info('{username}退出'.format(username=request.session['now_account']))
        try:
            del request.session['now_account']
            del request.session['login_status']
            init_filter_session(request, type=False)
        except KeyError:
            logging.error('session invalid')
        return HttpResponseRedirect("/login/")  # ('/api/login/')


@login_check
def index(request):
    """
    首页
    :param request:
    :return:
    """
    # project_length = ProjectInfo.objects.count()
    # module_length = ModuleInfo.objects.count()
    # test_length = TestCaseInfo.objects.filter(type__exact=1).count()
    # suite_length = TestSuite.objects.count()
    #
    # total = get_total_values()
    manage_info = {
        # 'project_length': project_length,
        # 'module_length': module_length,
        # 'test_length': test_length,
        # 'suite_length': suite_length,
        'account': request.session["now_account"],
        # 'total': total
    }

    init_filter_session(request)
    return render_to_response('index.html', manage_info)


@login_check
def result_management(request):
    """
    结果管理
    :param request:
    :return:
    """
    account = request.session["now_account"]
    # if request.is_ajax():
    #     testconfig_info = json.loads(request.body.decode('utf-8'))
    #     msg = config_info_logic(**testconfig_info)
    #     return HttpResponse(get_ajax_msg(msg, '/api/config_list/1/'))
    # elif request.method == 'GET':
    manage_info = {
        'account': account,
        # 'project': ProjectInfo.objects.all().values('project_name').order_by('-create_time')
    }
    return render_to_response('result_management.html', manage_info)