from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


xml_response = b'''
<pnp xmlns="urn:cisco:pnp" version="1.0" udi="PID:CSR1000V,VID:V00,SN:9KW268VR0AG">
  <request xmlns="urn:cisco:pnp:backoff" correlator="CiscoPnP-1.0-R29.90116-I1-P371-T1189547-2">
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
<pnp xmlns="urn:cisco:pnp" version="1.0" udi="PID:CSR1000V,VID:V00,SN:9KW268VR0AG">
  <info xmlns="urn:cisco:pnp:work-info" correlator="CiscoPnP-1.0-R29.90116-I1-P371-T1189547-2">
        <workInfo>
    <bye/>
   </workInfo>
  </info>
</pnp>
'''

@csrf_exempt
def work_request(request):
    return HttpResponse(xml_response,  content_type="application/xml")

@csrf_exempt
def work_response(request):
    print(request.body)
    return HttpResponse(xml_bye)
