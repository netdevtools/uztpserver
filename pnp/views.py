from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


xml_response = b'''
<pnp xmlns="urn:cisco:pnp" version="1.0" udi="{{ udi }}">
  <request xmlns="urn:cisco:pnp:backoff" correlator="{{ correlator }}">
   <backoff>
    <reason>backoffNow</reason>
    <callbackAfter>
     <seconds>20</seconds>
    </callbackAfter>
   </backoff>
  </request>
</pnp>
'''

xml_bye = b'''
<pnp xmlns="urn:cisco:pnp" version="1.0" udi="{{ udi }}">
  <info xmlns="urn:cisco:pnp:work-info" correlator="{{ correlator }}">
        <workInfo>
    <bye/>
   </workInfo>
  </info>
</pnp>
'''

@csrf_exempt
def work_request(request):
    correlator = request.pnp[0].attrib.get("correlator").encode()
    udi = request.pnp.attrib.get("udi").encode()
    response = xml_response.replace(b"{{ udi }}", udi)
    response = response.replace(b"{{ correlator }}", correlator)
    return HttpResponse(response,  content_type="application/xml")

@csrf_exempt
def work_response(request):
    correlator = request.pnp[0].attrib.get("correlator").encode()
    udi = request.pnp.attrib.get("udi").encode()
    response = xml_bye.replace(b"{{ udi }}", udi)
    response = response.replace(b"{{ correlator }}", correlator)
    return HttpResponse(response)
