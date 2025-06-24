
1. Abra o terminal e entre no SQLite
Navegue até o diretório onde está seu arquivo .db (por exemplo: app.db, database.db, etc).
```shell
cd /caminho/para/sua/database/
```
```shell
sqlite3 nome_do_arquivo.db
sqlite3 achiles.db
```


2. Verificar as tabelas da base:
```shell
.tables
```


3. Ver todos os registros de uma tabela ex: weight_records
```sql
SELECT * FROM weight_records;
```


4. Para sair do console
```shell
.quit
```