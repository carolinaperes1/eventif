from django.shortcuts import render
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm

def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)