#회원가입
@app.route('/user/register', methdos=['POST'])

#마이페이지 보기(GET),수정(PUT)
@app.route('/user/<int:id>', methods=['GET','PUT'])

#아이돌 팔로우 보기, 등록, 삭제
@app.route('/user/follow', methods=['GET','POST','DELETE'])

#내가 쓴 글 확인
@app.route('/user/write', methods=['GET'])

#알림내역확인
@app.route('/user/alarm', methods=['GET'])

#닉네임 중복 검사
@app.route('/user/nickname', methods=['POST'])