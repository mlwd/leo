
import cgi, os, sys, urllib
import leo_lookup

html_template = '''
<html>
<head>
<meta charset="utf-8">
<style type="text/css">
  body, h1, td, input {font-family: sans-serif; color: black}
  input {
    padding: 8px;
    border-radius: 4px;
  }
</style>
<title>Leo</title></head>
<body>
<table align="center">
<form action="leo_cgi.py" method="get">
<tr>
  <td align="center" valign="bottom" height="50">
    <b>English</b>
  </td>
</tr>
<tr>
  <td align="center">
    <input type="text" name="word_en" value="%(word_en)s" size="50">
  </td></tr>
<tr>
  <td align="center">
    <input type="submit" value="Look up">
  </td>
</tr>
</form>
  <tr><td align="center" valign="bottom" height="40">
    <b>German</b>
  </td>
</tr>
<tr>
  <td align="center">
    %(word_de)s
  </td>
</tr>
<table>
</body>
</html>
'''
query_string = os.environ.get("QUERY_STRING");
query_dict = urllib.parse.parse_qs(query_string);
word_en = query_dict.get("word_en", [""])[0];
word_de = leo_lookup.leo_lookup(word_en);

# Translation was unsuccessful when the returned word is None.
# Replace this by an empty string in the output.
if word_de == None:
  word_de = ""

html = html_template % {"word_en" : word_en, "word_de" : word_de}
print(html.encode("ascii", "xmlcharrefreplace").decode())
