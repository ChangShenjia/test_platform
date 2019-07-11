from BehaviorAnalysis.utils.operation import add_register_data


def register_info_logic(**kwargs):
    """

    :param kwargs:
    :return:
    """
    return add_register_data(**kwargs)

def get_ajax_msg(msg, success):
    """
    ajax提示信息
    :param msg: str：msg
    :param success: str：
    :return:
    """
    return success if msg is 'ok' else msg

def init_filter_session(request, type=True):
    """
    init session
    :param request:
    :return:
    """
    if type:
        request.session['user'] = ''
        request.session['name'] = ''
        request.session['project'] = 'All'
        request.session['module'] = '请选择'
        request.session['report_name'] = ''
    else:
        del request.session['user']
        del request.session['name']
        del request.session['project']
        del request.session['module']
        del request.session['report_name']