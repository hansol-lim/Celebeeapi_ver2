#뉴스피드
@app.route('/feed/news', methods=['GET'])

#뉴스피드 좋아요
@app.route('/feed/news/like/<int: id>', methods=['POST','DELETE'])

#댓글 보기
@app.route('/feed/news/comment', methods=['GET'])

#댓글 등록 및 삭제
@app.route('/feed/news/comment', methods=['POST', 'DELETE'])

#댓글 좋아요
@app.route('/feed/news/comment/like/<int:id>', methods=['POST','DELETE'])

#영상피드
@app.route('/feed/video', methods=['GET'])

#영상피드 좋아요
@app.route('/feed/video/like/<int: id>', methods=['POST','DELETE'])

#댓글 보기
@app.route('/feed/video/comment', methods=['GET'])

#댓글 등록 및 삭제
@app.route('/feed/video/comment', methods=['POST', 'DELETE'])

#댓글 좋아요
@app.route('/feed/video/comment/like/<int:id>', methods=['POST','DELETE'])