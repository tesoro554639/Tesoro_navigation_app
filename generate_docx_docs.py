import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_docx(output_path):
    doc = docx.Document()

    # Set 0.5 inch margins
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(0.5)
        s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.5)
        s.right_margin = Inches(0.5)

    primary_hex = "1A237E"  # Indigo
    accent_hex = "303F9F"

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("LABORATORY ACTIVITY DOCUMENTATION\nStatefulWidget & Bottom Navigation Bar Application")
    r_title.bold = True
    r_title.font.size = Pt(18)
    r_title.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    # Metadata Table
    table_meta = doc.add_table(rows=3, cols=2)
    table_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_rows = [
        ("Student Name: Luis James Tesoro", "Student ID: 554639"),
        ("Course & Section: BSIT — 2nd Year - 4745 (CCE106L)", "Date: November 12, 2026"),
        ("Project Folder: Tesoro_navigation_app", "GitHub: https://github.com/tesoro554639/Tesoro_navigation_app")
    ]
    for row_idx, (c0, c1) in enumerate(meta_rows):
        row = table_meta.rows[row_idx]
        row.cells[0].text = c0
        row.cells[1].text = c1
        set_cell_background(row.cells[0], "E8EAF6")
        set_cell_background(row.cells[1], "E8EAF6")
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(9.5)

    doc.add_paragraph() # Spacer

    # Section 1
    h1 = doc.add_paragraph()
    r = h1.add_run("1. Learning Objectives & Project Overview")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    p1 = doc.add_paragraph(
        "This project implements a multi-screen Flutter application structured with a Material 3 NavigationBar and persistent state handling. "
        "It showcases how StatefulWidget and setState() manage active views, in-memory demo authentication, and modular architecture across isolated Dart source files.\n\n"
        "Core Competencies Implemented:\n"
        "• Bottom Navigation Shell: Designed a homepage with a responsive NavigationBar having four destinations (Home, Calculator, Profile, Social Media).\n"
        "• Reactive Tab Switching: Dynamic destination selection controlled via setState() updates.\n"
        "• State Preservation: Utilization of IndexedStack to retain input data, calculations, and scroll states across tab navigations.\n"
        "• Component Integration: Seamless inclusion of the Laboratory Activity 4 Calculator widget without regression.\n"
        "• Modular Code Organization: Strict separation of concerns across 9 dedicated Dart files in the lib/ directory."
    )
    p1.paragraph_format.space_after = Pt(8)

    # Section 2: Module Breakdown
    h2 = doc.add_paragraph()
    r = h2.add_run("2. Module Architecture & Source File Breakdown")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    modules = [
        ("main.dart", "StatelessWidget", "App entry point; configures MaterialApp, Material 3 theming (Indigo seed), and sets LoginScreen as initial home route."),
        ("demo_auth.dart", "Static Class", "In-memory authentication service. Verifies credentials against default admin account (admin / admin123) or in-memory registered user."),
        ("login_screen.dart", "StatefulWidget", "Login form with obscure text toggle, field validation, SnackBar feedback, and navigation replacement to MainScreen."),
        ("register_screen.dart", "StatefulWidget", "Registration form enforcing username rules (min 3 chars, admin reserved), password constraints (min 6 chars), and confirmation match."),
        ("main_screen.dart", "StatefulWidget", "Core container managing the NavigationBar with four destinations and IndexedStack to preserve each tab's state."),
        ("home_page.dart", "StatelessWidget", "Welcome overview dashboard presenting application highlights and directory cards describing the available tabs."),
        ("calculator_screen.dart", "StatefulWidget", "Calculator widget from Lab 4 supporting +, −, ×, ÷ with division-by-zero checks, numerical parsing validation, and clear reset button."),
        ("profile_page.dart", "StatelessWidget", "Student profile displaying Avatar, Luis James Tesoro, Student ID (554639), Section (4745), and official institutional email."),
        ("social_media_page.dart", "StatelessWidget", "Social media directory with interactive handles (Facebook, Instagram, YouTube) triggering SnackBar notifications on tap.")
    ]

    table_mod = doc.add_table(rows=len(modules) + 1, cols=3)
    table_mod.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["File Name", "Component Type", "Description & Responsibilities"]
    hdr_cells = table_mod.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        set_cell_background(hdr_cells[i], primary_hex)
        p = hdr_cells[i].paragraphs[0]
        for r in p.runs:
            r.bold = True
            r.font.size = Pt(9)
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for idx, (f, c, d) in enumerate(modules):
        cells = table_mod.rows[idx + 1].cells
        cells[0].text = f
        cells[1].text = c
        cells[2].text = d
        bg = "FFFFFF" if idx % 2 == 0 else "F8F9FA"
        for cell in cells:
            set_cell_background(cell, bg)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            for r in p.runs:
                r.font.size = Pt(8.5)

    doc.add_page_break()

    # Section 3
    h3 = doc.add_paragraph()
    r = h3.add_run("3. Technical Analysis: State Preservation with IndexedStack")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    doc.add_paragraph(
        "A cornerstone requirement of this laboratory is preserving tab state while switching destinations. "
        "In standard naive implementations where the active view is swapped conditionally (e.g., body: pages[selectedIndex]), "
        "Flutter completely unmounts and disposes the outgoing widget state. This causes user text inputs in the calculator to reset, "
        "operation results to clear, and scroll positions to be lost whenever the user navigates away.\n\n"
        "To achieve seamless persistence, MainScreen implements IndexedStack:\n"
        "IndexedStack(index: selectedIndex, children: pages)\n\n"
        "Mechanism: IndexedStack maintains all destination widgets simultaneously in the Element and Render trees while visually stacking and displaying only the destination corresponding to selectedIndex. The remaining pages stay alive in memory, preserving their TextEditingController values, calculated state, and scroll offsets without requiring complex external state management solutions."
    )

    # Section 4: Screenshots
    h4 = doc.add_paragraph()
    r = h4.add_run("4. Four Primary Destinations: Screenshot Verification")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    t_shots = doc.add_table(rows=2, cols=2)
    t_shots.alignment = WD_TABLE_ALIGNMENT.CENTER
    shot_items = [
        ("screenshots/01_home_page.png", "Figure 1: Home Page (Overview Dashboard)"),
        ("screenshots/02_calculator_page.png", "Figure 2: Calculator Page (Active Calculation State)"),
        ("screenshots/03_profile_page.png", "Figure 3: Profile Page (Luis James Tesoro - 554639)"),
        ("screenshots/04_social_media_page.png", "Figure 4: Social Media Page (Connected Accounts)")
    ]

    for i, (path, cap) in enumerate(shot_items):
        row = i // 2
        col = i % 2
        cell = t_shots.rows[row].cells[col]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(path, width=Inches(1.8))
        p_cap = cell.add_paragraph(cap)
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        for r in p_cap.runs:
            r.bold = True
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    doc.add_page_break()

    # Section 5: Auth Screenshots
    h5 = doc.add_paragraph()
    r = h5.add_run("5. Authentication Flow & System Verification")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    t_auth = doc.add_table(rows=1, cols=2)
    t_auth.alignment = WD_TABLE_ALIGNMENT.CENTER
    auth_items = [
        ("screenshots/00_login_screen.png", "Figure 5: Login Screen"),
        ("screenshots/00_register_screen.png", "Figure 6: Register Screen")
    ]
    for i, (path, cap) in enumerate(auth_items):
        cell = t_auth.rows[0].cells[i]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(path, width=Inches(2.0))
        p_cap = cell.add_paragraph(cap)
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        for r in p_cap.runs:
            r.bold = True
            r.font.size = Pt(8.5)
            r.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    # Section 6: Submission Summary
    h6 = doc.add_paragraph()
    r = h6.add_run("6. Verification & Submission Summary")
    r.bold = True
    r.font.size = Pt(13)
    r.font.color.rgb = RGBColor(0x1A, 0x23, 0x7E)

    doc.add_paragraph(
        "• Flutter Code Analysis: flutter analyze passed cleanly with 0 issues.\n"
        "• Automated Tests: flutter test passed all smoke tests and UI visual verifications.\n"
        "• Bottom Navigation: All 4 destinations smoothly switchable using setState().\n"
        "• State Persistence: Calculator values and calculations preserved across tab switches via IndexedStack.\n"
        "• GitHub Repository: https://github.com/tesoro554639/Tesoro_navigation_app"
    )

    doc.save(output_path)
    print(f"DOCX created successfully at: {output_path}")

if __name__ == "__main__":
    create_docx("Tesoro_Navigation_App_Documentation.docx")
