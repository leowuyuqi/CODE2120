from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys

# Create your views here.

def ezpz_get(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s: %s" %(var_a + " Love", var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def caculate(request):
	jsob = {'x1':0,'x2':0}
	log = []
	if request.method == 'POST':
		try:
			data = request.POST['data']
			received = json.loads(data)
			jsob.update(received)


			r = int(jsob['n1'])+int(jsob['n2'])
			x = int(jsob['n1'])-int(jsob['n2'])
			result = {'sum':r, 'diff':x}
			return JsonResponse(result)
			
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse('Only return post request')
