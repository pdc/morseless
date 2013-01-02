# Create your views here.

import json
import logging
from django.http import HttpResponse

logging.addLevelName(5, 'TRACE')

def log(request, log_name):
    many_data = json.loads(request.POST['data'])
    for data in many_data:
        full_name = '.'.join([__name__, log_name, data['logger']])
        logger = logging.getLogger(full_name)
        for msg in data['message']:
            level = getattr(logging, data['level'])
            logger.log(level, msg)
    return HttpResponse('{success: true}', content_type='application/json')

