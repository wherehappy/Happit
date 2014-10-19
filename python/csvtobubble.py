#!/usr/bin/python
from __future__ import print_function
import csv
import sys
import datetime

title = ""
html_file_name = "personal.html"

def getType(string):
    if not string:
        return "number"
    try:
        float(string)
        return "number"
    except ValueError:
        return "string"

def csv2bubble(csvfile, title, delimiter=',', quotechar='"'):
    """
csv to motion
    """

    columns_as_javascript = []
    datarows_as_javascript = []

    csvfile = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
    try:
        columns = csvfile.next()
        first_row = csvfile.next()

        columns_as_javascript.append("data.addColumn('%s', '%s');" % ("string", "ID"))
        columns_as_javascript.append("data.addColumn('%s', '%s');" % ("date", "date"))

        for column_number in range(len(columns))[2:]:
            column_type = getType(first_row[column_number])
            column_name = columns[column_number].replace("_", " ").title()
            columns_as_javascript.append("data.addColumn('%s', '%s');" % (column_type, column_name))

        def row2javascript(row):
            attributes = []
            try:
                datetime.datetime.strptime("2014-06-01", '%Y-%m-%d')
                attributes.append("'%s'" % row[0])  # Id
            except ValueError:
                attributes.append("'1970-01-01'" % row[0])  # Id
            attributes.append("new Date('%s')" % row[1])  # Date

            for column_number in range(len(columns))[2:]:
                # If string surround with '', if number append as it is, if type unknown don't append
                try:
                    if getType(first_row[column_number]) == "string":
                        attributes.append("'%s'" % row[column_number])

                    elif getType(first_row[column_number]) == "number":
                        if row[column_number] == "":
                            attributes.append("NaN")
                        else:
                            attributes.append(str(row[column_number]))
                except IndexError:
                    attributes.append("")

            attributes_joined = ", ".join(attributes)
            datarows_as_javascript.append("\t[%s]" % attributes_joined)

        row2javascript(first_row)
        for row in csvfile:
            row2javascript(row)

        # Insert in HTML

        html = "<!DOCTYPE html>\n<html><head>\n"
        html += "<title>%s</title>" % title
        html += """
        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
        <script type="text/javascript">
        google.load('visualization', '1', {'packages':['motionchart']});
        google.setOnLoadCallback(drawChart);
        function drawChart() {
        var data = new google.visualization.DataTable();
        """
        html += "\n"
        html += "\n".join(columns_as_javascript)
        html += "\n\n"
        html += "data.addRows([\n"+ ",\n".join(datarows_as_javascript)  + "\n]);"
        html += "\n\n"
        html += """
        // This should be a json object INSIDE A STRING.
        var options = {}
        options['state'] = '{}';
        options['width'] = 1000;
        options['height'] = 700;

        var chart = new google.visualization.MotionChart(document.getElementById('chart_div'));


        chart.draw(data, options);
        }
        </script>
        </head>

        <body>"""

        html += "<h1>%s</h1>" % title
        html += """
        <div id="chart_div" style="width: 800px; height: 600px;"></div>
        </body>
        </html>"""

    except StopIteration:
        print("The CSV file should have at least an header and one row.", file=sys.stderr)

    return html

if __name__ == '__main__':
    if not sys.stdin.isatty():
        csvfile = sys.stdin
    elif sys.argv >= 2:
        csvfile = open(sys.argv[1], "r")
    else:
        print("Exmample: cat file.csv | ./csv2mothionchart.py > motionchart.html", file=sys.stderr)
        print("Or: ./csv2mothionchart.py file.csv > motionchart.html", file=sys.stderr)
        sys.exit(1)

    title = "How Others Feel"
    print(csv2motionchart(csvfile, title))
