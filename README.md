# Webshop API

To run this project execute the commands as in this readme described.




## Deployment

To deploy this project run

```bash
docker-compose build --no-cache
docker-compose up &
```

wait till these two commands have executed. Then run the following:
```bash
docker-compose exec django-service python manage.py collectstatic --noinput
docker-compose exec django-service python manage.py migrate
docker-compose exec django-service python manage.py test
```

This will run the DB migrations and run the tests.

Then load the fixtures:
```bash
docker-compose exec django-service python manage.py loaddata fixtures/webshop_data.json
```

Then you can test it: 
http://0.0.0.0:5000

## Documentation

Documentation is on the following link, you need to run the app (steps above) :
http://0.0.0.0:5000/swagger/

   
