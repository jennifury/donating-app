import webapp2
import jinja2
import os
from google.appengine.ext import ndb

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

class NewPost(ndb.Model):
    name = ndb.StringProperty(required=True)
    item = ndb.StringProperty(required=True)
    paragraph = ndb.StringProperty(required=True)

class NewPostHandler(webapp2.RequestHandler):
    def get(self):
        post_template= don_app_env.get_template('templates/post_upload.html')
        self.response.write(post_template.render())

    def post(self):
        poster_name = self.request.get('name')
        post_item = self.request.get('item')
        post_pics = self.request.get('pics')
        post_desc = self.request.get('paragraph')

        new_name = NewPost(name=poster_name, item = post_item, paragraph = post_desc)
        new_name.put()
        self.redirect("/thankyou")


class ItemHandler(webapp2.RequestHandler):
    def get(self):
        item_template= don_app_env.get_template('templates/item_page.html')
        self.response.write(item_template.render())

class DonationDisplayHandler(webapp2.RequestHandler):
    def get(self):
        donation_display_template= don_app_env.get_template('templates/donation_display.html')
        self.response.write(donation_display_template.render())

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        thanks_template= don_app_env.get_template('templates/thank_you.html')
        self.response.write(thanks_template.render())

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/about_us', AboutUsHandler),
    ('/donation_display', DonationDisplayHandler),
    ('/newdonation', NewPostHandler),
    ('/item', ItemHandler),
    ('/thankyou', ThanksHandler)
], debug=True)
