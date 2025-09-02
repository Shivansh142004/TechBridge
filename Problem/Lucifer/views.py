from django.shortcuts import render
from .forms import TweetForm, UserRegistrationForm
from .models import Tweet
from django.shortcuts import get_object_or_404, redirect # this is used to get the object from the database or return a 404 error if it does not exist and redirect to another page
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



def index(request): #in this function we render the index page
    return render(request, 'index.html') # in this line we render the index.html page
# Create your views here.

@login_required # in this line we check if the user is logged in or not, if not then it will redirect to the login page
def tweet_list(request): #esh function me ham sabhi tweets ko list karte hai aur unhe order by date aur time ke hisab se sort karte hai 
    tweets = Tweet.objects.all().order_by('created_at') #esh line me ham sabhi tweets ko lete hai aur unhe created_at ke hishab se order karte hai 
    return render(request,'tweet_list.html',{'tweets': tweets}) # eshke liye ham ko ek new page desing karna hoga

@login_required 
def tweet_create(request): #esh function me ham tweet create karte hai 
    if request.method == 'POST': #esh line me ham check karte hai ki request POST hai ya nahi
        form = TweetForm(request.POST, request.FILES) #esh line me ham form ko create karte hai aur POST data aur FILES ko pass karte hai 
        if form.is_valid():  #esh line me ham check karte hai ki form valid hai ya nahi 
            tweet = form.save(commit=False) #esh line me ham form ko save karte hai lekin commit=FALSE karte hai matlab abhi save nahi hota 
            tweet.user = request.user #esh line me ham user ko set karte hai jo tweet create kar raha hai 
            tweet.save() #esh line me ham tweet ko save karte hai
            return redirect('tweet_list') #esh line me ham tweet_list page par redirect karte hai 
    else:
        form = TweetForm() #esh line me ham form ko create karte hai ager POST request nahi hai 
    return render(request, 'tweet_create.html', {'form': form}) #esh line me ham form ko render karte hai tweet_create.html page me

@login_required
def tweet_edit(request, tweet_id): #esh function me ham tweet ko edit karte hai 
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user) #esh line me ham tweet ko get karte hai ya 404 error return karte hai ager tweet exist nahi karta aur user bhi wahi hai jo tweet create kiya tha
    if request.method == 'POST': #esh line me ham check karte hai ki request POST hai ya nahi 
        form = TweetForm(request.POST, request.FILES, instance=tweet) #esh line me ham form ko create karte hai aur POST data aur FILES ko pass karte hai aur instance me tweet ko set karte hai 
        if form.is_valid(): #esh line me ham check karte hai ki form valid hai ya nahi
            tweet = form.save(commit=False) #esh line me ham form ko save karte hai lekin commit = FALSE karte hai matlab abhi save nahi hota
            tweet.user = request.user #esh line me ham user ko set karte hai jo tweet edit kar raha hai
            tweet.save() #esh line me ham tweet ko save karte hai
            return redirect('tweet_list') #esh line me ham tweet_list page par redirect karte hai
    else:
        form = TweetForm(instance = tweet) #esh line me ham form ko create karte hai aur instance me tweet ko set karte hai 
    return render(request, 'tweet_create.html', {'form': form}) #esh line me ham form ko render karte hai tweet_create.html page me 

@login_required
def tweet_delete(request, tweet_id): #esh function me ham tweet ko delete karte hai
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user) #esh line me ham tweet ko get karte hai ya 404 error return karte hai ager tweet exist nahi karta aur user bhi wahi hai jo tweet create kiya tha 
    if request.method == 'POST': #esh line me ham check karte hai ki request POST hai ya nahi
        tweet.delete() #esh line me ham tweet ko ddelete karte hai 
        return redirect('tweet_list') #esh line me ham tweet_list page per redirect karte hai
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet}) #esh line me ham tweet_confirm_delete.html page ko render karte hai aur tweet ko pass karte hai 


def register(request): # in this line we define the register view
    if request.method == 'POST': # in this line we check if the request method is POST
        form = UserRegistrationForm(request.POST) # in this line we create a form instance with the POST data
        if form.is_valid(): # in this line we check if the form is valid
            user = form.save(commit=False) # in this line we save the user instance but do not commit it to the database yet
            user.set_password(form.cleaned_data['password1']) # in this line we set the password for the user instance
            user.save() # in this line we save the user instance to the database
            login(request, user) # in this line we log the user in after registration
            return redirect('tweet_list') # in this line we redirect the user to th tweet list page after successful registrations
    else:
        form = UserRegistrationForm() # in this line we create a form instance for GET request
    return render(request, 'registration/register.html', {'form': form}) # in this line we render the registration page with the form instance



    

