import json
import requests


class _PvP:
    def __init__(self, pvp_stats):
        self.kill_fame = pvp_stats['KillFame']
        self.death_fame = pvp_stats['DeathFame']
        self.fame_ratio = pvp_stats['FameRatio']


class _PvE:
    def __init__(self, pve_stats):
        self.total = pve_stats['Total']
        self.royal = pve_stats['Royal']
        self.outlands = pve_stats['Outlands']
        self.hellgate = pve_stats['Hellgate']


class _Gathering:
    def __init__(self, gathering_stats):
        self.fiber = gathering_stats['Fiber']['Total']
        self.hide = gathering_stats['Hide']['Total']
        self.ore = gathering_stats['Ore']['Total']
        self.rock = gathering_stats['Rock']['Total']
        self.wood = gathering_stats['Wood']['Total']
        self.all = gathering_stats['All']['Total']


class _PlayerFameStat:
    def __init__(self, lifetime_statistics, pvp_stats):
        self.pvp = _PvP(pvp_stats)
        self.pve = _PvE(lifetime_statistics['PvE'])
        self.gathering = _Gathering(lifetime_statistics['Gathering'])
        self.crafting = lifetime_statistics['Crafting']['Total']
        self.all = self.pvp.kill_fame + self.pve.total + self.gathering.all + self.crafting


#  Добавить что пользователя с таким id не существует
class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        info = self._get_info()
        self.name = info['Name']
        self.guild_id = info['GuildId']
        self.guild_name = info['GuildName']
        lifetime_stat = info['LifetimeStatistics']
        pvp_stats = {'KillFame': info['KillFame'], 'DeathFame': info['DeathFame'], 'FameRatio': info['FameRatio']}
        self.fame = _PlayerFameStat(lifetime_stat, pvp_stats)

    def _get_info(self):
        api_response = requests.session().get(f"https://gameinfo.albiononline.com/api/gameinfo/players/{self.player_id}")
        if api_response.status_code == 200:
            try:
                api_response = api_response.json()
            except Exception:
                return None
            return api_response
        else:
            return None


if __name__ == '__main__':
    Player('fE60LVCNRXyqQbYSyE2nWA')
