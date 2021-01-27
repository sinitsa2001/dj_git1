from datetime import datetime
from collections import OrderedDict
from urllib.parse import urlunparse, urlencode

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    # api_url = f"https://api.vk.com/method/users.get/fields=bdate,about,sex&access_token{response['access_token']}"

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields = ','.join(('bdate','sex', 'about')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)

    if resp.status_code != 200:
        return

    data =resp.json()['response'][0]

    if data['sex']:
        if data['sex'] == 2:
            user.userprofile.gender = UserProfile.MALE
        elif data['sex'] ==1:
            user.userprofile.gender = UserProfile.FEMALE

    if data['about']:
            user.userprofile.about_me = data['about']

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

        age = timezone.now().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    user.save()
