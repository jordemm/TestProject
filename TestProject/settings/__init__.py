from .base import *


try:
    from .production import *
    print ('local imported')
except:
    from .local import *
    print ('production imported')