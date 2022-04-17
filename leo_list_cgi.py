
import cgi, os, sys
import leo_db

# HTML template.
html_begin = '''
<html>
<head>
<meta charset="utf-8">
<style type="text/css">
  <!--
  body {background-color: lightgray;}
  body, h1, td, input {font-family: arial; color: black}
  -->
</style>
<title>English-German Dictionary</title></head>
<body>
<h1>English-German Dictionary</h1>
<table>
<tr>
<td></td>
<td><b>English</b></td>
<td><b>German</b></td>
</tr>
'''
html_end = '''
<table>
</body>
</html>
'''

word_list = leo_db.leo_db_list();
html = html_begin
i = 1
for word_en, word_de in word_list:
  html += "<tr>"
  html += "<td>%d</td>" % i
  html += "<td>%s</td><td>%s</td>" % (word_en, word_de)
  html += "</tr>"
  i += 1
html += html_end
print(html.encode("ascii", "xmlcharrefreplace").decode())
