import webapp2
import jinja2
import os

don_app_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class AboutUsHandler(webapp2.RequestHandler):
    def get(self):
        about_us_template= don_app_env.get_template('templates/about_us.html')
        self.response. write(about_us_template.render())


app = webapp2.WSGIApplication([
    ('/', AboutUsHandler)
], debug=True)
