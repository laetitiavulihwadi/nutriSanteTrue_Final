import threading

_thread_local = threading.local()

class CurrentRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_local.request = request 
        return self.get_response(request)
    
def get_current_request():
    return getattr(_thread_local, 'request', None)