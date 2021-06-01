##　使用Docker建構flask服務(uwsgi + nginx + mysql)



大致環境

> * Python 3.7.10
> * uWSGI 2.0.18
> * Flask 1.1.0
> * Ngnix 1.19.5
> * MySQL 8.0.23
> * Docker Engine release 19.03.0+ <font color="red">以上只是敘述環境，這個一定要安裝</font> [版本可參考](https://docs.docker.com/compose/compose-file/)
>   * 註 : windows環境，建議使用wsl2
> * Git



建立服務

```sh
git clone git@github.com:chouqimin/flask-docker.git

cd flask-docker

docker-compose up -d
```

註 : 通常`.env`檔案不會跟著commit進git裡，會放在`.gitignore`忽略掉，這邊為了試範先不拿掉



## 範例

首頁

![首頁](https://raw.githubusercontent.com/chouqimin/flask-docker/main/sample_img/home.JPG)

---

首頁 代入參數 name

![首頁代參數name](https://raw.githubusercontent.com/chouqimin/flask-docker/main/sample_img/home_use_parameter.JPG)

---

## RESTful API

post(新增)

![post(新增)](https://raw.githubusercontent.com/chouqimin/flask-docker/main/sample_img/task_post_method.JPG)

---

get(查詢)

![get(查詢)](https://raw.githubusercontent.com/chouqimin/flask-docker/main/sample_img/task_get_method.JPG)

---

put(更新)

![put(更新)](https://raw.githubusercontent.com/chouqimin/flask-docker/main/sample_img/task_put_method.JPG)

---

delete(刪除)

![delete(刪除)](https://raw.githubusercontent.com/chouqimin/flask-docker/main/sample_img/task_delete_method.JPG)

