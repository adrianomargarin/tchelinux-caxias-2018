# <README.md>

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.
6. Execute o runserver.

```console
git clone git@github.com:adrianomargarin/tchelinux-caxias-2018.git
cd tchelinux-caxias-2018
virtualenv env --python=python3 # python 3.6 ou mais atual
. env/bin/activate
pip install -r requirements_dev.txt
cp contrib/env-sample .env
coverage run --source='.' manage.py test --verbosity=1 && coverage report --show-missing
python manage.py runserver
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define um SECRET_KEY segura para instância.
4. Defina DEBUG=True
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create tchelinux-caxias-2018

heroku config:set ALLOWED_HOSTS=.herokuapp.com
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=TRUE

git push heroku master --force
```
