#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def get_piechart(data,width,height):
  #Set the limit of entries which will be detailed
  detail_limit = 25
  #Remove intestation line
  data = data[1:]
  
  piechart = Pie()
  piechart.width = width
  piechart.height = height
  piechart.x = -30
  piechart.y = 0
  piechart.startAngle = 45
  
  #Set labels and data for detailed entries
  piechart.labels = [ "{enum}. {name} [{sales}]".format(enum=e+1, name=item[1], sales=item[3]) for e, item in enumerate(data[:detail_limit]) ]
  piechart.data = [ item[3]*3 for item in data[:detail_limit] ]
  #Set label and data for cumulative final slice
  piechart.labels.append("All the Others")
  piechart.data.append( sum( [car[3] for car in data[detail_limit:]] ) )
  
  #Enable advanced Labels options
  piechart.simpleLabels = 0
  #Set layout preferences for detailed entries
  for s in range(detail_limit):
    piechart.slices[s].popout = detail_limit
    piechart.slices[s].label_simple_pointer = 1
    piechart.slices[s].labelRadius = 1.5
  #Set layout preferences for "All the Others" slice
  piechart.slices[detail_limit].label_simple_pointer = 0
  piechart.slices[detail_limit].labelRadius = 0.3
  piechart.slices[detail_limit].strokeWidth = 1
  piechart.slices[detail_limit].strokeColor = colors.blue
  piechart.slices[detail_limit].fillColor = colors.red
  
  #piechart.checkLabelOverlap = 0
  
  return piechart

def get_barchart(data,width,height):
  #Set the number of bars to display
  bars_num = 10
  #Select only the required data, removing the intestation line
  data = data[1:bars_num+1]
  
  barchart = VerticalBarChart()
  barchart.width = width - 50
  barchart.height = height - 25
  
  #Populate 'values' with total revenue (item[2]*item[3] = price*units sold)
  values = [ item[2]*item[3] for item in data ]
  barchart.data = [tuple(values),]
  
  barchart.valueAxis.valueMin = round( min(values)*0.5 , 2 )
  barchart.valueAxis.valueMax = round( max(values)*1.1 , 2)
  barchart.valueAxis.valueStep = round( (barchart.valueAxis.valueMax - barchart.valueAxis.valueMin)/12 , 2 )
  barchart.bars[0].fillColor = colors.green
  
  barchart.categoryAxis.categoryNames = [ item[1] for item in data ]
  barchart.categoryAxis.labels.angle = 90
  barchart.categoryAxis.labels.dy = 60
  barchart.categoryAxis.labels.fillColor = colors.blue
  
  return barchart

def generate(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  
  piechart = Drawing(250,250)
  piechart.add(get_piechart(table_data,piechart.width,piechart.height))
  
  barchart = Drawing(500,300)
  barchart.add(get_barchart(table_data,barchart.width,barchart.height))
  
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,40)
  report.build([report_title, report_info, empty_line, piechart, barchart, empty_line, report_table])
