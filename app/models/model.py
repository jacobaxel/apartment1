import numpy as np

def apt1(option):
    dict = {
    "rent":"Rent: $6,000/month",
    "sq feet":"Square Footage: 3,228",
    "beds":"Number of Bedrooms: 4",
    "baths":"Number of Bathrooms: 3.5",
    "safety":"Safety of Neighborhood: 10",
    "elevator":"Elevator: Yes",
    "doorman":"Doorman: Yes",
    "proximity":"Proximity: 15 minutes",
    "pets":"Pets Allowed: No",
    "lighting":"Natural Lighting: Great"}
    return dict[option]
def scoreDict1(option):
    dict = {
    "rent":6000.0/18000.0,
    "sq feet":3228.0/10000.0,
    "beds":4.0/5.0,
    "baths":3.5/4.0,
    "safety":10.0/10.0,
    "elevator":1.0,
    "doorman":1.0,
    "proximity":15.0/75.0,
    "pets":0.0,
    "lighting":1.0}
    return dict[option]
def apt2(option):
    dict = {
    "rent":"Rent: $2,000/month",
    "sq feet":"Square Footage: 600",
    "beds":"Number of Bedrooms: 1",
    "baths":"Number of Bathrooms: 1",
    "safety":"Safety of Neighborhood: 7",
    "elevator":"Elevator: Yes",
    "doorman":"Doorman: No",
    "proximity":"Proximity: 5 minutes",
    "pets":"Pets Allowed: No",
    "lighting":"Natural Lighting: Average"}
    return dict[option]
def scoreDict2(option):
    dict = {
    "rent":2000.0/18000.0,
    "sq feet":600.0/10000.0,
    "beds":1.0/5.0,
    "baths":1.0/4.0,
    "safety":7.0/10.0,
    "elevator":1.0,
    "doorman":0.0,
    "proximity":5.0/75.0,
    "pets":0.0,
    "lighting":0.33}
    return dict[option]
def apt3(option):
    dict = {
    "rent":"Rent: $1,000/month",
    "sq feet":"Square Footage: 440",
    "beds":"Number of Bedrooms: 1",
    "baths":"Number of Bathrooms: 1",
    "safety":"Safety of Neighborhood: 9",
    "elevator":"Elevator: No",
    "doorman":"Doorman: No",
    "proximity":"Proximity: 5 minutes",
    "pets":"Pets Allowed: Yes",
    "lighting":"Natural Lighting: Great"}
    return dict[option]
def scoreDict3(option):
    dict = {
    "rent":1000.0/18000.0,
    "sq feet":440.0/10000.0,
    "beds":1.0/5.0,
    "baths":1.0/4.0,
    "safety":9.0/10.0,
    "elevator":0.0,
    "doorman":0.0,
    "proximity":5.0/75.0,
    "pets":1.0,
    "lighting":1.0}
    return dict[option]
def apt4(option):
    dict = {
    "rent":"Rent: $18,000/month",
    "sq feet":"Square Footage: 10,000",
    "beds":"Number of Bedrooms: 5",
    "baths":"Number of Bathrooms: 4",
    "safety":"Safety of Neighborhood: 6",
    "elevator":"Elevator: Yes",
    "doorman":"Doorman: Yes",
    "proximity":"Proximity: 75 minutes",
    "pets":"Pets Allowed: No",
    "lighting":"Natural Lighting: Good"}
    return dict[option]
def scoreDict4(option):
    dict = {
    "rent":18000.0/18000.0,
    "sq feet":10000.0/10000.0,
    "beds":5.0/5.0,
    "baths":4.0/4.0,
    "safety":6.0/10.0,
    "elevator":1.0,
    "doorman":1.0,
    "proximity":75.0/75.0,
    "pets":0.0,
    "lighting":0.66}
    return dict[option]
def apt5(option):
    dict = {
    "rent":"Rent: $800/month",
    "sq feet":"Square Footage: 1,800",
    "beds":"Number of Bedrooms: 4",
    "baths":"Number of Bathrooms: 2.5",
    "safety":"Safety of Neighborhood: 2",
    "elevator":"Elevator: No",
    "doorman":"Doorman: No",
    "proximity":"Proximity: 15 minutes",
    "pets":"Pets Allowed: Yes",
    "lighting":"Natural Lighting: Poor"}
    return dict[option]
def scoreDict5(option):
    dict = {
    "rent":800.0/18000.0,
    "sq feet":1800.0/10000.0,
    "beds":4.0/5.0,
    "baths":2.5/4.0,
    "safety":2.0/10.0,
    "elevator":0.0,
    "doorman":0.0,
    "proximity":15.0/75.0,
    "pets":1.0,
    "lighting":0.0}
    return dict[option]
