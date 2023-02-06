from fpdf import FPDF
from datetime import date

def createPdf(org_name,name,parents_name ,age,desig_name,start_date,end_date,location,emp_name):
    my_pdf = FPDF()
    my_pdf.add_page()
    my_pdf.set_font("Arial")
    age = str(age)
    my_pdf.set_font_size(14)
    my_pdf.cell(200, 18, txt = "DRAFT OF EMPLOYEE-SERVICE-AGREEMENT",ln = 1, align = 'C')
    my_pdf.set_font_size(10)
    my_pdf.cell(200, 18, txt = "THIS EMPLOYEE SERVICE AGREEMENT executed at Anubandh.com on "+str(date.today()),ln = 2, align = 'L')
    my_pdf.cell(200, 18, txt = "BETWEEN"+org_name+", a company incorporated under the Companies Act, 1956 or Companies Act, " ,ln = 3, align = 'L')
    my_pdf.cell(200, 18, txt = "represented by Mr./Ms. "+emp_name+", having it's registered office at "+location+", hereinafter referred" ,ln = 4, align = 'L') 
    my_pdf.cell(200, 18, txt = "to as the EMPLOYER (which expression shall, unless it is repugnant to the context, mean and include it's successors-in-interests, administrators and permitted assigns);" ,ln = 5, align = 'L')
    my_pdf.cell(200, 18, txt = "AND Mr. /Ms. "+name+", son of / wife of/ daughter of Mr. "+parents_name+", Indian national , aged about "+age+"years, hereinafter referred to as the EMPLOYEE.WHEREAS" ,ln = 6, align = 'L')

    my_pdf.cell(200, 18, txt = "The EMPLOYER is carrying on the business of"+org_name,ln = 7, align = 'L')
    my_pdf.cell(200, 18, txt = "The EMPLOYER called for applications from the eligible candidates for the post"+desig_name+"and in ",ln = 8, align = 'L')
    my_pdf.cell(200, 18, txt = "response thereto an application-dated "+str(date.today())+" was forwarded by the EMPLOYEE to the ",ln = 9, align = 'L')
    my_pdf.cell(200, 18, txt = "EMPLOYER.",ln = 10, align = 'C')
    my_pdf.cell(200, 18, txt = "On processing the application and the relevant documents, the EMPLOYER found the EMPLOYEE ",ln = 11, align = 'L')
    my_pdf.cell(200, 18, txt = "adequately qualified for the post and offered to appoint him as "+desig_name+" in the ",ln = 12, align = 'L')
    my_pdf.cell(200, 18, txt = "Company.",ln = 13, align = 'L')
    my_pdf.cell(200, 18, txt = "The EMPLOYEE has accepted the said appointment on the terms and conditions herein after set out.",ln = 14, align = 'L')

    my_pdf.cell(200, 18, txt = "NOW THEREFORE IN CONSIDERATION OF THE MUTUAL OBLIGATIONS AND UNDER TAKINGS ",ln = 15, align = 'L')
    my_pdf.cell(200, 18, txt = "CONTAINED HEREIN THIS AGREEMENT WITNESSETH AS FOLLOWS",ln = 16, align = 'L')
    my_pdf.cell(200, 18, txt = "NAME OF THE POST:"+desig_name,ln = 17, align = 'L')
    my_pdf.cell(200, 18, txt = "The said EMPLOYEE is hereby appointed as "+desig_name,ln = 18, align = 'L')
    my_pdf.cell(200, 18, txt = "PROBATION AND CONFIRMATION:",ln = 19, align = 'L')
    my_pdf.cell(200, 18, txt = "The EMPLOYEE shall be on probation for a period of 1 month. The decision of the management on ",ln = 20, align = 'L')
    my_pdf.cell(200, 18, txt = "the performance of the EMPLOYEE during the period of probation is final and binding on the ",ln = 21, align = 'L')
    my_pdf.cell(200, 18, txt = "DURATION OF EMPLOYMENT:"+start_date+" to "+end_date,ln = 22, align = 'L')
    my_pdf.cell(200, 18, txt = "On successful completion of probation, the EMPLOYEE shall be appointed as a permanent ",ln = 23, align = 'L')
    my_pdf.cell(200, 18, txt = "EMPLOYEE of the EMPLOYER for a period of "+start_date+" to "+end_date,ln = 24, align = 'L')
    my_pdf.cell(200, 18, txt = "PLACE OF POSTING: "+location,ln = 25, align = 'L')
    my_pdf.cell(200, 18, txt = "HOURS OF WORK: 9 hours",ln = 27, align = 'L')
    my_pdf.cell(200, 18, txt = "The EMPLOYEE is required to work from 9Am to 6Pm during the Weekdays. The weekly holiday would be on Sunday.",ln = 28, align = 'L')
    my_pdf.cell(200, 18, txt = "ARBITRATION:",ln = 29, align = 'L')
    my_pdf.cell(200, 18, txt = "Any dispute arising under this Agreement or any matter incidental thereto, shall be submitted for ",ln = 30, align = 'L')
    my_pdf.cell(200, 18, txt = "arbitration as per the provisions of Arbitration and Conciliation Act, 1996. The arbitration shall be held ",ln = 31, align = 'L')
    my_pdf.cell(200, 18, txt = "at "+location+".",ln = 32, align = 'L')

    my_pdf.cell(200, 18, txt = "The parties hereto have signed on the day and year first hereinabove written",ln = 33, align = 'L')
    my_pdf.cell(200, 18, txt = "EMPLOYER (sign/ authentication)				EMPLOYEE (sign/ authentication)",ln = 45, align = 'L')

    my_pdf.output("my_pdf.pdf")
    return True