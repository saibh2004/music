from ... import utils as ytm_utils

__all__ = __name__.split('.')[-1:]

def _url(self, endpoint=None):
    return ytm_utils.url_youtube_music \
    (
        endpoint = endpoint or '',
    )