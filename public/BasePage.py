from public.Decorator import *
from public.Common import *

d = Driver()

class Elements:
    resourceId = 'resourceId'
    className = 'className'
    text = 'text'
    description = 'description'


class CommonOperations(object):

    @restart(d, d.pkgname)
    @classmethod
    def case_restart_check(self,text=None,resourceId=None,restart=False):
        """用例是否需要重新启动检查"""
        if text is not None:
            self.d(text=text).click(timeout=2)
        elif resourceId is not None:
            self.d(resourceId=text).click(timeout=2)
        elif restart is True:
            raise Exception('restart')
    
    @exception_pass
    @classmethod
    def start_page_control():
        """开屏页处理"""
        pass
    
    @exception_pass
    @classmethod
    def ad_control():
        """广告处理"""
        pass

class Action(object):

    @classmethod
    def exist_click(cls, elements, value, timeout=3):
        """判断元素是否存在才点击"""
        match(elements):
            case Elements.resourceId:
                if d.driver(resourceId=value).exists(timeout=timeout):
                    d.driver(resourceId=value).click()
            case Elements.className:
                if d.driver(className=value).exists(timeout=timeout):
                    d.driver(className=value).click()
            case Elements.text:
                if d.driver(text=value).exists(timeout=timeout):
                    d.driver(text=value).click()
            case Elements.description:
                if d.driver(description=value).exists(timeout=timeout):
                    d.driver(description=value).click()
            case _:
                raise Exception('{} is undefined'.format(elements))                                
        