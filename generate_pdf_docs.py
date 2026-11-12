import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

def create_pdf(output_pdf_path):
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()

    # Custom color palette
    primary_color = colors.HexColor("#1A237E")  # Dark Indigo
    accent_color = colors.HexColor("#303F9F")   # Medium Indigo
    text_dark = colors.HexColor("#212121")       # Charcoal

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        alignment=TA_CENTER,
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=accent_color,
        alignment=TA_CENTER,
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=primary_color,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True,
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=text_dark,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
    )

    caption_style = ParagraphStyle(
        'Caption',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=primary_color,
        alignment=TA_CENTER,
        spaceBefore=3,
        spaceAfter=6,
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white,
        alignment=TA_LEFT,
    )

    table_body_style = ParagraphStyle(
        'TableBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=text_dark,
        alignment=TA_LEFT,
    )

    code_body_style = ParagraphStyle(
        'CodeBody',
        parent=styles['Normal'],
        fontName='Courier-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#0D47A1"),
    )

    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#757575"),
        alignment=TA_CENTER,
    )

    story = []

    # ==================== PAGE 1 ====================
    # Title & Header
    story.append(Paragraph("LABORATORY ACTIVITY DOCUMENTATION", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("StatefulWidget & Bottom Navigation Bar Application", subtitle_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=2, color=primary_color, spaceBefore=2, spaceAfter=8))

    # Metadata Table
    meta_data = [
        [
            Paragraph("<b>Student Name:</b> Luis James Tesoro", table_body_style),
            Paragraph("<b>Student ID:</b> 554639", table_body_style),
        ],
        [
            Paragraph("<b>Course & Section:</b> BSIT — 2nd Year - 4745 (CCE106L)", table_body_style),
            Paragraph("<b>Date:</b> November 12, 2026", table_body_style),
        ],
        [
            Paragraph("<b>Project Folder:</b> Tesoro_navigation_app", table_body_style),
            Paragraph("<b>GitHub Repo:</b> <font color='#1A237E'><u>https://github.com/tesoro554639/Tesoro_navigation_app</u></font>", table_body_style),
        ]
    ]
    t_meta = Table(meta_data, colWidths=[270, 270])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#E8EAF6")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#9FA8DA")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    # 1. Objectives & Overview
    story.append(Paragraph("1. Learning Objectives & Project Overview", h1_style))
    story.append(Paragraph(
        "This project implements a multi-screen Flutter application structured with a Material 3 <b>NavigationBar</b> and persistent state handling. It showcases how <code>StatefulWidget</code> and <code>setState()</code> manage active views, in-memory demo authentication, and modular architecture across isolated Dart source files.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Core Competencies Implemented:</b><br/>"
        "• <b>Bottom Navigation Shell:</b> Designed a homepage with a responsive <code>NavigationBar</code> having four destinations (Home, Calculator, Profile, Social Media).<br/>"
        "• <b>Reactive Tab Switching:</b> Dynamic destination selection controlled via <code>setState()</code> updates.<br/>"
        "• <b>State Preservation:</b> Utilization of <code>IndexedStack</code> to retain input data, calculations, and scroll states across tab navigations.<br/>"
        "• <b>Component Integration:</b> Seamless inclusion of the Laboratory Activity 4 Calculator widget without regression.<br/>"
        "• <b>Modular Code Organization:</b> Strict separation of concerns across 9 dedicated Dart files in the <code>lib/</code> directory.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # 2. Module Breakdown Table
    story.append(Paragraph("2. Module Architecture & Source File Breakdown", h1_style))
    module_table_data = [
        [Paragraph("File Name", table_header_style), Paragraph("Component Type", table_header_style), Paragraph("Module Role & Technical Description", table_header_style)],
        [
            Paragraph("<b>main.dart</b>", code_body_style),
            Paragraph("StatelessWidget", table_body_style),
            Paragraph("App entry point; configures <code>MaterialApp</code>, Material 3 theming (Indigo seed), and sets <code>LoginScreen</code> as initial home route.", table_body_style)
        ],
        [
            Paragraph("<b>demo_auth.dart</b>", code_body_style),
            Paragraph("Static Class", table_body_style),
            Paragraph("In-memory authentication service. Verifies credentials against default admin account (<code>admin</code> / <code>admin123</code>) or in-memory registered user.", table_body_style)
        ],
        [
            Paragraph("<b>login_screen.dart</b>", code_body_style),
            Paragraph("StatefulWidget", table_body_style),
            Paragraph("Login form with obscure text toggle, field validation, SnackBar feedback, and navigation replacement to <code>MainScreen</code>.", table_body_style)
        ],
        [
            Paragraph("<b>register_screen.dart</b>", code_body_style),
            Paragraph("StatefulWidget", table_body_style),
            Paragraph("Registration form enforcing username rules (min 3 chars, admin reserved), password constraints (min 6 chars), and confirmation match.", table_body_style)
        ],
        [
            Paragraph("<b>main_screen.dart</b>", code_body_style),
            Paragraph("StatefulWidget", table_body_style),
            Paragraph("Core container managing the <code>NavigationBar</code> with four destinations and <code>IndexedStack</code> to preserve each tab's state.", table_body_style)
        ],
        [
            Paragraph("<b>home_page.dart</b>", code_body_style),
            Paragraph("StatelessWidget", table_body_style),
            Paragraph("Welcome overview dashboard presenting application highlights and directory cards describing the available tabs.", table_body_style)
        ],
        [
            Paragraph("<b>calculator_screen.dart</b>", code_body_style),
            Paragraph("StatefulWidget", table_body_style),
            Paragraph("Calculator widget from Lab 4 supporting +, −, ×, ÷ with division-by-zero checks, numerical parsing validation, and clear reset button.", table_body_style)
        ],
        [
            Paragraph("<b>profile_page.dart</b>", code_body_style),
            Paragraph("StatelessWidget", table_body_style),
            Paragraph("Student profile displaying Avatar, Luis James Tesoro, Student ID (554639), Section (4745), and official institutional email.", table_body_style)
        ],
        [
            Paragraph("<b>social_media_page.dart</b>", code_body_style),
            Paragraph("StatelessWidget", table_body_style),
            Paragraph("Social media directory with interactive handles (Facebook, Instagram, YouTube) triggering SnackBar notifications on tap.", table_body_style)
        ],
    ]

    t_modules = Table(module_table_data, colWidths=[115, 85, 340])
    t_modules.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#B0BEC5")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CFD8DC")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#F8F9FA")]),
    ]))
    story.append(t_modules)

    # ==================== PAGE 2 ====================
    story.append(PageBreak())
    story.append(Paragraph("3. Technical Analysis: State Preservation with IndexedStack", h1_style))
    story.append(Paragraph(
        "A cornerstone requirement of this laboratory is <b>preserving tab state while switching destinations</b>. In standard naive implementations where the active view is swapped conditionally (e.g., <code>body: pages[selectedIndex]</code>), Flutter completely unmounts and disposes the outgoing widget state. This causes user text inputs in the calculator to reset, operation results to clear, and scroll positions to be lost whenever the user navigates away.",
        body_style
    ))
    story.append(Paragraph(
        "To achieve seamless persistence, <code>MainScreen</code> implements <code>IndexedStack</code>:<br/>"
        "<code>IndexedStack(index: selectedIndex, children: pages)</code><br/>"
        "<b>Mechanism:</b> <code>IndexedStack</code> maintains all destination widgets simultaneously in the Element and Render trees while visually stacking and displaying only the destination corresponding to <code>selectedIndex</code>. The remaining pages stay alive in memory, preserving their <code>TextEditingController</code> values, calculated state, and scroll offsets without requiring complex external state management solutions.",
        body_style
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph("4. Four Primary Destinations: Screenshot Verification", h1_style))
    story.append(Paragraph(
        "Below are screenshots of all four navigation destinations captured from the live application:",
        body_style
    ))
    story.append(Spacer(1, 4))

    img_dir = "screenshots"
    w, h = 105, 210

    img_home = Image(os.path.join(img_dir, "01_home_page.png"), width=w, height=h)
    img_calc = Image(os.path.join(img_dir, "02_calculator_page.png"), width=w, height=h)
    img_prof = Image(os.path.join(img_dir, "03_profile_page.png"), width=w, height=h)
    img_soc = Image(os.path.join(img_dir, "04_social_media_page.png"), width=w, height=h)

    # 4 images arranged in a 2x2 grid
    grid_data = [
        [img_home, img_calc],
        [
            Paragraph("<b>Figure 1: Home Page</b><br/>(Welcome dashboard & overview)", caption_style),
            Paragraph("<b>Figure 2: Calculator Page</b><br/>(Arithmetic operations & state retention)", caption_style)
        ],
        [img_prof, img_soc],
        [
            Paragraph("<b>Figure 3: Profile Page</b><br/>(Student information & credentials)", caption_style),
            Paragraph("<b>Figure 4: Social Media Page</b><br/>(Sample accounts with SnackBar alerts)", caption_style)
        ]
    ]
    t_grid = Table(grid_data, colWidths=[270, 270])
    t_grid.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_grid)

    # ==================== PAGE 3 ====================
    story.append(PageBreak())
    story.append(Paragraph("5. Authentication Flow & Additional Screens", h1_style))
    story.append(Paragraph(
        "The application includes an in-memory authentication gateway verifying users prior to accessing the main dashboard. Tested with both default admin credentials (<code>admin</code> / <code>admin123</code>) and newly registered student accounts.",
        body_style
    ))
    story.append(Spacer(1, 4))

    img_login = Image(os.path.join(img_dir, "00_login_screen.png"), width=w, height=h)
    img_reg = Image(os.path.join(img_dir, "00_register_screen.png"), width=w, height=h)

    auth_grid = [
        [img_login, img_reg],
        [
            Paragraph("<b>Figure 5: Login Screen</b><br/>(Credential authentication & password visibility toggle)", caption_style),
            Paragraph("<b>Figure 6: Register Screen</b><br/>(New account creation with constraint validation)", caption_style)
        ]
    ]
    t_auth = Table(auth_grid, colWidths=[270, 270])
    t_auth.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t_auth)
    story.append(Spacer(1, 10))

    story.append(Paragraph("6. Verification & Submission Summary", h1_style))
    story.append(Paragraph(
        "• <b>Flutter Code Analysis:</b> <code>flutter analyze</code> passed cleanly with 0 issues.<br/>"
        "• <b>Automated Tests:</b> <code>flutter test</code> passed all smoke tests and UI golden visual verifications.<br/>"
        "• <b>Bottom Navigation:</b> All 4 destinations smoothly switchable using <code>setState()</code>.<br/>"
        "• <b>State Persistence:</b> Calculator values and calculations preserved across tab switches via <code>IndexedStack</code>.<br/>"
        "• <b>GitHub Repository:</b> <font color='#1A237E'><b>https://github.com/tesoro554639/Tesoro_navigation_app</b></font>",
        body_style
    ))
    story.append(Spacer(1, 16))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#B0BEC5"), spaceBefore=4, spaceAfter=8))
    story.append(Paragraph("University of Mindanao • CCE106L Mobile Programming • Luis James Tesoro (554639)", footer_style))

    doc.build(story)
    print(f"Refined PDF generated: {output_pdf_path}")

if __name__ == "__main__":
    create_pdf("Tesoro_Navigation_App_Documentation.pdf")
