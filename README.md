# MBT_GraphWalker_Python
GraphWalker is an open source Model-based testing tool for test automation. It's designed to make it easy to design your tests using graphs see http://graphwalker.github.io

# Introduction
Here explored GraphWalker tool using python but some limitations with GraphWalker using Python :  
We can implement GW using python only in RESTFUL service i.e. This service only handle one session at a time see http://graphwalker.github.io/rest-overview/ . Test cases are generated in online mode and so we can run only one model file at a time.
For Rest API see http://graphwalker.github.io/rest-overview/#command-line-example 

What GraphWalker does not do (see http://graphwalker.github.io/features/#what-graphwalker-does-not-do) 

1. Test case execution (Selenium webdriver for web and Appium for Mobile platform )

2. Graph Editing (yED open source tool)see https://www.yworks.com/products/yed

# Quickstart

Download GW standalone server see http://graphwalker.github.io/download/ we are used GW version 3.4 or http://graphwalker.github.io/content/archive/graphwalker-cli-3.4.2.jar

Create shortcut for GW standalone server see http://graphwalker.github.io/cli-overview/#creating-a-script-facilitating-command-line-handling-on-a-linux-machine

Install virtualenv via pip:

On Terminal 1 : 

$ pip install virtualenv

$ virtualenv env_name

$ source ~/env_name/bin/activate

(env_name) xxx $ pip install -r requirements.txt

Set PYTHONPATH 

(env_name) xxx $ export PYTHONPATH=`pwd`

On Terminal 2 : Start Graphwalker server

 $ gw3 --debug all online  --service RESTFUL -m  ~/resources/LoginParametrize/LoginParametrized.graphml “random(edge_coverage(100))”

On Terminal 1 : Run model file

(env_name) xxx $ python ~/tests/LoginParametrizedDemo.py 

For test result:

For Test result we are used GW getstat see http://graphwalker.github.io/rest-getstatistics/
(see http://graphwalker.github.io/cli-source/#examples)

# Design your own model

1. Using Graph Editing (yED open source tool)see https://www.yworks.com/products/yed and http://graphwalker.github.io/Model_design/

2. Verify model see http://graphwalker.github.io/cli-check/#check:

   $ gw3 check -m ~/resources/LoginParametrize/LoginParametrized.graphml "random(edge_coverage(10))"

   It will prompt : No issues found with the model(s) if model is correct.

3. Generate source code see http://graphwalker.github.io/cli-source/#examples:

   $ gw3 source -i model_name.graphml python.template >> model_name.py

   It will create python source code file with name model_name.py : Functions as per designed Edges and Vertices as per  
   provided nomenclature for understanding, we are added prefix e_ and v_ before edges/vertices names 

4. Start GraphWalker server see http://graphwalker.github.io/rest-overview/#command-line-example

5. Run model file and 

6. Fetch result stats see http://graphwalker.github.io/rest-getstatistics/#getstatistics 

# For parameterization : 

If you need to access or change data in the model, we can use the REST calls getData and setData. See http://graphwalker.github.io/rest-getdata/#getData and http://graphwalker.github.io/rest-setdata  # /#setData and http://graphwalker.github.io/tests_parametrisation/
Here we are used GW gaurd feature.

# Multiple models:

We Are you using REST, http://graphwalker.github.io/rest-overview/,  when running the tests? If so, start, the graphwalker rest service with --verbose or -o options.

 $ gw3 -d all online -s RESTFUL -o -m m1.graphml "random(edge_coverage(100))" -m m2.graphml "random(edge_coverage(100))"

It will output the model name as well as the element name for every getNext request. The model name will represent the class in which you'll find the method (element) to call.

If you have one python script/program, and edges and vertices that happen to share the same name between the models, your script will run the same code for them.
 (see http://graphwalker.github.io/yed_model_syntax/#multiple-models)

# How to find out which test case fails?

From a given set of graphs, generators and stop conditions, GraphWalker will generate a path through the graphs and
The path represents your test, or test case that means : If any path will fail then test case will failed.
see http://graphwalker.github.io/features/#path-generation


# Can i generate a list of test cases or count of test cases?

We can generate test cases offline using

 $ gw3 offline  --model model_name.graphml "random(edge_coverage(100))"

# GraphWalker tool is provided GraphWalker Studio 
see https://github.com/GraphWalker/graphwalker-project/tree/master/graphwalker-studio

Simple steps to start GraphWalker studio:
See http://graphwalker.github.io/download/#standalone-jar and Download the jar "Latest development standalone Studio - 4.0.0-SNAPSHOT" and 

1. Start on terminal java -jar "Latest development standalone Studio - 4.0.0-SNAPSHOT.jar",

2. Open http://localhost:9090/ in browser, it's run default port 9090 and you can see the GraphWalker studio GUI. 

Currently, We can use GraphWalker Studio as: 

1. Verify designed model file(.graphml)

2. Graphical representation of path generation 

3. Able to see, how the paths are generated while run the test cases

4. Save test case as Json format and run this file next time

5. Set and execute available generator methods on model file

6. Design model
