from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
    
    
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('''<html>
                                    <body>
                                    <div contentEditable="true" id="editable"    style="position:absolute;top:15%;left:10%;width:200px;height:120px;border: medium solid yellow;color: black;background: white;"></div>
                                    <div>
                                        <input id="fileUpload" type="file" />
                                    </div
                                    </body>
                                   </html>''')


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
