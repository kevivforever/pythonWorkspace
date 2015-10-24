import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

hidden_html = """
<input type="hidden" name="food" value="%s">
"""
item_html = "<li>%s</li>"

shopping_list_html ="""
<br>
<br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))
		

class MainPage(Handler):
	def get(self):
		items = self.request.get_all("food")
		self.render("shopping_list.html", items = items)

class stmthandler(Handler):
	def get(self):
		n = self.request.get('n')
		n = n and int(n)
		self.render('statement_syntax.html', n = n)

class loophandler(Handler):
	def get(self):
		n = self.request.get('n')
		n = n and int(n)
		self.render('loop_syntax.html', n = n)

class Fizzbuzzhandler(Handler):
	def get(self):
		n = self.request.get('n', 0)
		n = n and int(n)
		self.render('fizzbuzz.html', n = n)
		
app = webapp2.WSGIApplication([('/',MainPage),('/fizzbuzz',Fizzbuzzhandler),('/loop',loophandler),('/stmt',stmthandler)],debug=True)

	
		