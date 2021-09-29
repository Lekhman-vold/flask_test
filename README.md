`Change variables POSTGRES_DB POSTGRES_USER POSTGRES_PASSWORD`

app/__init__.py
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/db_name'

docker-compose.yml 
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      
`Run project`

docker-compose up --build
