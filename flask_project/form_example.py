# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:28:45 2021

@author: Sarbajit
"""

from flask import Flask, render_template, request, flash  
from forms import ContactForm  
app = Flask(__name__)  
app.secret_key = 'development key'  
  
@app.route('/contact', methods = ['GET', 'POST'])  
def contact():  
   form = ContactForm()  
   if form.validate() == False:  
      flash('All fields are required.')  
   return render_template('contact.html', formform = form)  
  
  
  
@app.route('/success',methods = ['GET','POST'])  
def success():  
   return render_template("success.html")  
  
if __name__ == '__main__':  
   app.run()  