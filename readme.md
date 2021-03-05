### create venv
```shell
cd flask-vue-demo

python -m venv venv

[mac/linux]:
  source venv/bin/activate
  
[windows]:
  venv\Scripts\activate

```
### install requirements
```shell
pip install -r requirements.txt

```

### create log file
```shell
Create the Logs folder under the project directory and create the Log file
: /logs/log
```


### start project
```
mac/linux:
    start.sh
windows:
    start.bat
```

### create table
```
see doc/sql/db.sql and change.sql
```

---
### init web project
```shell script
cd web/vue-app
yarn install
```
### start web project
```shell
yarn serve

```
