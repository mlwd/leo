Leo command line interface
--------------------------

This program is intended to be used in a terminal to quickly translate
English words into German without needing to open another program or
visiting a website. The translations are generated with a Python script
which makes a request to the online dictionary [Leo](https://www.leo.org)
by providing the given English word as a HTTP GET parameter. The HTML response
is parsed with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
to find the German translation.
A local [SQLite](https://www.sqlite.org) data base file which resides in the
same directory as these Python scripts is used to cache word pairs which have
already been seen.

Usage:
```bash
  $alias leo="python3 leo.py"
  $leo cinch
  English: cinch
  Deutsch: fester Halt, todsichere Sache, Leichtigkeit, Spielerei
```

There is also a [CGI script](leo_cgi.py) which provides the same functionality
in the browser. The CGI script can be served with [LigHTTPd](https://www.lighttpd.net/)
by using the included [configuration file](lighttpd.conf) and the [start script](lightppd.sh).

