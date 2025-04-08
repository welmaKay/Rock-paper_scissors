
def generate_payslip(employee, output_folder="payslips"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    filename = f"{output_folder}/{employee['Name'].replace(' ', '_')}_Payslip_{employee['Month']}_{employee['Year']}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, f"Payslip for {employee['Month']} {employee['Year']}")

    c.setFont("Helvetica", 12)
    lines = [
        f"Name: {employee['Name']}",
        f"Email: {employee['Email']}",
        f"Basic Pay: ${employee['Basic Pay']:.2f}",
        f"Allowances: ${employee['Allowances']:.2f}",
        f"Deductions: ${employee['Deductions']:.2f}",
        f"Net Pay: ${employee['Basic Pay'] + employee['Allowances'] - employee['Deductions']:.2f}"
    ]

    y = height - 100
    for line in lines:
        c.drawString(50, y, line)
        y -= 25

    c.save()
    return filename

def send_email(to_email, subject, body, attachment):
    # You must set up Yagmail with your credentials before running this
    yag = yagmail.SMTP("your_email@example.com")  # Replace with your email
    yag.send(
        to=to_email,
        subject=subject,
        contents=body,
        attachments=attachment
    )
    print(f"Email sent to {to_email}")

def main():
    # Load Excel file
    df =pd.read_excel("employees.xlsx")

    for _, row in df.iterrows():
        payslip = generate_payslip(row)
        email_body = f"""
        Hi {row['Name']},

        Please find attached your payslip for {row['Month']} {row['Year']}.

        Best regards,
        HR Department
        """
        send_email(row['Email'], "Your Monthly Payslip", email_body, payslip)

if __name__ == "__main__":
    main()