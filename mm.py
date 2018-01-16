from __future__ import print_function
from mailmerge import MailMerge
from datetime import date

template = "123.docx"
document = MailMerge(template)
print(document.get_merge_fields())
di={"Name":"Sherni"}
document.merge(
    status='Gold',
    city='Springfield',
    phone_number='800-575666666666666666666666666666666666666666666655-5555',
    Business='ANKIttttttttttTs',
    zip='55555',
    purchases='$500,000',
    shipping_limit='$500',
    state='MO',
    address='1234 Main Street',
    date='{:%d-%b-%Y}'.format(date.today()),
    discount='5%',
    recipient=di["Name"])

document.write('test-output2.docx')