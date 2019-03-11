#댓글 등록 및 삭제
@app.route('/comment', methods=['POST', 'DELETE'])

#댓글 좋아요
@app.route('/comment/like/<int:id>', methods=['POST','GET'])