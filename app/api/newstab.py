#뉴스탭 보기
@app.route('/newstab', methods=['GET'])

#뉴스 검색
@app.route('/newstab/<int: id>', methods=['GET'])

#뉴스탭 좋아요
@app.route('/newstab/like/<int: id>', methods=['POST','DELETE'])

#댓글 보기
@app.route('/newstab/comment', methods=['GET'])

#댓글 등록 및 삭제
@app.route('/newstab/comment', methods=['POST', 'DELETE'])

#댓글 좋아요
@app.route('/newstab/comment/like/<int:id>', methods=['POST','GET'])