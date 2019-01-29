import os
import requests
from flask import Flask, render_template, request
from getstats import Baseball

application = Flask(__name__)

@application.route('/')
def student():
   return render_template('welcome.html')

@application.route('/basics',methods = ['POST', 'GET'])
def basic_results():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      results=myteam.results
      return render_template("basics.html",result = results, errors = myteam.errors)

@application.route('/batting',methods = ['POST', 'GET'])
def batting_result():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      results=myteam.batting_stats('atBats', 'runs', 'hits', 'homeruns', 'runsBattedIn', 'earnedRuns',
                            'stolenBases', 'battingAvg', 'batterOnBasePct', 'totalBases')
      return render_template("batting.html",result = results, errors = myteam.errors)

@application.route('/pitching',methods = ['POST', 'GET'])
def pitching_result():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      results=myteam.pitching_stats('earnedRunAvg', 'inningsPitched', 'pitchingAvg', 'shutouts',
                            'battersHit', 'pitcherStrikeouts','strikeoutsPer9Innings')
      return render_template("pitching.html",result = results, errors = myteam.errors)

@application.route('/fielding',methods = ['POST', 'GET'])
def fielding_result():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      results=myteam.fielding_stats('inningsPlayed', 'totalChances', 'fielderTagOuts', 'assists', 'errors',
                            'fielderDoublePlays', 'passedBalls',  'fieldingPct', 'defenceEfficiencyRatio')
      return render_template("fielding.html",result = results, errors = myteam.errors)

@application.route('/overall',methods = ['POST', 'GET'])
def overall_result():
   if request.method == 'POST':
      input = request.form
      myteam = Baseball(team=str(input['Name']))
      results=myteam.overall_stats('wins', 'losses', 'gamesBack', 'runsFor', 'runsAgainst', 'runDifferential')
      return render_template("overall.html",result = results, errors = myteam.errors)

if __name__ == '__main__':
   application.run(debug = True, port=8080)
