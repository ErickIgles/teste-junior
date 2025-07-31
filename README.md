SOFTWARE PARA GERENCIAR OS ABASTECIMENTOS E TANQUES DE COMBUSTÍVEIS



### Passos para rodar

1. Clone este repositório:
    git clone https://github.com/ErickIgles/teste-junior.git

2 entre no repositorio:
    cd teste-junior

2 crie um ambiente virtual
    python -m venv venv

3 ative o ambiente virtual
    venv\Scripts\activate     # Windows

4 Instale as dependências:
    pip install -r requirements.txt

5 Execute as migrations
    python manage.py migrate

6 Crie um superusuário (para acessar o admin):
    python manage.py createsuperuser

7 Rode o servidor de desenvolvimento:
    python manage.py runserver

8 Acesse no navegador:

    http://127.0.0.1:8000/

9 Acesse o adminitração

    http://127.0.0.1:8000/

10 Acesse o modelo de Exibição Tanque e realize o cadastro
11 Acesse o modelo de Exibição Bomba e realize o cadastro

12 retorne a url inicial
    http://127.0.0.1:8000/

13 acesse o botão 'Registar abastecimento' no canto superior

14 Escolha a Bomba que foi abastecida informe a quantidade abastecida e o valor, e aperte em registrar

15 Após o cadastro há um retorno automatico para a tela inicial e apresentára o seu registro de abastecimento.
