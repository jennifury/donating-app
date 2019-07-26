import webapp2
import jinja2
import os

don_app_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):  
    
    def post(self):
        
    
app = webapp2.WSGIApplication([
    ('/', WelcomeHandler)  
], debug=True)
