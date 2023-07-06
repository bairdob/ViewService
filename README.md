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


