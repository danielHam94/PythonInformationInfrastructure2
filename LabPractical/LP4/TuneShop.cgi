#! /usr/bin/env python3

print('Content-type: text/html\n')

import MySQLdb, cgi

string = "i211s19_hamsu" 			#change this to yours
password = "my+sql=i211s19_hamsu"	#change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

def results_table(records):
    html = """
    <!doctype html>
    <html>
    <head><meta charset="utf-8">
    <title>Welcome to the Tune Shop</title></head>
        <body>
            <h1>Welcome to the Tune Shop</h1>
            <table border='1' width='70%'>
            <tr><th>SongID</th><th>Song</th><th>Artist</th><th>Price</th><th>Buy</th></tr>
            {content}
            </table>          
        </body>
    </html>"""

    table =""
    for row in records:
        table+="<tr>"
        for item in row:
            table +="<td align='center'>"+str(item)+"</td>"
        table += "<td align='center'><a href='Sold.cgi" + str(row[0]) + "'>Buy</a></td></tr>"
    print(html.format(content=table))

try:
    SQL = "SELECT * FROM Songs;"
    cursor.execute(SQL)
    results = cursor.fetchall()

except:
    print ('<p>Something went wrong with the SQL!</p>')
    print (SQL)
    print ("\nError:", e)
else:
    results_table(results)

