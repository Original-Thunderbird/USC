# CSCI572
## CSCI572.1 Search Engine Comparison
Search given queries (queries.txt) at Yahoo!, retrieve top 10 results. Use result from Google (google.json) as benchmark, determine overlap and correlation.

### 1. Getting Started
venv
```
python -m venv se
source se/bin/activate
pip install -r requirements.txt
```
run
```
python scrape.py
```
note: Yahoo! may block your visit temporaily, you may need to run multiple times to get results for all queries, each time starting from the query that first got blocked previously, and use a seperate json to accummulate results, as scrape.py overwrite hw1.json each run.

When finish,
```
python eval.py
```
to get hw1.csv.


### 2. Technologies
python, json


### 3. Result
hw1.csv (query-wise comparison), hw1.txt (analysis on hw1.csv)



## CSCI572.2 Crawling
### 1. Getting Started
venv for stats.py
```
python -m venv crawl
source crawl/bin/activate
pip install pandas
```
Install Eclipse Neon and crawler4j following guidance in docs/Crawler4jinstallation.pdf, **remember to use java 1.8 with crawler4j-4.1-jar-with-dependencies.jar** so that coude can work.

open src/ in eclipse, run. This takes around 1.5 hour to complete (but result from a previous run has been given as *.wsj.csv).

When finish, run stats.py, output will be CrawlReport_wsj.txt


### 2. Technologies
Java, crawler4j



## CSCI572.3 MapReduce on Google Cloud
Produce Inverted index of documents. Use Google Cloud dataproc, submit MR task as .jar


### 1. Getting Started
follow the 2 pdf


### 2. Technologies
Java, Google Clound Dataproc


### 3. Dataset
too large, contact dafu690127@gmail.com