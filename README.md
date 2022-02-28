## CaseItau

### Para construir o ambiente é necessário o docker e docker-compose
~~~
dentro da raiz do projeto, executar os seguintes passos:
 - sudo docker-compose up -d
 - acessar http://127.0.0.1:8080/catapi/create para gerar dados no DB
 - o index está em http://127.0.0.1:8080/catapi/
~~~

### URL das APIs:
~~~
 - http://127.0.0.1:8080/catapi/create
 - http://127.0.0.1:8080/catapi/categoria/chapeu
 - http://127.0.0.1:8080/catapi/categoria/oculos
 - http://127.0.0.1:8080/catapi/todos
 - http://127.0.0.1:8080/catapi/raca/abys
 - http://127.0.0.1:8080/catapi/temperamento/loyal
 - http://127.0.0.1:8080/catapi/origem/egypt
 - http://127.0.0.1:8080/catapi/update/abys
~~~

### Coleção no Postman para consumo das APIs
~~~
 - caseita.postman_collection-v2.json
~~~

### Arquivo para importar objetos para o Elasticsearch (view, index)
~~~
Vá em Stack Management -> Saved Objects -> Import:
 - elasticsearch-views.ndjson
~~~

### URLs:
~~~
 - Kibana ->  http://127.0.0.1:5601/
 - Grafana -> http://127.0.0.1:3000/
    Grafana com user/paas admin/admin

 - View no Kibana -> http://127.0.0.1:5601/goto/98c32b2dd59f69642f844c33e2d09977
~~~

### Screenshots

![1](/screenshots/grafana-dashboard.png)
![2](/screenshots/kibana-nginx-logs.png)
![3](/screenshots/kibana-django-logs.png)

