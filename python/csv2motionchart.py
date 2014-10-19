#!/usr/bin/python
from __future__ import print_function
import csv
import sys
import datetime

title = "Google Motion Chart csv converter Test"
html_file_name = "personal.html"

def getType(string):
    if not string:
        return "number"
    try:
        float(string)
        return "number"
    except ValueError:
        return "string"

def csv2motionchart(csvfile, title, delimiter=',', quotechar='"'):
    """
    This function takes in an csv file and a title and returns a html file with a working Google Motion Chart.
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
            # Google Motion Charts requires ID to be the first field and date to be the second.
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
                    # Google Motion Chart will treat "" as a null value and ether remove bobles where it has no data.
                    # Or interplolate if it as      an value for this field before and after.
                    attributes.append("")

            # data_javascript rows should be on this format:
            # ['Apples',  new Date('2011-04-11'), 1000, 300, 'East'],

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
        options['state'] = '{"iconType":"BUBBLE","dimensions":{"iconDimensions":["dim0"]},"xAxisOption":"10","yZoomedDataMin":-656,"uniColorForNonSelected":false,"sizeOption":"2","showTrails":true,"yLambda":0,"yZoomedIn":false,"xZoomedDataMax":801083,"orderedByY":false,"iconKeySettings":[],"duration":{"multiplier":1,"timeUnit":"D"},"nonSelectedAlpha":0.4,"xZoomedDataMin":5,"colorOption":"3","time":"2014-07-09","yZoomedDataMax":47543,"playDuration":15000,"yAxisOption":"51","xZoomedIn":false,"xLambda":0,"orderedByX":false}';
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
        print("Exmample: cat file.csv | ./csv2motonchart.py > personal.html", file=sys.stderr)
        print("Or: ./csv2motionchart.py file.csv > motionchart.html", file=sys.stderr)
        sys.exit(1)

    title = "personal"
    print(csv2motionchart(csvfile, title))
        