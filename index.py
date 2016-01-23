#!/usr/bin/env python
import mysql.connector

config = {
  'user': 'admin',
  'password': 'admin',
  'host': '127.0.0.1',
  'database': 'main',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
query = ("SELECT keyword FROM main "
         "WHERE id=%(id_no)s")
cursor.execute(query, {'id_no':1})
bld_no=1
result = cursor.fetchall()
keyword= result[0][0]
cursor.close()
cnx.close()
print "Content-Type: text/html"
print
print """\
<style type="text/css">
.bold { padding:0;
	margin:0 0 1em 0;
	font-family: Arial, Verdana,  sans-serif;
	text-align: justify;
	font-size: 18pt;
	font-weight: bold;
	color: red;
	display:inline;
}
</style>
<html>
<body>
"""
print ("<h2>Hello, <div class=\"bold\">{}</div>, build number is <div class=\"bold\">{}</div></h2>".format(keyword, bld_no))

print """\
</body>
</html>
"""
