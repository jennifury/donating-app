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
        self.response.write(about_us_template.render())

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        donation_template = don_app_env.get_template('templates/homepage.html')
        self.response.write(donation_template.render())

class NewPostHandler(webapp2.RequestHandler):
    def get(self):
        post_template= don_app_env.get_template('templates/post_upload.html')
        self.response.write(post_template.render())

    def post(self):
        post_template= don_app_env.get_template('templates/post_upload.html')
        poster_name = self.request.get('name')
        post_item = self.request.get('item')
        post_pic = self.request.get('pic')
        post_desc = self.request.get('paragraph')
        self.response.write(post_template.render())

class ItemHandler(webapp2.RequestHandler):
    def get(self):
        item_template= don_app_env.get_template('templates/item_page.html')
        self.response.write(item_template.render())

class DonationDisplayHandler(webapp2.RequestHandler):
    def get(self):
        donation_display_template= don_app_env.get_template('templates/donation_display.html')
        self.response.write(donation_display_template.render())


app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/about_us', AboutUsHandler),
    ('/donation_display', DonationDisplayHandler),
    ('/newdonation', NewPostHandler),
    ('/item', ItemHandler)
], debug=True)
