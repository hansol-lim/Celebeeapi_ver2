# Celebee API
셀레비(*이름 변경 예정*) 어플리케이션의 api 서버입니다.


## Create Virtual Environment
---
```
# 가상환경 생성
$ python3 -m venv venv

# 가상환경 실행
$ source venv/bin/activate

# 관련 라이브러리 설치
(venv) $ pip install -r requirements.txt
```

## Execute Flask App
---
```
# .env 설정 없을 시
$ export FLASK_APP=beamme.py
$ export FLASK_ENV=development

# flask 실행
(venv) $ flask run
```
## Data Schema
---

### User
```
{
    _id:
    uid:
    email:
    token:
    nickname:
    photo:
}
```

### Idol
```
{
    _id:
    idol_name:
}
```

### Schedule
```
{
    _id:
    date:
    regi_time:
    sc_name:
    sc_info:
    idol_id:
}
```

### Post
```
{
    _id:
    body:
    time:
    user_id:
    post_list_id:
}
```

### PostList
```
{
    _id:
    post_type_num:
    title_name:
}
```

### Comment
```
{
    _id:
    body:
    time:
    post_id:
    schedule_id:
    news_feed_id:
    video_feed_id:
    newstab_id:
    user_id:
}
```

###CoComment
```
{
    _id:
    body:
    time:
    comment_id:
    user_id:
}
```

### PostPhoto
```
{
    _id:
    photo_user_id:
    photo_post_id:
    photo_url:
}
```

### FeedNews
```
{
    _id:
    thumbnail_photo:
    thumbnail_url:
    thumbnail_title:
    thumbnail_info:
    schedule_id:
}
```

### FeedVideo
```
{
    _id:
    thumbnail_photo:
    thumbnail_url:
    thumbnail_title:
    thumbnail_info:
    schedule_id:
}
```