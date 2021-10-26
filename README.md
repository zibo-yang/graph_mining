# Graph Mining Algorithm

This is my personal project for MPRI 2.29.2 graph mining. My goal is to program the algorithm to find the densest subgraph in specific large graph.

Sorry for the inconvenience of usage of this repository since the refinement of makefile and coding comment are restricted by lack of time. I will try my best to optimize its usage as soon as I could and update it on my github account. Please stay tuned on git and send email to zibo.yang@ip-paris.fr if there is any doubt.

## Dependency
Please install python3, pip and matplotlib first

## Usage
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

Although there are plenty of examples in ./stu-master and ./network-example, the authur didn't feed them into algorithms since inappropriate
reading setting based on previous biases of number as the only type of input data. However, it doesn't affect the correctness of our algorithms. The authur takes advantage of the generated complete graph(n-clique) which serves to validate the time-complexity plot, which shares no influence for our conclusion for the complete graph as the worst cases to find densest graph. To verify the correctness of algorithms:
```bash
python3 algo1.py
python3 algo2.py
```
where the graphs to feed come from our class slides and are very unusual to produce, which shows the correctness of algorithms. 
