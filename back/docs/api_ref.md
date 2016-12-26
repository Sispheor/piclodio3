# API reference

## WebRadio management

**Model detail**

| Parameter  | Type    | Choices     | Description                                                                                                                                           |
|------------|---------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| id         | integer |             | The unique ID of the object                                                                                                                           |
| name       | string  |             | Name of the web radio                                                                                                                                 |
| url        | string  |             | URL of the stream of the web radio                                                                                                                    |
| is_default | boolean | true, false | The web radio which started when the /play URL is called. Only one webradio can be the default one. The last started web radio become the default one |


### **GET** /webradio/
Get a list all available web radio.

#### Example call
```
curl -X GET http://127.0.0.1:8000/webradio/
```

#### Example answer
```
[{
	"id": 1,
	"name": "my favorite web radio",
	"url": "http://domain.example.com",
	"is_default": true
}, {
	"id": 2,
	"name": "Piclodio Rock",
	"url": "http://domain.example.com",
	"is_default": false
}]
```

### **GET** /webradio/{webradio_id}
Get details about a web radio.

#### Example call
```
curl -X GET http://127.0.0.1:8000/webradio/1
```

#### Example answer
```
{
	"id": 1,
	"name": "my favorite web radio",
	"url": "http://domain.example.com",
	"is_default": true
}
```

### **POST** /webradio/
Create a web radio.

#### Example call
```
curl -H "Content-Type: application/json" -X POST -d '{"name": "my name", "url": "http://mydomain.example.com", "is_default": "false"}' http://127.0.0.1:8000/webradio/
```

#### Example answer
```
{
	"id": 5,
	"name": "my name",
	"url": "http://mydomain.example.com",
	"is_default": false
}
```

### **DELETE** /webradio/{webradio_id}
Delete a web radio.

#### Example call
```
curl -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/webradio/3/
```

### **PUT** /webradio/{webradio_id}
Update a web radio.

#### Example call
```
curl -H "Content-Type: application/json" -X PUT -d  '{"id": 4, "name": "new name", "url": "http://mydomain.example.com", "is_default": "true"}' http://127.0.0.1:8000/webradio/4/
```

#### Example answer
```
{
	"id": 4,
	"name": "new name",
	"url": "http://mydomain.example.com",
	"is_default": false
}
```

## Alarms management

**Model detail**

| Parameter | Type      | Choices | Description                                                      |
|-----------|-----------|---------|------------------------------------------------------------------|
| id        | integer   |         | The unique ID of the object                                      |
| name      | string    |         | Name of the alarm                                                |
| dayofweek | DayOfWeek |         | DayOfWeek object                                                 |
| hour      | integer   |         | Hour when the alarm will be scheduled. Must be in range [0:23]   |
| minute    | integer   |         | Minute when the alarm will be scheduled. Must be in range [0:59] |
| is_active | boolean   |         | If set, the alarm is active. Else the alarm is disabled.         |
| webradio  | integer   |         | WebRadio object                                                  |

### **GET** /alarms/
Get a list all available web radio.

#### Example call
```
curl -X GET http://127.0.0.1:8000/alarms/
```

#### Example answer
```
[
    {
        "id": 3,
        "name": "week end",
        "dayofweek": {
            "monday": false,
            "tuesday": false,
            "wednesday": false,
            "thursday": false,
            "friday": false,
            "saturday": true,
            "sunday": true
        },
        "hour": 10,
        "minute": 30,
        "is_active": false,
        "webradio": {
            "id": 5,
            "name": "my name",
            "url": "http://mydomain.example.com",
            "is_default": false
        }
    },
    {
        "id": 4,
        "name": "work",
        "dayofweek": {
            "monday": true,
            "tuesday": true,
            "wednesday": true,
            "thursday": true,
            "friday": true,
            "saturday": false,
            "sunday": false
        },
        "hour": 7,
        "minute": 30,
        "is_active": true,
        "webradio": {
            "id": 4,
            "name": "new name",
            "url": "http://mydomain.example.com",
            "is_default": false
        }
    }
]
```