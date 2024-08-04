from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from datetime import datetime

# Define the receipt data
receipt_data = {
    'receipt_number': '031',
    'Transaction ID': "TDI456",
    'date': datetime.now().strftime('%Y-%m-%d'),
    'customer_name': 'Diya Fransis',
    'items': [
        {'name': 'Item 1', 'quantity': 2, 'price': 17.99},
        {'name': 'Item 2', 'quantity': 1, 'price': 5},
        {'name': 'Item 3', 'quantity': 3, 'price': 7.99},
    ],
    'subtotal': 0,
    'tax': 0,
    'total': 0,
    "Payment Method": "Credit Card"
}

# Calculate the subtotal, tax, and total
for item in receipt_data['items']:
    receipt_data['subtotal'] += item['quantity'] * item['price']
receipt_data['tax'] = receipt_data['subtotal'] * 0.08
receipt_data['total'] = receipt_data['subtotal'] + receipt_data['tax']

# Create the PDF
c = canvas.Canvas('receipt.pdf', pagesize=letter)

# Set the font and font size
c.setFont('Helvetica', 12)

# Draw the receipt header
c.drawString(1 * inch, 10 * inch,'Receipt            : {}'.format(receipt_data['receipt_number']))
c.drawString(1 * inch, 9.5 * inch,'Transaction ID    : {}'.format(receipt_data['Transaction ID']))
c.drawString(1 * inch, 9 * inch,'Date                : {}'.format(receipt_data['date']))

# Draw the customer information
c.drawString(1 * inch, 8.5 * inch,'Customer Name     : {}'.format(receipt_data['customer_name']))
c.drawString(1 * inch, 8 * inch,'Transcation method  : {}'.format(receipt_data['Payment Method']))

# Draw the items
y = 7.5 * inch
for item in receipt_data['items']:
    c.drawString(1 * inch, y, '{} x {} = ${:.2f}'.format(item['name'], item['quantity'], item['quantity'] * item['price']))
    y -= 0.2 * inch

# Draw the subtotal, tax, and total
c.drawString(1 * inch, 6.5 * inch, 'Subtotal: ${:.2f}'.format(receipt_data['subtotal']))
c.drawString(1 * inch, 6 * inch, 'Tax (8%): ${:.2f}'.format(receipt_data['tax']))
c.drawString(1 * inch, 5.5 * inch, 'Total: ${:.2f}'.format(receipt_data['total']))

c.save()