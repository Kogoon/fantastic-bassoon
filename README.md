# fantastic-bassoon
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

