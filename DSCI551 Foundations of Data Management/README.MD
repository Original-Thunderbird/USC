# DSCI-551
Techs about data querying, data management and data processing. For items not detailed with running steps, refer to .docx for requirements and steps.
<table>
  <tr>
    <td><a href="#HW1">hw1: Firebase CRUD</a></td>
    <td><a href="#HW2">hw2: XML processing</a></td>
  </tr>
  <tr>
    <td>hw3: SQL</td>
    <td>hw4: B+ tree; SQL join algorithm</td>
  </tr>
  <tr>
    <td>hw5: SQL-to-MapReduce translation; Spart Dataframe; Spark RDD</td>
  </tr>
  <tr>
    <td>lab1: HW env config</td>
    <td>lab2: HDFS structure and image</td>
  </tr>
  <tr>
    <td>lab3: MongoDB query</td>
    <td>lab4: DynamoDB; json processing</td>
  </tr>
</table>

<a id="HW1"></a>
## DSCI-551.HW1
Firebase CRUD
### 1. Getting Started
environment
```
python -m venv car
source car/bin/activate
pip install -r requirements.txt
```
Create a Google Firebase realtime project.

load csv to firebase:
```
python3 load.py cars.csv
```
You can see Firebase content appeared immediately.

takes a range of price (in two arguments) and outputs IDs of cars in the range (inclusive)
```
python3 search_price.py (number) (number)
```
results will be given in terminal.

creates a keyword index for keywords appearing in car name.
```
python3 create_index.py cars.csv
```
results are in the inv_ind doc in Firebase.

Search cars by keyword
```
python3 search_car.py “honda accord”
```
results will be given in terminal.


### 2. Technologies
Firebase, json, python


### 3. Result
result screenshot of load.py/create_index.py are task1_screenshot.png/task3_screenshot.png


<a id="HW3"></a>
## DSCI-551.HW2
takes an XML file of HDFS file system image and convert it to TSV format.
### 1. Getting Started
```
python -m venv qxml
source qxml/bin/activate
pip install -r requirements.txt
python3 xml2tsv.py (xml file name) (tsv file name)
```
fsimage04.xml and fsimage70.xml are available example input files.


### 2. Technologies
python, XML



## Proj: Web-App simulation of HDFS
Simulate HDFS structure with 2 different DB implementations (SQL & Firebase in our choice), and provide a web app interface.

Commands that the system support: mkdir; ls; cat; rm; put; getPartitionLocations(file); readPartition(file, partition#).

Implemented partition-based map and reduce (PMR): mapping on each simulated dataNode, reducing on result from each. Result in intermediate steps are provided.

See [project guideline](proj/docs/project%20guideline.pdf) for detailed requirements.

**See codebase [here](https://github.com/Original-Thunderbird/551proj)**.

### 1. Getting Started
You need npm, node.js and MySQL workbench on your machine; a Firebase Real-Time project opened. Configure MySQL connection and Firebase url in server/config.js

environment installation:
```
cd server
npm install
cd ../client
npm install
```

start server:
```
cd server
node index.js
```

start client: open another terminal,
```
cd client
npm start
```

### 2. Technologies
JavaScript, SQL, Firebase, json, Node.js, React.js


### 3. Result
[report with test on each functionalities](proj/docs/FinalReport.pdf), [screencast with explanation of the interface and demo](https://youtu.be/pgpFmHx2yVI)
