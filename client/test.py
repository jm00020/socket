import pdfkit
import time

start = time.time()
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

pdfkit.from_file('map.html', 'out.pdf', configuration=config)
# pdfkit.from_url('http://google.com', 'out.png', configuration=config)
end = time.time()

print(end-start)