def apt6(option):
    dict = {
    "rent":"Rent: $1,400/month",
    "sq feet":"Square Footage: 700",
    "beds":"Number of Bedrooms: 2",
    "baths":"Number of Bathrooms: 1",
    "safety":"Safety of Neighborhood: 4",
    "elevator":"Elevator: Yes",
    "doorman":"Doorman: No",
    "proximity":"Proximity: 35 minutes",
    "pets":"Pets Allowed: Yes",
    "lighting":"Natural Lighting: Great"}
    return dict[option]
def scoreDict6(option):
    dict = {
    "rent":1400.0/18000.0,
    "sq feet":700.0/10000.0,
    "beds":2.0/5.0,
    "baths":1.0/4.0,
    "safety":4.0/10.0,
    "elevator":1.0,
    "doorman":0.0,
    "proximity":35.0/75.0,
    "pets":1.0,
    "lighting":1.0}
    return dict[option]
def apt7(option):
    dict = {
    "rent":"Rent: $300/month",
    "sq feet":"Square Footage: 400",
    "beds":"Number of Bedrooms: 1",
    "baths":"Number of Bathrooms: 1",
    "safety":"Safety of Neighborhood: 10",
    "elevator":"Elevator: No",
    "doorman":"Doorman: No",
    "proximity":"Proximity: 1 minute",
    "pets":"Pets Allowed: Yes",
    "lighting":"Natural Lighting: Poor"}
    return dict[option]
def scoreDict7(option):
    dict = {
    "rent":300.0/18000.0,
    "sq feet":400.0/10000.0,
    "beds":1.0/5.0,
    "baths":1.0/4.0,
    "safety":10.0/10.0,
    "elevator":0.0,
    "doorman":0.0,
    "proximity":1.0/75.0,
    "pets":1.0,
    "lighting":0.0}
    return dict[option]
def apt8(option):
    dict = {
    "rent":"Rent: $2,500/month",
    "sq feet":"Square Footage: 1,000",
    "beds":"Number of Bedrooms: 1",
    "baths":"Number of Bathrooms: 2",
    "safety":"Safety of Neighborhood: 8",
    "elevator":"Elevator: No",
    "doorman":"Doorman: No",
    "proximity":"Proximity: 2 minutes",
    "pets":"Pets Allowed: No",
    "lighting":"Natural Lighting: Good"}
    return dict[option]
def scoreDict8(option):
    dict = {
    "rent":2500.0/18000.0,
    "sq feet":1000.0/10000.0,
    "beds":1.0/5.0,
    "baths":2.0/4.0,
    "safety":8.0/10.0,
    "elevator":0.0,
    "doorman":0.0,
    "proximity":2.0/75.0,
    "pets":0.0,
    "lighting":0.66}
    return dict[option]
def apt9(option):
    dict = {
    "rent":"Rent: $300/month",
    "sq feet":"Square Footage: 200",
    "beds":"Number of Bedrooms: 0",
    "baths":"Number of Bathrooms: 0.5",
    "safety":"Safety of Neighborhood: 10",
    "elevator":"Elevator: No",
    "doorman":"Doorman: No",
    "proximity":"Proximity: 0.5 minutes",
    "pets":"Pets Allowed: Yes",
    "lighting":"Natural Lighting: Great"}
    return dict[option]
def scoreDict9(option):
    dict = {
    "rent":300.0/18000.0,
    "sq feet":200.0/10000.0,
    "beds":0.0/5.0,
    "baths":0.5/4.0,
    "safety":10.0/10.0,
    "elevator":0.0,
    "doorman":0.0,
    "proximity":0.5/75.0,
    "pets":1.0,
    "lighting":1.0}
    return dict[option]
def apt10(option):
    dict = {
    "rent":"Rent: Free",
    "sq feet":"Square Footage: 250",
    "beds":"Number of Bedrooms: 1",
    "baths":"Number of Bathrooms: 1",
    "safety":"Safety of Neighborhood: 2",
    "elevator":"Elevator: No",
    "doorman":"Doorman: No",
    "proximity":"Proximity: 70 minutes",
    "pets":"Pets Allowed: Yes",
    "lighting":"Natural Lighting: Poor"}
    return dict[option]
