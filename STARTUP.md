1.坑1, 容器起来后会有报错但是不影响, 正常使用http://<Your IP Address>:8080/vnc.html 进行扫码登录
2.坑2, 有python但是没有pip工具, 需要下载get-pip.py, 然后
```bash
# 下载
wget https://bootstrap.pypa.io/get-pip.py
# 安装pip
python3 get-pip.py
```
3.坑3 需要安装依赖库
```bash
python3 -m pip install -r ./wesdk/requirements.txt
```

4.坑4 api解析过时, 无法从消息中取出自己的昵称和wxid, 需要注释代码
