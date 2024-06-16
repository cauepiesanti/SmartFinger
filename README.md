.apk:


https://colab.research.google.com/drive/16wji2BWd5HHlp7eNqBBcZONCxxCzV-jy?usp=sharing#scrollTo=EOQ0JSg7XC7g

adicionar comando:

!pip install flask pyserial requests adafruit-circuitpython-fingerprint adafruit-blinka

alterar requirements na linha 40:

requirements = python3,kivy,flask,pyserial,requests,adafruit-circuitpython-fingerprint,adafruit-blinka

descomentar linha 98:

android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)
