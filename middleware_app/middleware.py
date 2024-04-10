class SonaliMiddleware:

    def __init__(self, get_response):
        self.get_response=get_response
        self.website = {
            'url':'https://codewithstein.com'
        }

    def __call__(self, request):
        print('call sonali')
        response=self.get_response(request)

        return response
    
    def process_template_response(self, request, response):
        print('process template response')
        response.context_data['website']=self.website
        return response