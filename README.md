# Desafio Geofusion

## Autor

Marcio de Lima

## Instalação

Este projeto está em running no HEROKU, desta forma, para seu uso basta chamar a REST API no endpoint abaixo ou acessar a página inicial que contém um HTML para testar a API e pegar o retorno em json. 

## Links: 

Serviço direto: https://desafiogeofusion.herokuapp.com/predict/lat=????&lng=????

Exemplo: https://desafiogeofusion.herokuapp.com/predict/lat=-22.8232257917&lng=-47.0758807513

Pagina de Teste: https://desafiogeofusion.herokuapp.com/

## Descrição

Este projeto destina-se a implantação de um modelo de ML como um serviço REST API. 

## Tecnologias

Esse projeto foi implementado em Python 3.7, FLASK, HTML e Jquery. O deploy foi efetuado no HEROKU.

## Considerações

O modelo foi treinado pelos scripts fornecidos pela GeoFusion, mas seu maior valor no dataset era no máximo R$ 17050.705936673578, sendo impossível o modelo preditivo alcançar os valores de 96040.6114295958 e 78410.6259787695 servidos como exemplo. Além disso, o retorno de numero de concorrentes como float não faz sentido, mas foi feito conforme o pedido via serviço, no HTML, esses valores aparecem como inteiros. 


