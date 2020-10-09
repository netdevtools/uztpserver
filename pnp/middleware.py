import xml.etree.ElementTree as ET


class PnpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.body.startswith(b'<pnp xmlns="urn:cisco:pnp"'):
            request.pnp = ET.fromstring(request.body)
            print(request.pnp)
            print(request.headers)
        response = self.get_response(request)

        return response
