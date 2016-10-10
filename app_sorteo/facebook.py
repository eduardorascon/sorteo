import webapp2
import urllib2
import json
import base

class FacebookHandler(base.BaseHandler):
    client_id = '652896994869977'
    base_url = 'https://sorteoiphone7.appspot.com/fb'
    graph_url = 'https://graph.facebook.com/v2.8'

    def get(self):
        code = self.request.get('code')
        has_code = code != ''
        access_token = ''

        if has_code:
            params = (FacebookHandler.client_id, FacebookHandler.base_url, '{app-secret}', code)
            url = graph_url + '/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s' % params
            response = urllib2.urlopen(url)
            json_response = json.load(response)
            access_token = json_response['access_token']
        else:
            self.redirect('/')

        has_access_token = access_token != ''

        if has_access_token:
            self.session['access_token'] = access_token
            get_fb_user_data()
            self.redirect('/')

    def post(self):
        params = (FacebookHandler.client_id, FacebookHandler.base_url)
        url = str('https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s&response_type=code' % params)
        self.redirect(url)

    def get_fb_user_data(self):
        if self.session.get('access_token'):
            url = graph_url + '/me?fields=id,name,first_name'
            response = urllib2.urlopen(url)
            json_response = json.load(response)
            self.session['first_name'] = json_response['first_name']