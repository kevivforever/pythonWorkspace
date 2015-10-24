import cgi
def escape_html(s):
    for (i,o) in (("&", "&amp;"),
                 (">", "&gt;"),
                 ("<", "&lt;"),
                 ('"', "&quot;")):
        s = s.replace(i,o)
    return s

def escape_html_cgi(s):
    return cgi.escape(s, quote = True)

print escape_html("vivek>keviv")
print escape_html("<b>html!</b>")
print escape_html('"hello, & = &amp;"')
print
print "now printing using cgi"
print escape_html_cgi("vivek>keviv")
print escape_html_cgi("<b>html!</b>")
print escape_html_cgi('"hello, & = &amp;"')
