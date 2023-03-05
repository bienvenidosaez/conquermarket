# Para generar la imagen custom

docker build --no-cache -f dockerfiles/Dockerfile.dev -t 'bienvenidosaez/marketplace_django_base_dev:latest' .

# Para añadir a los Dockerfiles y que cojan la imagen base

FROM bienvenidosaez/marketplace_django_base_dev:latest

# Para generar la imagen custom

docker build --no-cache -f dockerfiles/Dockerfile.prod -t 'bienvenidosaez/marketplace_django_base_prod:latest' .

# Para añadir a los Dockerfiles y que cojan la imagen base

FROM bienvenidosaez/marketplace_django_base_prod:latest

pass cRsuD20r0zVI
