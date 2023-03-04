
import os,sys
from os.path import dirname ,join,abspath

sys.path.insertI(0,abspath(dirname(__file__),'..'))



from payment import payment_details



def course():
    print("This is my course details")
    

payment_details.payment()