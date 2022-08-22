## Session 

* AWS Elasic cache for Redis
``` bash
export REDIS_URL=REDIS_ENDPOINT
```

* Python Code (Sample)

``` python
import os
import redis

url = os.environ.get('REDIS_URL')

client = redis.Redis.from_url('redis://' + url)
client.ping()
```

* result
``` bash
True
```