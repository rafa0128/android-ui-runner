from functools import wraps
from public.Log import Log

flag = 'IMAGE:'
log = Log()

def restart(d,pkgname):
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                d.driver.app_stop(pkgname)
                d.driver.app_start(pkgname)
        return wrapper
    return _wrapper

def exception_pass(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            pass
    return wrapper

def funlog(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.i('--> %s' % func.__qualname__)
        ret = func(*args, **kwargs)
        return ret
    return wrapper

def teststep(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('--> %s' % func.__qualname__)
            ret = func(*args, **kwargs)
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('\t<-- %s, %s, %s', func.__qualname__, 'AssertionError', 'Error')
            raise AssertionError(e)
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('\t<-- %s, %s, %s', func.__qualname__, 'Exception', 'Error')
            raise Exception(e)
    return wrapper


def teststeps(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.i('--> %s' % func.__qualname__)
            ret = func(*args, **kwargs)
            log.d('  <-- %s, %s', func.__qualname__, 'Success')
            return ret
        except AssertionError as e:
            log.e('AssertionError, %s', e)
            log.e('  <-- %s, %s, %s', func.__qualname__, 'AssertionError', 'Error')
            raise AssertionError(e)
        except Exception as e:
            log.e('Exception, %s', e)
            log.e('  <-- %s, %s, %s', func.__qualname__, 'Exception', 'Error')
            raise Exception(e)
    return wrapper


def testcase(d):
    def testcase(func):
        def wrapper(*args, **kwargs):
            try:
                log.d('--> %s', func.__qualname__)
                ret = func(*args, **kwargs)
                log.d('<-- %s, %s\n', func.__qualname__, 'Success')
                return ret
            except AssertionError as e:
                log.e('AssertionError, %s', e)
                log.e('<-- %s, %s, %s\n', func.__qualname__, 'AssertionError', 'Fail')

                if flag in str(e):
                    raise AssertionError(e)
                else:
                    raise AssertionError(d.screenshot(func.__qualname__))
            except Exception as e:
                log.e('Exception, %s', e)
                log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', 'Error')

                if flag in str(e):
                    raise Exception(e)
                else:
                    raise Exception(d.screenshot(func.__qualname__))
        return wrapper
        
    return testcase

# def testcase(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             log.d('--> %s', func.__qualname__)
#             ret = func(*args, **kwargs)
#             log.d('<-- %s, %s\n', func.__qualname__, 'Success')
#             return ret
#         except AssertionError as e:
#             log.e('AssertionError, %s', e)
#             log.e('<-- %s, %s, %s\n', func.__qualname__, 'AssertionError', 'Fail')

#             if flag in str(e):
#                 raise AssertionError(e)
#             else:
#                 raise AssertionError(d.screenshot(func.__qualname__))
#         except Exception as e:
#             log.e('Exception, %s', e)
#             log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', 'Error')

#             if flag in str(e):
#                 raise Exception(e)
#             else:
#                 raise Exception(d.screenshot(func.__qualname__))
#     return wrapper

def _wrapper1(d):
    def _wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                log.d('--> %s', func.__qualname__)
                ret = func(*args, **kwargs)
                log.d('<-- %s, %s\n', func.__qualname__, 'Success')
                return ret
            except AssertionError as e:
                log.e('AssertionError, %s', e)
                log.e('<-- %s, %s, %s\n', func.__qualname__, 'AssertionError', 'Fail')

                if flag in str(e):
                    raise AssertionError(e)
                else:
                    raise AssertionError(d.screenshot(func.__qualname__))
            except Exception as e:
                log.e('Exception, %s', e)
                log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', 'Error')

                if flag in str(e):
                    raise Exception(e)
                else:
                    raise Exception(d.screenshot(func.__qualname__))
        return wrapper
    return _wrapper

# def _wrapper(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             log.d('--> %s', func.__qualname__)
#             ret = func(*args, **kwargs)
#             log.d('<-- %s, %s\n', func.__qualname__, 'Success')
#             return ret
#         except AssertionError as e:
#             log.e('AssertionError, %s', e)
#             log.e('<-- %s, %s, %s\n', func.__qualname__, 'AssertionError', 'Fail')

#             if flag in str(e):
#                 raise AssertionError(e)
#             else:
#                 raise AssertionError(d.screenshot(func.__qualname__))
#         except Exception as e:
#             log.e('Exception, %s', e)
#             log.e('<-- %s, %s, %s\n', func.__qualname__, 'Exception', 'Error')

#             if flag in str(e):
#                 raise Exception(e)
#             else:
#                 raise Exception(d.screenshot(func.__qualname__))
#     return wrapper


def setup(d):
    return _wrapper1(d)


def teardown(d):
    return _wrapper1(d)


def setupclass(d):
    return _wrapper1(d)


def teardownclass(d):
    return _wrapper1(d)
