import json
import requests


class _SearchInfoGuild:
    def __init__(self, guild_id, guild_name, alliance_id):
        self.id = guild_id
        self.name = guild_name
        self.ally_id = alliance_id
        self.ally_tag = 0

    def _get_ally_id(self):
        pass


class _SearchInfoPlayer:
    def __init__(self, player_id, player_name):
        self.id = player_id
        self.name = player_name


class Search:
    def __init__(self, request):
        self.request = request
        self.players, self.guilds = self._get_object_list()

    def _get_object_list(self):
        # Достать данные игроков
        def _get_player_args(resp_object):
            return _SearchInfoPlayer(resp_object['Id'], resp_object['Name'])

        # Достать данные гильдий
        def _get_guild_args(resp_object):
            return _SearchInfoGuild(resp_object['Id'], resp_object['Name'], resp_object['AllianceId'])

        api_response = requests.session().get(f"https://gameinfo.albiononline.com/api/gameinfo/search?q={self.request}")
        try:
            api_response = api_response.json()
        except Exception:
            return None, None
        return map(_get_player_args, api_response['players']), map(_get_guild_args, api_response['guilds'])

