TOUTORIAL PARA GERAR O .APK COM MÁQUINA VIRTUAL DO GOOGLE:

1- [Link para os comandos da máquina virtual](https://colab.research.google.com/drive/16wji2BWd5HHlp7eNqBBcZONCxxCzV-jy?usp=sharing)
2- Upar o main.py, criar uma pasta chamada "images" e colocar as imagens dentro (não é possível upar a pasta inteira) 
3- Executar os comandos linha a linha

Obs.: o comando: "buildozer -v android debug" demora bastante, tipo uns 30 minutos

Ao final será gerado um .APK na pasta bin:

1- Baixar o .APK (demora uns 5 minutos)
2- Instalar o Android Studio (pois ele vem com o adb)
3- Adicionar o adb no PATH de variáveis do sistema
4- Habilitar o modo desenvolvedor do celular (varia de celular pra celular)
5- Habilitar depuração USB no celular
6- Conectar o celular via usb no PC
7- Abrir o CMD e navegar até o diretório do .APK
8- Executar "adb devices" para ver os aparelhos conectados
9- Executar "adb install -r nome-do-APK.apk"
10- o APP deve estar instalado no celular

