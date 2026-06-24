# PDF/XLSX export
from reportlab.pdfgen import canvas


def export_pdf(
        filename,
        text
):

    c = canvas.Canvas(
        filename
    )

    c.drawString(
        100,
        800,
        text
    )

    c.save()