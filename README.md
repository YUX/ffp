![](https://img.shields.io/badge/language-python-blue.svg) ![](https://img.shields.io/docker/pulls/yuxio/ffp.svg)

# ffp
**yet another Flask File Proxy**

### RECOMMENDED

**make sure you have**

- docker, `docker --version`
- Domain name
- ssl
- Nginx (or anything you can point your domain to local port 502)

### INSTALLATION

1. install **ffp** via docker 

```shell

docker run -d --name=ffp \

  -p 127.0.0.1:502:80 \

  --restart=always \

  yuxio/ffp:latest

```

2. Point your domain or subdomain to local `502` port. (reverse proxy)

3. Get the HTTPS work

### USAGE

1. **File Proxy**
   - Rewrite `https://github.com/YUX-IO/ffp/blob/master/README.md` to `https://your.domain.here/https://github.com/YUX-IO/ffp/blob/master/README.md`
   - Now you get the file passed through the proxy.

2. **Rewritten Script Proxy**          *please note `/r/` in the url*
   - Rewrite `https://github.com/YUX-IO/ffp/blob/master/README.md` to `https://your.domain.here/r/https://github.com/YUX-IO/ffp/blob/master/README.md`
   - This will replace all the URL in the script to `https://your.domain.here/URL`, which means you'd get all the resources passing through your proxy.

### OTHER

1. If you don't have a domain, use `docker run -d --name=ffp -p 80:80 yuxio/ffp:latest`, then rewrite `https://github.com/YUX-IO/ffp/blob/master/README.md` to `http://$IP/https://github.com/YUX-IO/ffp/blob/master/README.md`, it should work just fine. But you can't use **Rewritten Script Proxy**.
2. If you don't want to use docker, clone this repository then run `pip install -r requirements.txt && python main.py --host=0.0.0.0 --port=$PORT`, choose the port you want. Rewrite `https://github.com/YUX-IO/ffp/blob/master/README.md` to `http://$IP:$PORT/https://github.com/YUX-IO/ffp/blob/master/README.md`.

# ffp
**使用Flask制作的文件代理**

### 推荐食用方法

**确保你有**

- docker环境, 通过`docker --version`查看。
- 域名
- ssl证书
- Nginx，或者其他帮助你反代绑定域名的工具

### 安装

1. 通过docker部署**ffp**

```shell

docker run -d --name=ffp \

  -p 127.0.0.1:502:80 \

  --restart=always \

  yuxio/ffp:latest

```
没有报错的话，此时**ffp**就部署成功了，监听本地的502端口。

2. 将你的域名，或者子域名绑定到本地的502端口。

3. 部署你的HTTPS。

### 用法

1. **文件代理**
   - 把你想要获取的文件地址前加上你的域名，例如，将 `https://github.com/YUX-IO/ffp/blob/master/README.md` 改成 `https://your.domain.here/https://github.com/YUX-IO/ffp/blob/master/README.md`
   - 这样这个`README.md`文件就会通过**ffp**代理，即时文件的原地址在你目前所处的网络环境下无法访问，也可以通过**ffp**正常查看。
  