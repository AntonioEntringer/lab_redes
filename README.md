# lab_redes
Execução de um laboratório que envia arquivos entre maquinas distintas usando github

No diretório desejado faça download cliente na maquina que seja desejado enviar o arquivo 
Execute os comando para construir e executar o docker

docker build -t client .
docker run --network host client:latest

No diretório desejado faça download server na maquina que seja desejado receber o arquivo 
Execute os comando para construir e executar o docker

docker build -t server .
docker run -it --network host -v /root/receber:/root/receber server:latest

<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
Imagens disponiveis no dockerhub por meio de:

docker pull antonioentringer/client:latest
docker pull antonioentringer/server:latest

