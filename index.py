#!/usr/bin/env python

html = """Content-type: text/html\n
 
<html>
<head>
<title>Python Porting Guide</title>
{MENU}
</head>
<body>
<br>
Input all or a portion of the known syntax for either Python2.x or Python3.x <br />
Results are based only on version differences, not every module in existence to python<br />
 
<form method=POST action='portingguide.py'>
        <p><input type=text name=search placeholder="'viewall' for everything">
        <p><input type=submit value='Search'> <!-- <input type="button" onclick="change.viewall()"        value="viewall"> -->
<br /><br />
{SEARCHED_TEXT}{SEARCHED}<br /><br />
{SEARCH_TEXT} <br /><br />
</body>
</html>
""".format(
        MENU="Hello",
        SEARCHED="HELLO",
        SEARCH_TEXT="NEW",
        SEARCHED_TEXT="NEW 2",
        )
print(html)