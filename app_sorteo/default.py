import webapp2
import os
from google.appengine.ext.webapp import template
import base

class DefaultHandler(base.BaseHandler):
    def get(self):

    	title = 'Prueba Appengine'
    	if self.session.get('name') != None:
    		title = self.session.get('name')

        template_values = {
            'title': title
        }
        
        path = os.path.join(os.path.dirname(__file__), '../templates/default.html')
        self.response.write(template.render(path, template_values))