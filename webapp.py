from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def render_response():
    passangers = float(request.args['passangers']) 
    budget = request.args['budget'] 
    use = request.args['use'] 
      
    if passangers <= 8 and budget == "20" and use == 'long distance driving' :
        car = "volvo xc90" ", " "ford explorer"
    elif passangers <= 8 and budget == "55" and use == 'long distance driving' :
        car = "chevy suburban" ", " "lexus RX" ", " "BMW 5 series"
    elif  passangers <= 8 and budget == "80" and use == 'long distance driving' :
        car = "lamborghini urus" ", " "porche panamera" ", " "mercedez benz s-class" 
    elif  passangers <= 5 and budget == "20" and use == 'commute to work/school' :
        car = "toyota prius" ", " "toyota corrola" ", " "chevy malibu"
    elif  passangers <= 5 and budget == "55" and use == 'commute to work/school' :
        car = "tesla model s" ", " "mercedez benz GLE" 
    elif  passangers <= 5 and budget == "80" and use == 'commute to work/school' :
        car = "porche cheyan" ", " "mercedez G wagon" ", " "tesla model y" ", " "tesla model x"
    elif  passangers <= 4 and budget == "20" and use == 'personal enjoynment' :
        car = "nissan 370z" ", " "toyoyta supra" ", " "toyota GR86" ", " "Alfa romeo giulia"
    elif  passangers ==5  and budget == "55" and use == 'personal enjoynment' :
        car = "dodge scat pack ", " " "bmw 3 series" ", " "mercedez amg c300" 
    else:
        car = "dodge hellcat" "dode demon" "lomborghini urus" "ferrari purosangue" "aston martin DBX"
        
    return render_template('response.html',choice=car)
    
if __name__=="__main__":
    app.run(debug=True)
