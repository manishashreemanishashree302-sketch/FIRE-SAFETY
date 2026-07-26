from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_slide(c, title, body_lines):
    c.setFont("Helvetica-Bold", 24)
    c.drawString(1 * inch, 7 * inch, title)
    
    c.setFont("Helvetica", 14)
    y = 6 * inch
    for line in body_lines:
        if line.startswith("-"):
            c.drawString(1 * inch, y, line)
        else:
            c.drawString(1.2 * inch, y, line)
        y -= 0.3 * inch
    c.showPage()

def generate_pdf():
    c = canvas.Canvas("presentation.pdf", pagesize=landscape(A4))
    
    # Title Slide
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(148.5 * 2.83, 400, "Fire Safety Equipment Inspection Register")
    c.setFont("Helvetica", 18)
    c.drawCentredString(148.5 * 2.83, 350, "By: M. MANISHA SHREE")
    c.drawCentredString(148.5 * 2.83, 320, "SIH 2026 - Internal Practical Assessment")
    c.showPage()
    
    # Slide 1
    create_slide(c, "1. The Problem", [
        "- Fire safety equipment carries paper tags showing the last inspection.",
        "- Nobody maintains a central list of all equipment.",
        "- The Consequence: Expired units are often discovered during an audit, or",
        "  far worse, when one is needed during an emergency and fails."
    ])
    
    # Slide 2
    create_slide(c, "2. The Solution", [
        "- A centralized, digital register that tracks every unit's location.",
        "- Automatically calculates next due dates.",
        "- Instantly highlights which units are overdue or approaching expiry.",
        "- Simple, responsive, and easy to use on mobile devices."
    ])
    
    # Slide 3
    create_slide(c, "3. Main Screen (List & Search)", [
        "- Clean, responsive list showing critical details at a glance.",
        "- Real-time search by ID, Type, or Location.",
        "- Filter by status (Valid, Expiring Soon, Expired, Unknown).",
        "- The total record count updates instantly as filters are applied."
    ])
    
    # Slide 4
    create_slide(c, "4. Detail View & Derived Figure", [
        "- Opens instantly upon tapping a record.",
        "- Derived Figure: A large, color-coded banner showing exact days until",
        "  expiry (or days overdue) is placed at the very top.",
        "- The safety officer sees the most important number first, avoiding the",
        "  need to read through a long table."
    ])
    
    # Slide 5
    create_slide(c, "5. Calculation Logic", [
        "- 1. Parse 'next_due' string into a Date object.",
        "- 2. Fetch current local date and strip out the time of day.",
        "- 3. Calculate difference in milliseconds.",
        "- 4. Convert to days by dividing by (1000 * 60 * 60 * 24) and round up.",
        "- 5. If negative, flag equipment as 'Overdue'."
    ])
    
    # Slide 6
    create_slide(c, "6. Edge Cases & Mobile UI", [
        "- Loading State: Simulated network delay with a spinner.",
        "- Empty Search: Clear message when no results match criteria.",
        "- Awkward Cases: Missing locations show 'Unknown Loc', missing equipment",
        "  shows a prominent yellow warning banner.",
        "- Mobile First: Minimum touch targets of 44px height, stacked flexbox layout."
    ])
    
    # Slide 7
    create_slide(c, "7. Current Status & Future Improvements", [
        "- What works: Search, filter, calculations, detail view, and mobile UI.",
        "- What is unfinished / Next improvement: Data is currently static JSON.",
        "- Next step: Implement a backend or LocalStorage solution to allow adding",
        "  new records directly from the UI."
    ])
    
    c.save()

if __name__ == "__main__":
    generate_pdf()
    print("presentation.pdf generated successfully.")
