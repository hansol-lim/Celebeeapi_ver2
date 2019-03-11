#스케줄 가져오기
@app.route('/sc', methods=['GET'])

#스케줄순서
@app.route('/sc/<int:date>', methods=['GET'])

#스케줄검색
@app.route('/sc/search', methods=['GET'])

#스케줄좋아요
@app.route('/sc/like/<int:id>', methods=['GET'])

#스케줄페이지네이션
@app.route('/sc/page/<int:page>', methods=['GET'])