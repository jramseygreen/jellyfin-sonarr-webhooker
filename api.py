from flask import Blueprint
from flask_parameter_validation import ValidateParameters, Json
import requests
import os
from typing import Optional

from response import response
from loader import config


api = Blueprint("api", __name__)

jellyfin_url = config['jellyfin_url']
jellyfin_api_key = config['jellyfin_api_key']


# all
@api.post('/sonarr')
@ValidateParameters()
def sonarr(eventType: Optional[str] = Json(default=None), series: Optional[dict] = Json(default=None), episodeFile: Optional[dict] = Json(default=None), deleteReason: Optional[str] = Json(default=None)):
    url = jellyfin_url + 'Library/Media/Updated'
    headers = {
        'accept': '*/*',
        'Authorization': f'MediaBrowser Token="{jellyfin_api_key}"',
        'Content-Type': 'application/json',
    }
    data = None

    if eventType == 'Download':
        data = {
            'Updates': [{'Path': f'{series["path"]}{os.sep}{episodeFile["relativePath"]}'}],
            'UpdateType': 'Created'
        }
    elif eventType == 'EpisodeFileDelete':
        if deleteReason == 'upgrade':
            data = {
                'Updates': [{'Path': f'{series["path"]}{os.sep}{episodeFile["relativePath"]}'}],
                'UpdateType': 'Modified'
            }
        if deleteReason == 'manual':
            data = {
                'Updates': [{'Path': f'{series["path"]}{os.sep}{episodeFile["relativePath"]}'}],
                'UpdateType': 'Deleted'
            }
    elif eventType == 'SeriesDelete':
        data = {
            'Updates': [{'Path': f'{series["path"]}'}],
            'UpdateType': 'Deleted'
        }
    if data:
        requests.post(url, headers=headers, json=data)

    return response.ok()


@api.post('/radarr')
@ValidateParameters()
def radarr(eventType: Optional[str] = Json(default=None), movie: Optional[dict] = Json(default=None), movieFile: Optional[dict] = Json(default=None), deleteReason: Optional[str] = Json(default=None)):
    url = jellyfin_url + 'Library/Media/Updated'
    headers = {
        'accept': '*/*',
        'Authorization': f'MediaBrowser Token="{jellyfin_api_key}"',
        'Content-Type': 'application/json',
    }
    data = None

    if eventType == 'Download':
        url = jellyfin_url + 'Library/Media/Updated'
        headers = {
            'accept': '*/*',
            'Authorization': f'MediaBrowser Token="{jellyfin_api_key}"',
            'Content-Type': 'application/json',
        }

        data = {
            'Updates': [{'Path': f'{movie["folderPath"]}/{movieFile["relativePath"]}'}],
            'UpdateType': 'Created'
        }
    elif eventType == 'MovieFileDelete':
        if deleteReason == 'upgrade':
            data = {
                'Updates': [{'Path': f'{movie["folderPath"]}{os.sep}{movieFile["relativePath"]}'}],
                'UpdateType': 'Modified'
            }
        if deleteReason == 'manual':
            data = {
                'Updates': [{'Path': f'{movie["folderPath"]}{os.sep}{movieFile["relativePath"]}'}],
                'UpdateType': 'Deleted'
            }
    elif eventType == 'SeriesDelete':
        data = {
            'Updates': [{'Path': f'{movie["folderPath"]}'}],
            'UpdateType': 'Deleted'
        }
    if data:
        requests.post(url, headers=headers, json=data)
    return response.ok()
