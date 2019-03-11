@app.route('/user/register', methdos=['POST'])

@app.route('/user/mypage', methods=['GET'])

@app.route('/user/mypage/edit', methods=['PUT'])

@app.route('/user/follow', methods=['POST'])

@app.route('/user/write', methods=['GET'])

@app.route('/user/nickname', methods=['POST'])

@app.route('/user/<int:id>', methods=['GET'])

@app.route('/user/alarm', methods=['GET'])

@app.route('/user/idollist', methods=['GET'])