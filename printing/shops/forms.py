
from .models import clients

from django.forms import ModelForm

class new_tranaction(ModelForm):

    class Meta:

        model=clients
        jls_extract_var = 'transactions'
        fields=[jls_extract_var,'amounts']
class addShopForm(ModelForm):
    
    class Meta:
        model = clients
        fields = ("shop_id","shop_name","location","phone_no","email","image","balance","transactions","amounts")
class editShopForm(ModelForm):
    
    class Meta:
        model = clients
        fields = ("shop_name","location","phone_no","email","image","balance","transactions","amounts")
class edittransactionform(ModelForm):
    class Meta:
        model = clients
        fields=("transactions","amounts")
class SearchForm(ModelForm):
    
    class Meta:
        model =clients
        fields = ("location",)

    