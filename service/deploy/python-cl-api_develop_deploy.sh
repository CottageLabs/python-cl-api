sudo ln -sf /home/cloo/python-cl-api/src/python-cl-api/service/deploy/python-cl-api-dev.conf /etc/supervisor/conf.d/python-cl-api-dev.conf

sudo ln -sf /home/cloo/python-cl-api/src/python-cl-api/service/deploy/pythonclapi-nginx /etc/nginx/sites-available/pythonclapi-nginx
sudo ln -sf /etc/nginx/sites-available/pythonclapi-nginx /etc/nginx/sites-enabled/pythonclapi-nginx

sudo apt-get update -q -y
sudo apt-get -q -y install libxml2-dev libxslt-dev python-dev lib32z1-dev

cd /home/cloo/python-cl-api/
. bin/activate
cd src/python-cl-api
git checkout develop
git pull
git submodule update --recursive --init
git submodule update --recursive

cd esprit
pip install -e .
cd ..

cd magnificent-octopus
pip install -e .
cd ..

pip install -e .

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart python-cl-api-dev
sudo nginx -t && sudo nginx -s reload
