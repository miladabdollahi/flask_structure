try:
    from configs.local import *
except ImportError:
    from configs.production import *
