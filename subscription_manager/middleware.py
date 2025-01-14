class ReferrerPolicyMiddleware:
    """
    Middleware to set the Referrer-Policy header in HTTP responses.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'  # Adjust this policy as needed
        return response
