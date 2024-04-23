def update_header(invmain_guid):

    from _ts_tta_invchild.models import TtaInvchild
    from _ts_tta_invmain.models import TtaInvmain
    from django.db.models import Sum

    # print(invmain_guid)
    # print('==============')

    sum_amount = TtaInvchild.objects.filter(invmain_guid = invmain_guid).aggregate(
        totalprice = Sum('totalprice'),
        total_incl_tax = Sum('total_incl_tax') 
        )
    
    # print(sum_amount)
    trans_main = TtaInvmain.objects.filter(invmain_guid = invmain_guid).first()
    # print(asd)
    # print('func')
    trans_main.total = sum_amount['totalprice'] 
    trans_main.total_incl_tax = sum_amount['total_incl_tax']  
    trans_main.save()