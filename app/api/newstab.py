#뉴스탭 보기
@app.route('/newstab', methods=['GET'])

#특정 뉴스
@app.route('/newstab/<int: id>', methods=['GET'])

#뉴스탭 좋아요
@app.route('/newstab/like/<int: id>', methods=['GET','POST'])