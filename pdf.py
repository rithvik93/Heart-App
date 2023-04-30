import streamlit as st
from fpdf import FPDF

def create_pdf(inputs):
    pdf = FPDF()
    pdf.add_page()

    # Add image as background
    pdf.image('back1.jpg', x=0, y=0, w=pdf.w, h=pdf.h)
    # font and color
    pdf.set_font("Arial","BUI", 23)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 10, 'Heart Disease Prediction', 1, 1, 'C' )
    # Set the background color and text color for the table
    pdf.set_font("Arial", "B", 12)
    
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(0, 0, 0)
    
    for key, value in inputs.items():
        if key!="Result":
            pdf.cell(50, 10, key, 1, 0, "L", True)
            pdf.cell(0, 10, str(value), 1, 1, "L", True)
        else:
            pdf.cell(50, 10, key, 1, 0, "L", True)
            if "having" in value:
                pdf.set_fill_color(255, 0, 0)  # RGB value for red
                pdf.cell(0, 10, str(value), 1, 1, "L", True)
            else:
                pdf.set_fill_color(0,255, 0)  # RGB value for green
                pdf.cell(0, 10, str(value), 1, 1, "L",True)
    return pdf



# Define your Streamlit app
def main(inputs):
    # Get user inputs

    # Add a button to generate the PDF
    
        # Create the PDF document
        pdf = create_pdf(inputs)

        # Download the PDF document
        st.download_button(
            label="Download PDF",
            data=pdf.output(dest="S").encode("latin1"),
            file_name="Report.pdf",
            mime="application/pdf",
        )
