import settings

class Cache():
    def __init__(self, app, **kwargs):
        self.cache_backend = settings.CACHE_BACKEND.get('handler')
        self.cache_config = settings.CACHE_BACKEND.get('config')
        app.request_class.cache = self.load_cache()

    def load_cache(self):
        try:
            return self.cache_backend(**self.cache_config)
        except Exception as e:
            print('Unable to load cache backend: {}'.format(e))
