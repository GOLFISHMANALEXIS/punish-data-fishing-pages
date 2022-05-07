import request
import threading

#urlnetworkdata
url = ''

data = {
  #todoelformdata
}


def do_request():
    while True:
      response = request.post(url, data=data).text
      print(response)

threads = []

for i in range(50):
       t = threading.Thread(target=do_request)
       t.daemon = True
       threads.append(t)

for i in range(50):
      threads[i].start()

for i in range(50):
      threads[i].join()

 
#cmd + python3 main.py
