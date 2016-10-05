import webapp2
import urllib2

class FacebookHandler(webapp2.RequestHandler):
    client_id = '652896994869977'
    base_url = 'https://sorteoiphone7.appspot.com/fb'

    def get(self):
        code = self.request.get('code')
        
        if not code == '':
            params = (client_id, base_url, '{app-secret}', code)
            url = str('https://graph.facebook.com/v2.7/oauth/access_token?client_id=%s&redirect_uri=%s&client_secret=%s&code=%s' % params)
            response = urllib2.urlopen(url)
            html = response.read()
            self.response.write(html)

        access_token = self.request.get('access_token')
        
        if not access_token == '':
            self.redirect('../')

    def post(self):
        params = (client_id, base_url)
        url = str('https://www.facebook.com/dialog/oauth?client_id=%s&redirect_uri=%s' % params)
        self.redirect(url)