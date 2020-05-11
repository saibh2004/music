'''
Package containing constants.

These constants help the super package achieve general tasks.

Example:
    >>> from ytm import constants
    >>>
    >>> constants.__all__
    ...
    >>>
'''

from ...constants import *

CHARS_ID           = '-a-zA-Z0-9_'
CHARS_PARAMS       = f'{CHARS_ID}%'
CHARS_CONTINUATION = CHARS_PARAMS

# Prefixes
PREFIX_ALBUM_ID           = 'MPREb_'
PREFIX_ALBUM_PLAYLIST_ID  = 'OLAK5uy_'
PREFIX_ARTIST_ID          = 'UC'
PREFIX_ARTIST_RADIO_ID    = 'RDEM'
PREFIX_ARTIST_SHUFFLE_ID  = 'RDAO'
PREFIX_PLAYLIST_BROWSE_ID = 'VL'
PREFIX_PLAYLIST_RADIO_ID  = 'RDAMPL'
PREFIX_CHART_PLAYLIST_ID  = 'PL'
PREFIX_PLAYLIST_ID        = 'RDCLAK5uy_'
PREFIX_SONG_RADIO_ID      = 'RDAMVM'

# Lengths
LEN_ALBUM_ID          = 17
LEN_ALBUM_PLAYLIST_ID = 41
LEN_ARTIST_ID         = 24
LEN_CHART_PLAYLIST_ID = 34
LEN_PLAYLIST_ID       = 43
LEN_SONG_ID           = 11

# Entropy Lengths
LEN_ENTROPY_ALBUM_ID          = LEN_ALBUM_ID          - len(PREFIX_ALBUM_ID)
LEN_ENTROPY_ALBUM_PLAYLIST_ID = LEN_ALBUM_PLAYLIST_ID - len(PREFIX_ALBUM_PLAYLIST_ID)
LEN_ENTROPY_ARTIST_ID         = LEN_ARTIST_ID         - len(PREFIX_ARTIST_ID)
LEN_ENTROPY_CHART_PLAYLIST_ID = LEN_CHART_PLAYLIST_ID - len(PREFIX_CHART_PLAYLIST_ID)
LEN_ENTROPY_PLAYLIST_ID       = LEN_PLAYLIST_ID       - len(PREFIX_PLAYLIST_ID)
