from .base import *


try:
    from .production import *
    print ('production imported')
except:
    from .local import *
    print('local imported')
