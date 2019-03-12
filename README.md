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
    _id: <UserID>,
    is_admin: <type:bool>,
    uid: <type: str>,
    email: <type: str>,
    token: <type: str>,
    nickname: <type: str>,
    photo: <type: str>,
    device_key: <type: str>
}
```
### Idol
```
{
    _id: <IdolID>,
    idol_name: <type: str>,
    idol_img: <type: str>
}
```
### Post
```
{
    _id: <PostID>,
    body: <type: str>,
    time: <type: datetime>,
    type_num: <type: int>
}
```
### Comment
```
{
    _id: <CommentID>,
    time: <type: datetime>,
    bool: <type: bool>
    body: <type: str>
}
```
### Badge
```
{
    _id: <BadgeID>,
    bad_name: <type: str>,
    bad_type: <type: int>
}
```
### Schedule
```
{
    _id: <ScheduleID>,
    date: <type: datetime>,
    sc_name: <type: str>,
    sc_info: <type: str>,
    sc_location: <type: str>,
}
```

### Feed
```
{
    _id: <FeedID>,
    nov: <type: bool>
    th_title: <type: str>,
    th_photo: <type: str>,
    th_url: <type: str>,
    th_info: <type: str>,
}
```
### Newstab
```
{
    _id: <NewsID>,
    pr_title: <type: str>,
    pr_photo: <type: str>,
    pr_url: <type: str>,
    pr_name: <type: str>,
    date: <type: datetime>
}
```
