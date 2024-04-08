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
#load the data from the JSON file
	with open('billionaires.json') as billionaires:
    	billionaire_data = json.load(billionaires) 
    	if 'name' in request.args:
    	name = request.args['name']
    	return render_template('nameData.html', name=name, options=get_year_options(weeks))

def get_year_options(weeks):
#     Returns the html code for a drop down menu.  Each option is a year for which there is complete data (1990 and 2016 are missing data)."""
    names = []
    options = ""
    for n in billionaire_data:
        names = n["Date"]["Year"]
        if (year not in years) and not (year == 1990 or year == 2016):
            years.append(year)
            options += Markup("<option value=\"" + str(year) + "\">" + str(year) + "</option>")
    return options



# @app.route('/')
# def home():
#     states = get_state_options()
#     #print(states)
#     return render_template('home.html', state_options=states)
# 
# @app.route('/showFact')
# def render_fact():
#     states = get_state_options()
#     state = request.args.get('state')
#     county = county_most_under_18(state)
#     county2 = county_highest_female(state)
#     county3 = county_Veterans(state)
#     county4 = county_2014_Population(state)
# #     highest =  county_2014_Population(state)
# #     countys = total_countys()
#     fact = "In " + state + ", the county with the highest percentage of under 18 year olds is " + county + "."
#     fact2 = "In " + state + ", the county with the highest percentage of females is " + county2 + "."
#     fact3 = "In " + state + ", the county with the highest number of veterans is " + county3 + "."
#     fact4 = "In " + state + ", the county with the highest population is " + county4 + "."
#     return render_template('home.html', state_options=states, funFact=fact, funFact2=fact2, funFact3=fact3, funFact4=fact4)
#     
#     
# # def total_countys():
# # 	with open('demographics.json') as demographics_data:
# # 		counties = json.load(demographics_data)
# # 	countys=0
# # 	for c in counties:
# # 		countys += 1
# # 	return countys
# 	
# 	
# def get_state_options():
#     """Return the html code for the drop down menu.  Each option is a state abbreviation from the demographic data."""
#     with open('demographics.json') as demographics_data:
#         counties = json.load(demographics_data)
#     states=[]
#     for c in counties:
#         if c["State"] not in states:
#             states.append(c["State"])
#     options=""
#     for s in states:
#         options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
#     return options
# 
# def county_most_under_18(state):
#     """Return the name of a county in the given state with the highest percent of under 18 year olds."""
#     with open('demographics.json') as demographics_data:
#         counties = json.load(demographics_data)
#     highest=0
#     county = ""
#     for c in counties:
#         if c["State"] == state:
#             if c["Age"]["Percent Under 18 Years"] > highest:
#                 highest = c["Age"]["Percent Under 18 Years"]
#                 county = c["County"]
#     return county
#     
# def county_highest_female(state):
#     """Return the name of a county in the given state with the highest percent of under 18 year olds."""
#     with open('demographics.json') as demographics_data:
#         counties = json.load(demographics_data)
#     highest=0
#     county2 = ""
#     for c in counties:
#         if c["State"] == state:
#             if c["Miscellaneous"]["Percent Female"] > highest:
#                 highest = c["Miscellaneous"]["Percent Female"]
#                 county2 = c["County"]
#     return county2
#     
# def county_Veterans(state):
#     """Return the name of a county in the given state with the highest percent of under 18 year olds."""
#     with open('demographics.json') as demographics_data:
#         counties = json.load(demographics_data)
#     highest=0
#     county3 = ""
#     for c in counties:
#         if c["State"] == state:
#             if c["Miscellaneous"]["Veterans"] > highest:
#                 highest = c["Miscellaneous"]["Veterans"]
#                 county3 = c["County"]
#     return county3
#     
# def county_2014_Population(state):
#     """Return the name of a county in the given state with the highest percent of under 18 year olds."""
#     with open('demographics.json') as demographics_data:
#         counties = json.load(demographics_data)
#     highest=0
#     county4 = ""
#     for c in counties:
#         if c["State"] == state:
#             if c["Population"]["2014 Population"] > highest:
#                 highest = c["Population"]["2014 Population"]
#                 county4 = c["County"]
#     return county4
#     return highest
#     
#     
# 
# def is_localhost():
#     """ Determines if app is running on localhost or not
#     Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
#     """
#     root_url = request.url_root
#     developer_url = 'http://127.0.0.1:5000/'
#     return root_url == developer_url
# 
# 
if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production
