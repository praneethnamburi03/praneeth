from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import clients
import json
from django.contrib import messages
from .forms import new_tranaction,addShopForm,editShopForm,SearchForm
import random
#from django.http import HttpResponse
#from django.template import loader
# Create your views here.
@login_required
def index(request):
    items=clients.objects.all()
    context={
        'items':items
    }
    #print(request.user) 
    return render(request,'customers/index.html',context)
    #return HttpResponse("<h1>Hello</h1>")

@login_required
def details_of_shop(request,id):
    client = clients.objects.get(shop_id=id)
    
    transactions = json.loads(client.transactions)
    amounts = json.loads(client.amounts)
    
    transaction_data = []
    for i in range(len(transactions)):
        transaction_data.append({'transaction': transactions[i], 'amount': amounts[i]})

    context = {
        'ids': client,
        'transaction_data': transaction_data,
    }

    return render(request, 'customers/details.html', context)
@login_required
def shop_list(request):
    form=SearchForm(request.POST or None)
    if form.is_valid():
        search_location = request.POST.get("location")

        # Filter shops based on the entered location
        shops = clients.objects.filter(location__icontains=search_location)
        return render(request, "customers/shop_list.html", {"shops": shops})
    return render(request,"customers/searchShop.html",{form:'form'})
@login_required
def add_transaction(request,id):
    try:
        form=new_tranaction(request.POST or None)
        if form.is_valid():
            client=clients.objects.get(pk=id)
            existing_transactions = json.loads(client.transactions)
            existing_amounts = json.loads(client.amounts)
            new_transactions=form.cleaned_data.get('transactions')
            new_amounts=form.cleaned_data.get('amounts')
            if '\n' in new_transactions and '\n' in new_amounts:
                new_amounts=list(map(str,new_amounts.split('\n')))
                new_transactions=list(map(str,new_transactions.split('\n')))
                for i in range(len(new_transactions)):
                    if 'paid' in new_transactions[i].lower():
                        new_amounts[i]='-'+new_amounts[i]
            else:
                if 'paid' in new_transactions.lower():
                    new_amounts='-'+new_amounts
                new_amounts=[new_amounts]
                new_transactions=[new_transactions]
            existing_transactions.extend(new_transactions)
            existing_amounts.extend(new_amounts)
            new_amounts_int = sum([int(i) for i in existing_amounts])   
            client.balance =new_amounts_int
            client.transactions = json.dumps(existing_transactions)
            client.amounts = json.dumps(existing_amounts)
            client.save()
            messages.success(request,'transaction added successfully')
            return redirect("shops:details_of_shop",id=id)
        #messages.success(request,'please enter valid details')
        return render(request,'customers/new-transaction.html',{'form':form})
    except Exception  as e:
        messages.success(request,'please enter valid details')
        return render(request,'customers/new-transaction.html',{'form':form})
'''def delete_transaction(request,id):
    items=clients.objects.get(shop_id=id)
    if request.method=='POST':
        items.delete()
        return redirect('shops:details_of_shop')
    return render(request,'customers/delete-transaction.html',{'items':items})'''
@login_required
def delete_shop(request,id):
    items=clients.objects.get(shop_id=id)
    if request.method=='POST':
        items.delete()
        return redirect('shops:index')
    return render(request,'customers/delete-shop.html',{'items':items})

'''def add_shop(request):
    form = addShopForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("shops:index")
    return render(request, "customers/add-shop.html", {'form': form})'''
@login_required
def add_shop(request):
    if request.method == 'POST':
        shop_id = random.randint(1000,1000000)
        shop_name = request.POST.get('shop_name', '')
        location = request.POST.get('location', '')
        phone_no = request.POST.get('phone_no', '')
        email = request.POST.get('email', 'temp@gmail.com')
        image = request.POST.get('image', 'https://th.bing.com/th/id/OIP.kqT6XFsG2BTW22Y4st2-KAHaHa?pid=ImgDet&rs=1')
        balance = request.POST.get('balance', 0)
        transactions_input = request.POST.get('transactions', '')
        amounts_input = request.POST.get('amounts', '')
        transactions_input=transactions_input.replace("\"","")
        transactions_input=transactions_input.replace("\'","")
        transactions_input=transactions_input.replace("[","")
        transactions_input=transactions_input.replace("]","")
        amounts_input=amounts_input.replace("\"","")
        amounts_input=amounts_input.replace("\'","")
        amounts_input=amounts_input.replace("[","")
        amounts_input=amounts_input.replace("]","")
        transactions = [transaction.strip() for transaction in transactions_input.split('\n')] if transactions_input else []
        amounts = [amount.strip() for amount in amounts_input.split('\n')] if amounts_input else []
        #new_transactions=list(map(str,new_transactions.split('\n')))
        for i in range(len(transactions)):
            if 'paid' in transactions[i].lower():
                amounts[i]='-'+amounts[i]
        balance=sum([int(i) for i in amounts])
        shop = clients(
            shop_id=shop_id,
            shop_name=shop_name,
            location=location,
            phone_no=phone_no,
            email=email,
            image=image,
            balance=balance,
            transactions=json.dumps(transactions),
            amounts=json.dumps(amounts)
        )
        shop.save()
        messages.success(request,'Shop is added successfully')
        return redirect('shops:index')
    return render(request, 'customers/add-shop.html')



'''def edit_shop(request,id):
    items=clients.objects.get(shop_id=id)
    form=editShopForm(request.POST or None,instance=items)
    if form.is_valid():
        form.save()
        
        return redirect("shops:index")
    return render(request,"customers/edit-shop.html",{'form':form,'items':items})'''

def edit_shop(request, id):
    shop = clients.objects.get(shop_id=id)
    if request.method == 'POST':
        shop.shop_name = request.POST.get('shop_name', '')
        shop.location = request.POST.get('location', '')
        shop.phone_no = request.POST.get('phone_no', '')
        shop.email = request.POST.get('email', 'temp@gmail.com')
        shop.image = request.POST.get('image', 'https://th.bing.com/th/id/OIP.kqT6XFsG2BTW22Y4st2-KAHaHa?pid=ImgDet&rs=1')
        client=clients.objects.get(pk=id)
        existing_amounts = json.loads(client.amounts)
        
        balance = request.POST.get('balance',0)
        
        transactions_input = request.POST.get('transactions', '')
        amounts_input = request.POST.get('amounts', '')
        #print("\n\n\n\n\n\n",amounts_input)
        transactions_input=transactions_input.replace("\"","")
        transactions_input=transactions_input.replace("\'","")
        transactions_input=transactions_input.replace("[","")
        transactions_input=transactions_input.replace("]","")
        amounts_input=amounts_input.replace("\"","")
        amounts_input=amounts_input.replace("\'","")
        amounts_input=amounts_input.replace("[","")
        amounts_input=amounts_input.replace("]","")
        
        transactions = [transaction.strip() for transaction in transactions_input.split(',')] if transactions_input else []
        amounts = [amount.strip() for amount in amounts_input.split(',')] if amounts_input else []
        shop.balance=sum([int(i) for i in amounts])
        print(shop.balance)
        shop.transactions = json.dumps(transactions)
        shop.amounts = json.dumps(amounts)

        shop.save()
        return redirect('shops:index')

    context = {
        'shop': shop
    }
    return render(request, 'customers/edit-shop.html', context)
'''def edit_transaction(request,id):
    item=clients.objects.get(shop_id=id)
    existing_transactions = json.loads(client.transactions)
    existing_amounts = json.loads(client.amounts)'''
