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

| Parameter | Type    | Choices     | Description                                                             |
|-----------|---------|-------------|-------------------------------------------------------------------------|
| id        | integer |             | The unique ID of the object                                             |
| name      | string  |             | Name of the alarm                                                       |
| monday    | boolean | true, false | If set, the alarm will be triggered every monday at the selected time   |
| tuesday   | boolean | true, false | If set, the alarm will be triggered every tuesday at the selected time  |
| wednesday | boolean | true, false | If set, the alarm will be triggered every wednesdayat the selected time |
| thursday  | boolean | true, false | If set, the alarm will be triggered every thursdayat the selected time  |
| friday    | boolean | true, false | If set, the alarm will be triggered every friday at the selected time   |
| saturday  | boolean | true, false | If set, the alarm will be triggered every saturdayat the selected time  |
| sunday    | boolean | true, false | If set, the alarm will be triggered every sunday at the selected time   |
| hour      | integer |             | Hour when the alarm will be scheduled. Must be in range [0:23]          |
| minute    | integer |             | Minute when the alarm will be scheduled. Must be in range [0:59]        |
| is_active | boolean | true, false | If set, the alarm is active. Else the alarm is disabled.                |
| webradio  | integer |             | WebRadio object                                                         |

### **GET** /alarms/
Get a list all available alarms.

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
        "monday": false,
        "tuesday": false,
        "wednesday": false,
        "thursday": false,
        "friday": false,
        "saturday": true,
        "sunday": true,
        "hour": 10,
        "minute": 30,
        "is_active": false,
        "webradio": 5
    },
    {
        "id": 4,
        "name": "work",
        "monday": true,
        "tuesday": true,
        "wednesday": true,
        "thursday": true,
        "friday": true,
        "saturday": false,
        "sunday": false,
        "hour": 7,
        "minute": 30,
        "is_active": true,
        "webradio": 4
    }
]
```

### **GET** /alarms/{alarmclock_id}
Get a details about an alarm by its ID.

#### Example call
```
curl -X GET http://127.0.0.1:8000/alarms/3
```

#### Example answer
```
{
    "id": 3,
    "name": "test",
    "monday": true,
    "tuesday": false,
    "wednesday": false,
    "thursday": false,
    "friday": false,
    "saturday": false,
    "sunday": false,
    "hour": 12,
    "minute": 12,
    "is_active": false,
    "webradio": 5
}
```

### **DELETE** /alarms/{alarmclock_id}
Delete an alarm

#### Example call
```
curl -H "Content-Type: application/json" -X DELETE http://127.0.0.1:8000/alarms/3/
```


### **POST** /alarms/
Create a new alarm.

#### Example call
```
curl -H "Content-Type: application/json" -X POST -d '{"name": "work", "monday": true, "tuesday": true, "wednesday": true, "thursday": true, "friday": true, "saturday": true, "sunday": true, "hour": 7, "minute": 30, "is_active": true, "webradio": 5}' http://127.0.0.1:8000/alarm/
```

#### Example answer
```
{
	"id": 7,
	"name": "work",
	"monday": true,
	"tuesday": true,
	"wednesday": true,
	"thursday": true,
	"friday": true,
	"saturday": true,
	"sunday": true,
	"hour": 7,
	"minute": 30,
	"is_active": true,
	"webradio": 5
}
```

### **PUT** /alarms/{alarmclock_id}
Update an alarm.

#### Example call
```
curl -H "Content-Type: application/json" -X PUT -d '{"name": "renamed", "monday": true, "tuesday": true, "wednesday": true, "thursday": true, "friday": true, "saturday": true, "sunday": true, "hour": 7, "minute": 30, "is_active": true, "webradio": 5}' http://127.0.0.1:8000/alarms/7/
```

#### Example answer
```
{
	"id": 7,
	"name": "work",
	"monday": true,
	"tuesday": true,
	"wednesday": true,
	"thursday": true,
	"friday": true,
	"saturday": true,
	"sunday": true,
	"hour": 7,
	"minute": 30,
	"is_active": true,
	"webradio": 5
}
```

## Player management

**Model detail**

| Parameter | Type    | Choices | Description                                                                             |
|-----------|---------|---------|-----------------------------------------------------------------------------------------|
| status    | string  | on, off | Start or stop the player.                                                               |
| webradio  | integer |         | Primary key of the WebRadio object to start. If not set, the efault webradio is started |

> **Note**. The web radio field is not required. When switching the status to "on", if a no web radio is set, the default one is launched.

### **Get** /player
Get the status on the player. If Mplayer is running, the status is "on". Else the status is "off"

#### Example call
```
curl -X GET http://127.0.0.1:8000/player/
```

#### Example answer
```
{
    "status":"off"
}
```

## Backup MP3 management

**Model detail**

| Parameter   | Type | Choices | Description                                                              |
|-------------|------|---------|--------------------------------------------------------------------------|
| backup_file | file |         | The MP3 backup file that will be lanched id the web radio doesn't answer |

### **Get** /backup
Get the name of the current backup MP3 file.

#### Example call
```
curl -X GET http://127.0.0.1:8000/backup/
```

#### Example answer
```
{
    "id": 1,
    "backup_file": "backup.mp3"
}
```

### **post** /backup
Send a new backup file. The new one will replace the last one if exist

#### Example call
```
curl -X POST -F "backup_file=@/home/nico/Desktop/backup.mp3" http://127.0.0.1:8000/backup
```

#### Example answer
```
{
    "backup_file":"backup_mp3/backup.mp3"
}
```
