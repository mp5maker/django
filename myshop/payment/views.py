from django.shortcuts import render

from django.template.loader import render_to_string

from django.core.mail import EmailMessage

from django.conf import settings

import weasyprint

from io import BytesIO

def payment_process(request):
    if request.method == 'POST':
        if result.is_success:
            order.save()
            subject = 'My Shop - Invoice no. {}'.format(order.id)
            message = 'Please, find attached the invoice for your recent purchase.'
            email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
            html = render_to_string('orders/order/pdf.html', {'order': order})
            out = BytesIO()
            stylesheets = None
            # stylesheets=[weastprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
            weasyprint.HTML[string=html].write_pdf(out, stylesheets)
            email.attach('order_{}.pdf'.format(order.id), out.getvalue(), 'application/pdf')
            email.send()
            return redirect('payment:done')
        else:
            return redirect('payment:cancelled')