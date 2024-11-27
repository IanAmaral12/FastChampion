Modelo entregável do projeto de Engenharia de Software

1 - Instalar Python e configurar a pasta de instalação ao PATH das Variáveis de Ambiente

No powershell ou cmd, na pasta do diretório, execute: 

2 - Iniciar o Ambiente virtual(Se estiver usando Linux, troque python por python3): 
venv\Scripts\Activate

3 - Instalar o Django:
pip install django

4 - Carregar Migrações: 
python manage.py makemigrations
python manage.py migrate

5  - Iniciar Servidor:
python manage.py runserver
