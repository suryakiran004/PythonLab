
import os
import subprocess
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Python Lab Record', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def get_program_output(filename, inputs=None):
    try:
        input_str = '\n'.join(inputs) + '\n' if inputs else ''
        result = subprocess.run(
            ['python', filename],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

programs = [
    {
        'file': 'count4letterword.py',
        'inputs': [],
        'note': 'Reads from woordd.txt'
    },
    {
        'file': 'dictionary.py',
        'inputs': ['hello world']
    },
    {
        'file': 'digitsum.py',
        'inputs': ['1234']
    },
    {
        'file': 'fact.py',
        'inputs': ['5']
    },
    {
        'file': 'fileop.py',
        'inputs': [],
        'note': 'Reads number.txt, Writes fileout.txt'
    },
    {
        'file': 'higherorder.py',
        'inputs': []
    },
    {
        'file': 'listcomprihention.py',
        'inputs': []
    },
    {
        'file': 'listdunct.py',
        'inputs': []
    },
    {
        'file': 'manualbubble.py',
        'inputs': ['5', '5', '1', '4', '2', '8']
    },
]

pdf = PDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)

for prog in programs:
    filename = prog['file']
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found.")
        continue

    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, f"Program: {filename}", 0, 1, 'L')
    pdf.ln(5)
    
    # Source Code
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Source Code:", 0, 1, 'L')
    pdf.set_font('Courier', '', 10)
    
    try:
        with open(filename, 'r') as f:
            code_content = f.read()
            # Handle latin-1 encoding issues if any by replacing
            code_content = code_content.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 5, code_content)
    except Exception as e:
        pdf.multi_cell(0, 5, f"Error reading file: {e}")
        
    pdf.ln(5)

    # Input (if any)
    if prog['inputs']:
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, "Sample Input:", 0, 1, 'L')
        pdf.set_font('Courier', '', 10)
        pdf.multi_cell(0, 5, '\n'.join(prog['inputs']))
        pdf.ln(5)
    
    # Output
    output = get_program_output(filename, prog['inputs'])
    
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, "Sample Output:", 0, 1, 'L')
    pdf.set_font('Courier', '', 10)
    # Handle latin-1 for output as well
    output = output.encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 5, output)

    if 'note' in prog:
        pdf.ln(5)
        pdf.set_font('Arial', 'I', 10)
        pdf.cell(0, 10, f"Note: {prog['note']}", 0, 1, 'L')

try:
    pdf.output('LabRecord.pdf', 'F')
    print("PDF generated successfully: LabRecord.pdf")
except Exception as e:
    print(f"Error generating PDF: {e}")
