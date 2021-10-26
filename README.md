This is my personal project for MPRI 2.29.2 graph mining. My goal is to program the algorithm to find the densest subgraph in specific large graph.

Sorry for the inconvenience of usage of this repository since the refinement of makefile and coding comment are restricted by lack of time. I will try my best to optimize its usage as soon as I could and update it on my github account. Please stay tuned on git and send email to zibo.yang@ip-paris.fr if there is any doubt.

##Dependency
Please install python3, pip and matplotlib first

##Usage
There are two different finding algorithms in this repository. To introduce the content of important files:

basic_funcitons.py: the basic elements of our algorithms which yields enough functionality.
algo1.py: finding densest subgraph by defining density as clique density
algo2.py: finding densest subgraph by defining density as average density
finding.py: generating n-clique graph and making plot of time complexity analysis through n-clique graph

advanced_basic_functions.py: Another advanced but complicated algorithm to find densest graph and make time-size plot

To check first algorithm:
```bash
cd src
python3 finding.py
```
(which produces the figure: time_complexity_analysis.png which clearly demonstrates exponential complexity and results in programming advanced_basic_function.py)

To check advanced algorithm:
```bash
cd src
python3 advanced_basic_functions.py
```
(which produces the figure: time_complexity_analysis2.png)
