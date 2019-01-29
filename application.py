import os
import requests
from flask import Flask, render_template, request
from getstats import Baseball

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('welcome.html')

@app.route('/basics',methods = ['POST', 'GET'])
def basic_results():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      return render_template("basics.html",result = myteam.results, errors = myteam.errors)

@app.route('/batting',methods = ['POST', 'GET'])
def batting_result():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      myteam.batting_stats('atBats', 'runs', 'hits', 'homeruns', 'runsBattedIn', 'earnedRuns',
                            'stolenBases', 'battingAvg', 'batterOnBasePct', 'totalBases')
      return render_template("batting.html",result = myteam.results, errors = myteam.errors)

@app.route('/pitching',methods = ['POST', 'GET'])
def pitching_result():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      myteam.pitching_stats('earnedRunAvg', 'inningsPitched', 'pitchingAvg', 'shutouts',
                            'battersHit', 'pitcherStrikeouts','strikeoutsPer9Innings')
      return render_template("pitching.html",result = myteam.results, errors = myteam.errors)

@app.route('/fielding',methods = ['POST', 'GET'])
def fielding_result():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      myteam.fielding_stats('inningsPlayed', 'totalChances', 'fielderTagOuts', 'assists', 'errors',
                            'fielderDoublePlays', 'passedBalls',  'fieldingPct', 'defenceEfficiencyRatio')
      return render_template("fielding.html",result = myteam.results, errors = myteam.errors)

@app.route('/overall',methods = ['POST', 'GET'])
def overall_result():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      myteam.overall_stats('wins', 'losses', 'gamesBack', 'runsFor', 'runsAgainst', 'runDifferential')
      return render_template("overall.html",result = myteam.results, errors = myteam.errors)

if __name__ == '__main__':
   app.run(debug = True)





# @app.route('/', methods=['GET', 'POST'])
# def index():
#     errors = []
#     results = {'key':'value', 'key2':'value2', 'key3':'value3'}
#     if request.method == "POST":
#         # get url that the person has entered
#         input = request.form.get('name')
#         # myteam = Baseball(team=str(input))
#         # errors=myteam.errors
#         # results=myteam.results
#         results['key4':str(input)]
#         return render_template('index.html', errors=errors, results=results)
