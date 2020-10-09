from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import random
import math


backoff_request = b'''
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

info_request = b'''
<pnp xmlns="urn:cisco:pnp" version="1.0" udi="{{ udi }}">
  <request correlator="{{ correlator }}" xmlns="urn:cisco:pnp:device-info">
   <deviceInfo type="all"/>
  </request>
</pnp>
'''

capability_request = b"""
<pnp xmlns="urn:cisco:pnp" version="1.0" udi="{{ udi }}">
  <request correlator="{{ correlator }}" xmlns="urn:cisco:pnp:capability" />
  </request>
</pnp>
"""

xml_bye = b'''
<pnp xmlns="urn:cisco:pnp" version="1.0" udi="{{ udi }}">
  <info xmlns="urn:cisco:pnp:work-info" correlator="{{ correlator }}">
        <workInfo>
    <bye/>
   </workInfo>
  </info>
</pnp>
'''

requests = [
    backoff_request,
    info_request,
    capability_request
]

@csrf_exempt
def work_request(request):
    req_type = random.random() * len(requests)
    req = requests[math.floor(req_type)]
    correlator = request.pnp[0].attrib.get("correlator").encode()
    udi = request.pnp.attrib.get("udi").encode()
    response = req.replace(b"{{ udi }}", udi)
    response = response.replace(b"{{ correlator }}", correlator)
    print(request.body)
    print(response)
    return HttpResponse(response,  content_type="application/xml")

@csrf_exempt
def work_response(request):
    print(request.body)
    correlator = request.pnp[0].attrib.get("correlator").encode()
    udi = request.pnp.attrib.get("udi").encode()
    response = xml_bye.replace(b"{{ udi }}", udi)
    response = response.replace(b"{{ correlator }}", correlator)
    return HttpResponse(response)
