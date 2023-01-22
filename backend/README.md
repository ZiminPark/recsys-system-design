# Redis
### Install Redis
https://redis.io/docs/getting-started/installation/

For Mac
```
brew install redis
```

### Start Redis
```
redis-server --port 6379
```

### Connect via CLI
```
redis-cli -h ${HOST} -p 6379
```

# MongoDB
### install
```
brew tap mongodb/brew
brew install mongodb-community
```

### Start/Stop MongoDB
```
brew services start mongodb-community 
brew services stop mongodb-community
```

### CLI
```
mongosh  # mongo shell
```