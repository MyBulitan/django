from django.conf import settings
import re

def get(key, default):
    return getattr(settings, key, default)

ADMIN_EMAIL = get('ADMIN_EMAIL', 'alafin@python.su')
TOPIC_PAGE_SIZE = get('TOPIC_PAGE_SIZE', 10)
FORUM_PAGE_SIZE = get('FORUM_PAGE_SIZE', 20)
USERS_PAGE_SIZE = get('USERS_PAGE_SIZE', 20)
AVATARS_UPLOAD_TO = get('AVATARS_UPLOAD_TO', 'forum/avatars')
AVATAR_WIDTH = get('AVATAR_WIDTH', 60)
AVATAR_HEIGHT = get('AVATAR_HEIGHT', 60)
GRAVATAR_SUPPORT = get('GRAVATAR_SUPPORT', True)
GRAVATAR_DEFAULT = get('GRAVATAR_DEFAULT', 'identicon')
DEFAULT_TIME_ZONE = get('DEFAULT_TIME_ZONE', 3)
SIGNATURE_MAX_LENGTH = get('SIGNATURE_MAX_LENGTH', 1024)
SIGNATURE_MAX_LINES = get('SIGNATURE_MAX_LINES', 3)
READ_TIMEOUT = get('READ_TIMEOUT', 3600 * 24 * 7)
HEADER = get('HEADER', 'DjangoBB')
TAGLINE = get('TAGLINE', 'Django based forum engine')
DEFAULT_MARKUP = get('DEFAULT_MARKUP', 'bbcode')
NOTICE = get('NOTICE', '')
HOST = get('HOST', 'localhost:8000')
USER_ONLINE_TIMEOUT = get('USER_ONLINE_TIMEOUT', 30)
EMAIL_DEBUG = get('FORUM_EMAIL_DEBUG', False)

FORUM_STAR_0 = get('FORUM_STAR_0', 0)
FORUM_STAR_0_HALF = get('FORUM_STAR_0_HALF', 10)
FORUM_STAR_1 = get('FORUM_STAR_1', 25)
FORUM_STAR_1_HALF = get('FORUM_STAR_1_HALF', 50)
FORUM_STAR_2 = get('FORUM_STAR_2', 75)
FORUM_STAR_2_HALF = get('FORUM_STAR_2_HALF', 100)
FORUM_STAR_3 = get('FORUM_STAR_3', 150)
FORUM_STAR_3_HALF = get('FORUM_STAR_3_HALF', 200)
FORUM_STAR_4 = get('FORUM_STAR_4', 300)
FORUM_STAR_4_HALF = get('FORUM_STAR_4_HALF', 500)
FORUM_STAR_5 = get('FORUM_STAR_5', 1000)

EMOTION_SMILE = get('EMOTION_SMILE', '<img src="%sforum/img/smilies/smile.png">' % settings.MEDIA_URL)
EMOTION_NEUTRAL = get('EMOTION_NEUTRAL', '<img src="%sforum/img/smilies/neutral.png">' % settings.MEDIA_URL)
EMOTION_SAD = get('EMOTION_SAD', '<img src="%sforum/img/smilies/sad.png">' % settings.MEDIA_URL)
EMOTION_BIG_SMILE = get('EMOTION_BIG_SMILE', '<img src="%sforum/img/smilies/big_smile.png">' % settings.MEDIA_URL)
EMOTION_YIKES = get('EMOTION_YIKES', '<img src="%sforum/img/smilies/yikes.png">' % settings.MEDIA_URL)
EMOTION_WINK = get('EMOTION_WINK', '<img src="%sforum/img/smilies/wink.png">' % settings.MEDIA_URL)
EMOTION_HMM = get('EMOTION_HMM', '<img src="%sforum/img/smilies/hmm.png">' % settings.MEDIA_URL)
EMOTION_TONGUE = get('EMOTION_TONGUE', '<img src="%sforum/img/smilies/tongue.png">' % settings.MEDIA_URL)
EMOTION_LOL = get('EMOTION_LOL', '<img src="%sforum/img/smilies/lol.png">' % settings.MEDIA_URL)
EMOTION_MAD = get('EMOTION_MAD', '<img src="%sforum/img/smilies/mad.png">' % settings.MEDIA_URL)
EMOTION_ROLL = get('EMOTION_ROLL', '<img src="%sforum/img/smilies/roll.png">' % settings.MEDIA_URL)
EMOTION_COOL = get('EMOTION_COOL', '<img src="%sforum/img/smilies/cool.png">' % settings.MEDIA_URL)
SMILES = ((r'(:|=)\)', EMOTION_SMILE), #:), =)
          (r'(:|=)\|',  EMOTION_NEUTRAL), #:|, =| 
          (r'(:|=)\(', EMOTION_SAD), #:(, =(
          (r'(:|=)D', EMOTION_BIG_SMILE), #:D, =D
          (r':o', EMOTION_YIKES), # :o, :O
          (r';\)', EMOTION_WINK), # ;\ 
          (r':/', EMOTION_HMM), #:/
          (r':P', EMOTION_TONGUE), # :P
          (r':lol:', EMOTION_LOL),
          (r':mad:', EMOTION_MAD),
          (r':rolleyes:', EMOTION_ROLL),
          (r':cool:', EMOTION_COOL)
         )
SMILES = get('SMILES', SMILES)