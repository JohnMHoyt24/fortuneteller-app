from django.shortcuts import render
import random

#fortuneList stores the set of fortunes that get displayed.
fortuneList = [
     "All will go well with your new project.",
   "If you continually give, you will continually have.",
   "Self-knowledge is a life long process.",
   "You are busy, but you are happy.",
   "Your abilities are unparalleled.",
   "Those who care will make the effort.",
   "Now is the time to try something new.",
   "Miles are covered one step at a time.",
   "Don’t just think, act!"
]
# Create your views here.
#This function creates the view by rendering fortune.html.
def fortune(request):
  #HttpResponse is the function that renders the page
  fortune = random.choice(fortuneList)
  context = {"fortune": fortune}
  return render(request, "randomfortune/fortune.html", context)
