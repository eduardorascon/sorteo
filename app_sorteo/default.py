import webapp2
import os
from google.appengine.ext.webapp import template

class DefaultHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'title': 'Test'
        }
        
        path = os.path.join(os.path.dirname(__file__), '../html/default.html')
        self.response.write(template.render(path, template_values))