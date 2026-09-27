import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header line
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(40, A4[1] - 35, A4[0] - 40, A4[1] - 35)
        self.drawString(40, A4[1] - 30, "PT TALAHOME JEPARA INDONESIA — SISTEM MANAJEMEN MUTU & SOP EKSPOR")
        
        # Footer line
        self.line(40, 45, A4[0] - 40, 45)
        self.drawString(40, 32, "Dokumen Rahasia Internal — Standar Operasional Prosedur 2026")
        page_str = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(A4[0] - 40, 32, page_str)
        self.restoreState()

def create_sop(filename, title, doc_no, rev, date, dept, sections):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=50,
        bottomMargin=55
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=6
    )
    
    sec_style = ParagraphStyle(
        'DocSec',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=10,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=5
    )
    
    bullet_style = ParagraphStyle(
        'DocBullet',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )

    story = []
    
    # Metadata Box Table
    meta_data = [
        [Paragraph(f"<b>DOKUMEN SOP RESMI</b><br/><font size=8 color='#64748b'>PT TALAHOME JEPARA</font>", body_style),
         Paragraph(f"<b>No:</b> {doc_no}<br/><b>Revisi:</b> {rev}", body_style),
         Paragraph(f"<b>Tanggal:</b> {date}<br/><b>Dept:</b> {dept}", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[200, 150, 165])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94a3b8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 12))
    
    # Title
    story.append(Paragraph(title, title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#2563eb'), spaceBefore=2, spaceAfter=10))
    
    for sec_title, paragraphs in sections:
        story.append(Paragraph(sec_title, sec_style))
        for p in paragraphs:
            if p.startswith("- ") or p.startswith("* "):
                clean_p = "&bull; " + p[2:]
                story.append(Paragraph(clean_p, bullet_style))
            elif isinstance(p, list): # It's a table
                t = Table(p[1], colWidths=p[0])
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#0f172a')),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,-1), 8.5),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                    ('TOPPADDING', (0,0), (-1,-1), 4),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#94a3b8')),
                ]))
                story.append(t)
                story.append(Spacer(1, 6))
            else:
                story.append(Paragraph(p, body_style))
        story.append(Spacer(1, 6))
        
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[OK] Generated: {filename}")
