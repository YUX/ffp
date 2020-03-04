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

  yuxio/ffp:latest

```

1. Point your domain or subdomain to local `502` port. (reverse proxy)

2. Get the HTTPS work

### USAGE

1. **File Proxy**
   - Rewrite `https://github.com/YUX-IO/ffp/blob/master/README.md` to `https://your.domain.here/https://github.com/YUX-IO/ffp/blob/master/README.md`
   - Now you get the file passed through the proxy.

2. **Rewritten Script Proxy**          --*please note `/r/` in the url*
   - Rewrite `https://github.com/YUX-IO/ffp/blob/master/README.md` to `https://your.domain.here/r/https://github.com/YUX-IO/ffp/blob/master/README.md`
   - This will replace all the URL in the script to `https://your.domain.here/URL`, which means you'd get all the resources passing through your proxy.

### OTHER

1. If you don't have a domain, use `docker run -d --name=ffp -p 80:80 yuxio/ffp:latest`, then rewrite `https://github.com/YUX-IO/ffp/blob/master/README.md` to `http://$IP/https://github.com/YUX-IO/ffp/blob/master/README.md`, it should work just fine. But you can't use **Rewritten Script Proxy**.
2. If you don't want to use docker, clone this repository then run `pip install -r requirements.txt && python main.py --host=0.0.0.0 --port=$PORT`, choose the port you want. Rewrite `https://github.com/YUX-IO/ffp/blob/master/README.md` to `http://$IP:$PORT/https://github.com/YUX-IO/ffp/blob/master/README.md`.
