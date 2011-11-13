from google.appengine.ext import webapp, db
from google.appengine.ext.webapp.util import run_wsgi_app

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.redirect("intro/index.html")
        
application = webapp.WSGIApplication([
    ('/', MainHandler),
  ])


def main():
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
