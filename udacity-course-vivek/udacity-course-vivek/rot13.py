import webapp2
import cgi
from string import *

form="""
<form method="post">
  <h1><b>Enter some text to ROT13:</b></h1>
  <br>
  <textarea name="input_text" value="%(text)s" rows="10" cols="50"></textarea>
  <br>
  <br>
  <div style="color: red">%(error)s</div>
  <input type="submit" value="submit">
</form>
"""
def escape_html(s):
    return cgi.escape(s, quote = True)

def createrot13_text(t):
	ROT13 = maketrans(
	"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	new_t = unicode(t.translate(ROT13))

	return new_t

class MainHandler(webapp2.RequestHandler):
	def write_form(self, error="", text=""):
		self.response.write(form % {"error": error, "text": escape_html(text)})

	def get(self):
		self.write_form()

	def post(self):
		user_text = self.request.get('input_text')
		rot13_text = createrot13_text(user_text)
		rot13_text_error = rot13_text

		self.write_form(rot13_text_error,rot13_text)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)