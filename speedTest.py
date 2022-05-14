import speedtest

t = speedtest.Speedtest()

t.get_servers();

b = t.get_best_server();

dr = t.download();
print(dr / 1024 / 1024);

ur = t.upload();
print(ur / 1024 / 1024);