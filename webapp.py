from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)


#load the data from the JSON file
with open('billionaires.json') as billionaires:
    billionaire_data = json.load(billionaires) 


@app.route('/')
def render_about():
    return render_template('home.html')
    
    
@app.route('/nameData')
def render_nameData():
	# with open('billionaires.json') as billionaires:
# 		billionaire_data = json.load(billionaires) 
# 	name = get_name_options()
	if "year" in request.args and "name" in request.args:
		year = request.args['year']
		name = request.args['name']
		info = get_info(name, year)
		return render_template('nameData.html', name_options=get_name_options(), year_options=get_year_options(), name=name, info=info) 
	return render_template('nameData.html', name_options=get_name_options(), year_options=get_year_options())


@app.route('/totalWorth')
def render_totalWorth():
	if "name" in request.args:
		name = request.args['name']
		return render_template('totalWorth.html', name_options=get_name_options(), name=name, worth=total_worth(name))
	return render_template('totalWorth.html', name_options=get_name_options())
    
    
@app.route('/worthChart')
def render_worthChart():
	if "name" in request.args:
		name = request.args['name']
		name2 = request.args['name2']
		name3 = request.args['name3']
		name4 = request.args['name4']
		name5 = request.args['name5']
		
		worth=total_worth_chart(name)
		worth2=total_worth_chart(name2)
		worth3=total_worth_chart(name3)
		worth4=total_worth_chart(name4)
		worth5=total_worth_chart(name5)
		return render_template('worthChart.html', name_options=get_name_options(), name=name, name2=name2, name3=name3, name4=name4, name5=name5, worth=worth, worth2=worth2, worth3=worth3, worth4=worth4, worth5=worth5) 
	return render_template('worthChart.html', name_options=get_name_options())


    
def total_worth_chart(name):
    # Returns the total worth of a selected billionaire
    with open('billionaires.json') as billionaires:
        billionaire_data = json.load(billionaires)
    initial_worth = None
    worth = 0
    for w in billionaire_data:
    	if w["name"] == name:
    		worth += w["wealth"]["worth in billions"]
    return str(round(worth))

    
def total_worth(name):
    # Returns the total worth of a selected billionaire
    with open('billionaires.json') as billionaires:
        billionaire_data = json.load(billionaires)
    initial_worth = None
    worth = 0
    worth_difference = 0
    for w in billionaire_data:
        if w["name"] == name:
            if initial_worth is None:
                initial_worth = w["wealth"]["worth in billions"]
            worth += w["wealth"]["worth in billions"]
    worth_difference = worth - initial_worth
    return name + "'s total worth combining the years 1996, 2001, and 2014 is " + str(round(worth)) + " billion dollars. In 1996 " + name + " was worth " + str(round(initial_worth)) + " billion dollars. This means that " + name + " grew " + str(round(worth_difference)) + " billion dollars."
	

	
def get_year_options():
#Returns the html code for a drop down menu.  Each option is a year for which there is complete data (1990 and 2016 are missing data)."""
	with open('billionaires.json') as billionaires:
		billionaire_data = json.load(billionaires) 
	years = []
	for y in billionaire_data:
		if y["year"] not in years:
			years.append(y["year"])
	year_options = ""
	for year in years:
		year_options += Markup("<option value=\"" + str(year) + "\">" + str(year) + "</option>")
	return year_options



def get_name_options():
#Returns the html code for a drop down menu.  Each option is a year for which there is complete data (1990 and 2016 are missing data)."""
	with open('billionaires.json') as billionaires:
		billionaire_data = json.load(billionaires) 
	names = []
	for n in billionaire_data:
		if n["name"] not in names:
			names.append(n["name"])
	options = ""
	for name in names:
		options += Markup("<option value=\"" + name + "\">" + name + "</option>")
	return options
	
	
	
def get_info(name, year):
	rank = ""
	company = ""
	founded = ""
	sector = ""
	age = ""
#Returns information on the billionaire selected
	with open('billionaires.json') as billionaires:
		billionaire_data = json.load(billionaires) 
	for n in billionaire_data:
		if n["name"] == name:
			if n["year"] == int(year):	
				rank = n["rank"]
				company = n["company"]["name"]
				founded = n["company"]["founded"]
				sector = n["company"]["sector"]
				age = n["demographics"]["age"]
				rank = name + " is the number " + str(rank) + " ranked billionaire in the world during " + str(year) + ". He became a billionaire at age " + str(age) + " by founding the company " + company + " in " + str(founded) + ". This company was founded in the " + sector + " sector."
				return rank
	return " This person is not a billionaire in the year you selected"



if __name__ == '__main__':
    app.run(debug=True) # change to False when running in production
