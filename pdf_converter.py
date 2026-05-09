from fpdf import FPDF
import os

class SpaceXReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'SpaceX Flight Analysis Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf_report():
    pdf = SpaceXReport()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Section 1
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "1. Introduction", 0, 1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "This report presents an analysis of rocket landing success factors based on a simulation model of Falcon 9 flight data.")
    pdf.ln(5)

    # Section 2
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "2. Methodology", 0, 1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "A synthetic dataset of 100 flights was generated to study variables including Payload Mass, Orbit Type, and Landing Outcomes.")
    pdf.ln(5)

    # Section 3
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "3. Visual Analysis", 0, 1)
    
    # Image 1
    if os.path.exists('figures/orbit_success_rate.png'):
        pdf.image('figures/orbit_success_rate.png', x=10, w=180)
        pdf.ln(5)
        pdf.cell(0, 10, "Figure 1: Landing success distribution across different orbits.", 0, 1, 'C')

    pdf.add_page()
    
    # Image 2
    if os.path.exists('figures/payload_vs_outcome.png'):
        pdf.image('figures/payload_vs_outcome.png', x=10, w=180)
        pdf.ln(5)
        pdf.cell(0, 10, "Figure 2: Statistical distribution of payload mass.", 0, 1, 'C')

    # Section 4
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "4. Conclusion", 0, 1)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "Initial analysis indicates that orbit type is a significant factor in landing success, while payload mass requires further predictive modeling.")

    output_path = 'outputs/SpaceX_Analysis_Report.pdf'
    pdf.output(output_path)
    print(f"PDF report generated successfully at: {output_path}")

if __name__ == "__main__":
    create_pdf_report()