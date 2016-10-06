import webapp2
import urllib2
import json

class FacebookHandler(webapp2.RequestHandler):
    client_id = '652896994869977'
    base_url = 'https://sorteoiphone7.appspot.com/fb'

    def get(self):
        code = self.request.get('code')
        has_code = code != ''
        access_token = ''

        if has_code:
            params = (FacebookHandler.client_id, FacebookHandler.base_url, '{app-secret}', code)
            url = 'https://graph.facebook.com/v2.7/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s' % params
            response = urllib2.urlopen(url)
            json_reponse = json.load(response)
            access_token = json_reponse['access_token']
        else:
            self.redirect('/')

        has_access_token = access_token != ''

        if has_access_token:
            self.redirect('/')

    def post(self):
        params = (FacebookHandler.client_id, FacebookHandler.base_url)
        url = str('https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s' % params)
        self.redirect(url)