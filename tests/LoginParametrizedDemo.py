import os
import requests,json


from faker import Faker
from time import sleep

##
## 1) Generate python stub source code:
##    java -jar graphwalker-3.4.0-SNAPSHOT.jar source -i model.graphml python.template > model.py
##
## 2) Start graphwalker:
##    java -jar graphwalker-3.4.0-SNAPSHOT.jar online --service RESTFUL -m model.graphml "random(edge_coverage(100))"
##
## 3) Run the per program:
##    python model.py
##

data = {item : [Faker().name(), Faker().password(4)] for item in range(1, 21)}

data_iter = iter(data)

result_dump = False

def ApplicationLaunched() :
    print( "ApplicationLaunched" )
    return




def GoToAnotherTests() :
    print( "GoToAnotherTests" )
    return




def LaunchApplication() :
    print( "LaunchApplication" )
    return




def LogOut() :
    print( "LogOut" )
    return




def LoggedIn() :
    print( "LoggedIn" )
    return




def LoggedOut() :
    print( "LoggedOut" )
    return




def Login() :
    try:
        user = data_iter.next()
        print "Login with user:: {}".format(user)
        print "User :: {} Pass :: {}".format(data[user][0], data[user][1])
        sleep(.5)
    except StopIteration:
        requests.put(gw_url + '/setData/loginTested=true')
        print "Login with Valid details"
        print "Successfully Logged in with Valid details"
        sleep(.5)
    return



def TheRestOfAppFunctionality() :
    print( "TheRestOfAppFunctionality" )
    return



gw_url = 'http://localhost:8887/graphwalker'

try:
    while requests.get(gw_url+'/hasNext').json()['hasNext'] == 'true' :
        result_dump = True
        # Get next step from GraphWalker
        step = requests.get(gw_url+'/getNext').json()['currentElementName']
        if step != '' :
            eval( step + "()" )
    else:
        if result_dump:
            result = requests.get(gw_url + '/getStatistics').json()
            if result:
                file_path = os.path.join(os.getcwd(), "result") + "/result.json"
                with open(file_path, 'w') as obj:
                    json.dump(result, obj)
                    print "Result has been dumped"
finally:
    pass
