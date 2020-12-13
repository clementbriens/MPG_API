import requests
import json
import sys

class MPG_API():

    def __init__(self, email, password, language = 'en-GB'):
        try:
            self.url = 'https://api.monpetitgazon.com'
            self.session = requests.Session()
            self.token, self.user = self.authenticate(email, password, language)
            self.session.headers.update({"Authorization": self.token})
            print('--- Successfully authenticated')
        except:
            print('--- Could not authenticate- verify credentials.')
            sys.exit()

    def authenticate(self, email, password, language = "en-GB"):
        payload = {"email" : email, "password" : password, "language" : language}
        r = self.session.post(self.url + '/user/signIn', json = payload)
        data = json.loads(r.text)
        return data['token'], data['userId']

    def get_wall(self, league_id):
        r = self.session.get(self.url + '/league/{}/wall'.format(league_id))
        data = json.loads(r.text)
        return data

    def get_coach(self, league_id):
        r = self.session.get(self.url + '/league/{}/coach'.format(league_id))
        data = json.loads(r.text)
        return data

    def get_current_matchday(self, league_id):
        r = self.session.get(self.url + '/league/{}/calendar'.format(league_id))
        data = json.loads(r.text)
        return data

    def get_matchday(self, league_id, day):
        r = self.session.get(self.url + '/league/{}/calendar/{}'.format(league_id,day))
        data = json.loads(r.text)
        return data

    def get_rankings(self, league_id):
        r = self.session.get(self.url + '/league/{}/ranking/detail'.format(league_id))
        data = json.loads(r.text)
        return data

    def get_rankings_scorer(self, league_id):
        r = self.session.get(self.url + '/league/{}/ranking/scorer'.format(league_id))
        data = json.loads(r.text)
        return data

    def get_rankings_player(self, league_id):
        r = self.session.get(self.url + '/league/{}/ranking/player'.format(league_id))
        data = json.loads(r.text)
        return data

    def get_rankings_team(self, league_id):
        r = self.session.get(self.url + '/league/{}/ranking/team'.format(league_id))
        data = json.loads(r.text)
        return data

    def get_rankings_winner(self, league_id):
        r = self.session.get(self.url + '/league/{}/ranking/winners'.format(league_id))
        data = json.loads(r.text)
        return data

    def get_teams(self, league_id):
        r = self.session.get(self.url + '/league/{}/teams'.format(league_id))
        data = json.loads(r.text)
        return data
