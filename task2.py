import csv
from fpdf import FPDF

title = "Automated Report !!!"

class PDF(FPDF):
    
    #...............................For Title............................
    def header(self):
        self.set_font('helvetica' , 'B' , 15)
        
        # to center the title
        title_w = self.get_string_width(title)
        doc_w = self.w
        self.set_x((doc_w-title_w) / 2)

        #for frame........
        self.set_draw_color(0,80,180)  
        self.set_fill_color(230,230,0)  
        self.set_text_color(220,50,50)  
        
        self.set_line_width(1)
        self.cell(title_w , 10 , title , border=1 , ln=1 , align='C' , fill=1)

        self.ln(20)            # line break....
        
        
    #...................footer.............................
    def footer(self):
        self.set_y(-15) #15mm form bottom
        self.set_font('times' , 'IU' , 10)
        self.set_text_color(169,169,0)
        self.cell(0, 10 , f"page : {self.page_no()} of {{nb}}" ,  align='C')
   
   
#.............................................Main code..................................
data = 'data.csv'
input_file = "data.csv"  # here you can add name of file which is in same folder or simply you can add path of the data file....


with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
        
#...........................Let's create file..............................

pdf = PDF()
pdf.add_page()


#.....................................Content..........................
pdf.set_font("Arial", size=12)
pdf.cell(0 , 10 , "Hello user (*_*)" , ln=1)

for row in data:
    pdf.cell(0, 10, ', '.join(row), ln=True)
    
    
#................................Save PDF......................................
pdf.output('task_2.pdf')

output_file = "task_2.pdf"

print(f"Report generated: {output_file}")   # for complation of the task
