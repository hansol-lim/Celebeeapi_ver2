#게시판 전체 내역
@app.route('/posts', methods=['GET'])

#게시판 내용, 등록, 수정, 삭제
@app.route('/post/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])

#게시글 검색
@app.route('/post/search/<int:id>', methods=['GET'])

#게시글 좋아요, 좋아요 취소
@app.route('/post/like/<int:id>', methods=['POST','DELETE'])

#댓글 보기
@app.route('post/comment', methods=['GET'])

#댓글 등록 및 삭제
@app.route('post/comment', methods=['POST', 'DELETE'])

#댓글 좋아요
@app.route('post/comment/like/<int:id>', methods=['POST','DELETE'])