from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

import os


# Create your views here.
def echo_view(request):
    # Check the request method and get the appropriate data

    '''
    if request.method == 'GET':
        data = request.GET
    elif request.method == 'POST':
        data = request.POST
    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)
    '''

    data = {}
    data['env'] = {}
    data['request'] = {}

    env = dict(os.environ)
    env_keys = sorted(list(env.keys()))
    for ek in env_keys:
        data['env'][ek] = env[ek]

    data['request']['META'] = {}
    mkeys = sorted(list(request.META.keys()))
    for mkey in mkeys:
        data['request']['META'][mkey] = str(request.META[mkey])

    # make a reverse url
    data['echo_reverse'] = reverse('echo')
    data['absolute'] = request.build_absolute_uri('/echo')

    # Return the data as JSON response
    return JsonResponse(data)
