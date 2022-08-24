# fantastic-bassoon (Memo)
Final Project


## Generate a secret key 

``` python
import os 
print(os.urandom(16))
```


## Authentication vs Authorization
* Authentication  : 인증 (로그인)
* Authorization   : 권한 부여 (로그인 상태 유지)


## Password 처리 
``` python
>>> from werkzeug.security import generate_password_hash, check_password_hash
>>> hash = generate_password_hash('1q2w3e4r')
>>> print(hash)
pbkdf2:sha256:260000$dIxGHqZOxEWiXscv$d4965051b2b2b41160932f8cbba873e85e9674d1684902b0028dfd6759550488
>>> check_password_hash(hash, '1q2w3e4r!')
False
>>> check_password_hash(hash, '1q2w3e4r')
True
```


## Generate SECRET KEY
``` bash
$ python -c 'import secrets; print(secrets.token_hex())'
'192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
```

## pip 
* mysql_client error
``` bash
$ sudo yum install -y python3-devel mysql-devel
```


## flask db
``` bash 
flask db init
flask db migrate
flask db upgrade
```


## mysql 
``` text
# mysql://<username>:<password>@<host>:<port>/<db_name>
engine = create_engine('mysql://username:password@your_host/your_dbname')
```