import webapp2
import urllib2
import json
import base

class FacebookHandler(base.BaseHandler):
    client_id = '652896994869977'
    base_url = 'https://sorteoiphone7.appspot.com/fb'
    graph_url = 'https://graph.facebook.com/v2.8'
    app_secret = 'app_secret' #replace with the real app_secret from fb

    def get(self):
        code = self.request.get('code')
        access_token = ''

        if code != '':
            params = (self.client_id, self.base_url, self.app_secret, code)
            url = self.graph_url + '/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s' % params
            response = urllib2.urlopen(url)
            json_response = json.load(response)
            access_token = json_response['access_token']
        else:
            self.redirect('/')

        if access_token != '':
            self.session['access_token'] = access_token
            self.get_fb_user_data()
            self.redirect('/')

    def post(self):
        params = (self.client_id, self.base_url)
        url = str('https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&response_type=code' % params)
        self.redirect(url)

    def get_fb_user_data(self):
        if self.session.get('access_token') != None:
            url = self.graph_url + '/me?fields=id,name&access_token=' + self.session.get('access_token')
            response = urllib2.urlopen(url)
            json_response = json.load(response)
            self.session['name'] = json_response['name']