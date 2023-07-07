# ViewService

Веб-сервис должен выдавать простую HTML обертку с изображением картинки

## Build 

```bash
$ docker compose build
$ docker compose up 
```

```bash
$ docker image build -t flask .
$ docker container run -p 8080:8080 flask    
```

## Query 

<details><summary>postman query collection</summary>
<p>

```json
{
	"info": {
		"_postman_id": "7c5bfb48-b13a-4c1c-b4b1-5b135edcadac",
		"name": "ViewService",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "image1",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8080/static/image1.jpg;500;flight;airlplane",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080",
					"path": [
						"static",
						"image1.jpg;500;flight;airlplane"
					]
				}
			},
			"response": []
		},
		{
			"name": "index",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8080",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080"
				}
			},
			"response": []
		},
		{
			"name": "index_with_categories",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8080/?category[]=auto&category[]=trains&category[]=airlplane&category[]=show&category[]=sandbox",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080",
					"path": [
						""
					],
					"query": [
						{
							"key": "category[]",
							"value": "auto"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "airlplane"
						},
						{
							"key": "category[]",
							"value": "show"
						},
						{
							"key": "category[]",
							"value": "sandbox"
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "index_too_much_categories",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://localhost:8080/?category[]=auto&category[]=trains&category[]=trains&category[]=trains&category[]=trains&category[]=trains&category[]=trains&category[]=trains&category[]=trains&category[]=trains&category[]=trains",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "8080",
					"path": [
						""
					],
					"query": [
						{
							"key": "category[]",
							"value": "auto"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						},
						{
							"key": "category[]",
							"value": "trains"
						}
					]
				}
			},
			"response": []
		}
	]
}
```
</p>
</details>


<details><summary>index</summary>
<p>

```bash
curl --request GET --url http://localhost:8080/
```

</p>
</details>

<details><summary>with categories</summary>
<p>

```bash
curl --request GET \
  --url 'http://localhost:8080/?category%5B%5D=auto&category%5B%5D=trains&category%5B%5D=airlplane&category%5B%5D=show&category%5B%5D=sandbox'
```
</p>
</details>

<details><summary>/static/[image_url];[show];[categories]</summary>
<p>

```bash
curl --request GET \
  --url 'http://localhost:8080/?category%5B%5D=auto&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains'
```

</p>
</details>

<details><summary>fail >10 categories</summary>
<p>

```bash
curl --request GET \
  --url 'http://localhost:8080/?category%5B%5D=auto&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains&category%5B%5D=trains'
```

</p>
</details>


## Limitations

> При запуске сервис считывает конфигурационный файл и начинает слушать HTTP обращения.

Считаем, что процесс не останавливается и по исчерпании необходимого количество показов картинок конфигурационного файла будет отдавать пустой ответ


