from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(data):
    filename = "reports/security_report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "CyberMegaTool - Security Report")
    
    y = 700
    for entry in data:
        c.drawString(100, y, entry)
        y -= 20

    c.save()
    print(f"✅ Report saved as {filename}")
