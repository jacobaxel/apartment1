from app import app
from flask import render_template, request, session, redirect
from app.models import model, formopener
import random

app.secret_key=b'>C\xad\n\xc4\xbb\xd9/ \xe7\x8d\xdf?EY\xab\xa1\\\x8bd(\xa3\xf5z'

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/apartment1',methods=["GET","POST"])
def apartment1():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        myList = []
        counter = 0
        for key in userdata:
            myList.append(key)
            counter = counter + 1
        if counter > 2:
            map(model.apt1, myList)
            session['options'] = myList
            apt1List = []
            for x in myList:
                apt1List.append(model.apt1(x))
            return render_template('apt1.html', apt1List = apt1List)
        else:
            return redirect('/')
@app.route('/apartment2',methods=["GET","POST"])
def apartment2():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score1'] = score
        myList = session['options']
        apt2List = []
        for x in myList:
            apt2List.append(model.apt2(x))
        return render_template('apt2.html', apt2List = apt2List)

@app.route('/apartment3',methods=["GET","POST"])
def apartment3():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        myList = session['options']
        apt3List = []
        for x in myList:
            apt3List.append(model.apt3(x))
        return render_template('apt3.html', apt3List = apt3List)

@app.route('/apartment4',methods=["GET","POST"])
def apartment4():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score3'] = score
        myList = session['options']
        apt4List = []
        for x in myList:
            apt4List.append(model.apt4(x))
        return render_template('apt4.html', apt4List = apt4List)

@app.route('/apartment5',methods=["GET","POST"])
def apartment5():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score4'] = score
        myList = session['options']
        apt5List = []
        for x in myList:
            apt5List.append(model.apt5(x))
        return render_template('apt5.html', apt5List = apt5List)

@app.route('/apartment6',methods=["GET","POST"])
def apartment6():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score5'] = score
        myList = session['options']
        apt6List = []
        for x in myList:
            apt6List.append(model.apt6(x))
        return render_template('apt6.html', apt6List = apt6List)

@app.route('/apartment7',methods=["GET","POST"])
def apartment7():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score6'] = score
        myList = session['options']
        apt7List = []
        for x in myList:
            apt7List.append(model.apt7(x))
        return render_template('apt7.html', apt7List = apt7List)

@app.route('/apartment8',methods=["GET","POST"])
def apartment8():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score7'] = score
        myList = session['options']
        apt8List = []
        for x in myList:
            apt8List.append(model.apt8(x))
        return render_template('apt8.html', apt8List = apt8List)

@app.route('/apartment9',methods=["GET","POST"])
def apartment9():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score8'] = score
        myList = session['options']
        apt9List = []
        for x in myList:
            apt9List.append(model.apt9(x))
        return render_template('apt9.html', apt9List = apt9List)

@app.route('/apartment10',methods=["GET","POST"])
def apartment10():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score9'] = score
        myList = session['options']
        apt10List = []
        for x in myList:
            apt10List.append(model.apt10(x))
        return render_template('apt10.html', apt10List = apt10List)

@app.route('/end',methods=["GET","POST"])
def end():
    if request.method=="GET":
        return redirect('/')
    else:
        userdata = request.form
        if 'rating' not in userdata:
            score = random.randrange(1,10,1)
        else:
            score = model.score(userdata['rating'])
        session['score10'] = score
        myList = session['options']
        apt2List = []
        scoreList = [session['score1'],session['score2'],session['score3'],
        session['score4'],session['score5'],session['score6'],session['score7'],
        session['score8'],session['score9'],session['score10']]
        myList = session['options']
        endList = []
        for x in myList:
            endList.append(model.end(x))
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        for a in myList:
            list1.append(model.scoreDict1(a))
            list2.append(model.scoreDict2(a))
            list3.append(model.scoreDict3(a))
            list4.append(model.scoreDict4(a))
            list5.append(model.scoreDict5(a))
            list6.append(model.scoreDict6(a))
            list7.append(model.scoreDict7(a))
            list8.append(model.scoreDict8(a))
            list9.append(model.scoreDict9(a))
            list10.append(model.scoreDict10(a))
        topThree = model.solveWeights(scoreList, myList,
        list1, list2, list3, list4, list5, list6, list7, list8, list9, list10)
        toReturn = []
        for x in topThree:
            toReturn.append(model.end(x))
        counter = 1
        while counter < 4:
            if counter == 1:
                toReturn[counter-1] = "Your Highest Weighted Cue Was: " + toReturn[counter-1]
            elif counter == 2:
                toReturn[counter-1] = "Your Second Highest Weighted Cue Was: " + toReturn[counter-1]
            else:
                toReturn[counter-1] = "Your Third Highest Weighted Cue Was: " + toReturn[counter-1]
            counter = counter + 1
        topThree = toReturn
        return render_template('end.html', endList = endList, scoreList = scoreList,
        topThree = topThree, myList = myList)
        #, predictions = predictions)


        # if 'cuisine' not in userdata:
        #     # cuisine = 'American'
        #     cuisine = random.choice(model.cuisineList)['strArea']
        #     session['cuisine'] = model.code(cuisine)['cuisine']
        #     dishes = model.meals(session['cuisine'])
        #     code = model.code(cuisine)['code']
        #     return render_template('genre.html', cuisine=cuisine, dishes=dishes, code=code)
        # cuisine = userdata['cuisine']
        # session['cuisine'] = model.code(cuisine)['cuisine']
        # dishes = model.meals(session['cuisine'])
        # code = model.code(cuisine)['code']
        # return render_template('genre.html', cuisine=cuisine, dishes=dishes, code=code)

# @app.route('/dishes',methods=["GET","POST"])
# def recipe():
#     if request.method=="GET":
#         return redirect('/')
#     else:
#         userdata = request.form
#         if 'meal' not in userdata:
#             meal = random.choice(model.meals(session['cuisine']))['strMeal']
#             session['meal']=meal
#             recipe = model.recipes(session['meal'])
#             return render_template('recipe.html', meal=meal, recipe=recipe)
#         meal = userdata['meal']
#         session['meal']=meal
#         recipe = model.recipes(session['meal'])
#         return render_template('recipe.html', meal=meal, recipe=recipe)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')