def scoreDict10(option):
    dict = {
    "rent":0.0/18000.0,
    "sq feet":250.0/10000.0,
    "beds":1.0/5.0,
    "baths":1.0/4.0,
    "safety":2.0/10.0,
    "elevator":0.0,
    "doorman":0.0,
    "proximity":70.0/75.0,
    "pets":1.0,
    "lighting":0.0}
    return dict[option]
def end(option):
    dict = {
    "rent":"Rent",
    "sq feet":"Square Footage",
    "beds":"Number of Bedrooms",
    "baths":"Number of Bathrooms",
    "safety":"Safety of Neighborhood",
    "elevator":"Elevator",
    "doorman":"Doorman",
    "proximity":"Proximity From Work/School",
    "pets":"Pets Allowed",
    "lighting":"Natural Lighting"}
    return dict[option]
def score(myScore):
    dict = {"one":1,"two":2,"three":3,"four":4,"five":5,
    "six":6,"seven":7,"eight":8,"nine":9,"ten":10}
    return dict[myScore]

def solveWeights(listOfScores, listOfOptions, listy1, listy2, listy3, listy4,
listy5, listy6,listy7, listy8,listy9, listy10):
    # numZeroes = 10 - len(listOfOptions)
    # zeroesList = [0.0] * numZeroes
    # alos = []
    # for b in listOfScores:
    #     alos.append([b])
    # solutionArray = np.array(alos)
    numVars = len(listOfOptions)
    solutionArray = np.array(listOfScores)
    A = [listy1, listy2, listy3, listy4, listy5, listy6,
    listy7, listy8, listy9, listy10]
    Atp = np.transpose(A)
    x = np.linalg.inv(Atp @ A) @ Atp @ solutionArray   #*Atp*solutionArray
    mySoln = x
    squared = []
    for a in np.nditer(mySoln):
        squared.append(a*a)
    sortedSq = sorted(squared, reverse = True)
    topThree = []
    myCount = 0
    while myCount < 3:
        myIndex = squared.index(sortedSq[myCount])
        topThree.append(listOfOptions[myIndex])
        myCount = myCount + 1
    return topThree

    #
    # listOfSolutionWeights = linSolved.toList()
    # listOfSolutionWeights = sorted(listOfSolutionWeights, key = lambda x: float(abs(x)))
    # topThree = []
    # myCounter = 0
    # while myCounter < 3:
    #     topThree.append(listOfSolutionWeights[myCounter])
    #     myCounter = myCounter + 1
    # return topThree


# import requests
# import random
# # def pickArea():
# #     cuisine_url= 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
#
#
# # area = 'American'
# # # meal =
# # recipe_url= ''
#
# # response = requests.get(area_url).json()
# cuisine_url= 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
# area = requests.get(cuisine_url).json()['meals'][5]['strArea']
# meals_url= 'https://www.themealdb.com/api/json/v1/1/filter.php?a=' + area
# meal = requests.get(meals_url).json()['meals'][0]['strMeal']
# recipe_url='https://www.themealdb.com/api/json/v1/1/search.php?s=' + meal
# recipe = requests.get(recipe_url).json()['meals'][0]['strIngredient7']
# cuisineList = requests.get(cuisine_url).json()['meals']
# # mealList = requests.get(meals_url).json()['meals']
#
# # def cuisines():
# #     for x in cuisineList:
# #         print(x['strArea'])
# #     return "done"
# # cuisines()
#
#
# def meals(cuisine_area):
#     meals_url= 'https://www.themealdb.com/api/json/v1/1/filter.php?a=' + cuisine_area
#     return requests.get(meals_url).json()['meals']
#
# def recipes(meal_food):
#     recipe_url='https://www.themealdb.com/api/json/v1/1/search.php?s=' + meal_food
#     return requests.get(recipe_url).json()['meals']
#
# # print(meals('Egyptian'))
# # print(mealList)
#
#     #requests.get(meals_url).json()['meals']
#
# def code(cuisine):
#     temp = {"American":"us","British":"gb","Canadian":"ca","Chinese":"cn","Dutch":"nl","Egyptian":"eg","French":"fr","Greek":"gr","Indian":"in","Irish":"ie","Italian":"it","Jamaican":"jm","Japanese":"jp","Kenyan":"ke","Malaysian":"my","Mexican":"mx","Moroccan":"ma","Russian":"ru","Spanish":"es","Thai":"th","Tunisian":"tn","Unknown":"aq","Vietnamese":"vn"}
#     if cuisine not in temp:
#         cuisine = random.choice(list(temp.keys()))
#         # session['cuisine'] = cuisine
#     return {'cuisine':cuisine, 'code':temp[cuisine]}
# # print(requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=Garides%20Saganaki').json()['meals'])
