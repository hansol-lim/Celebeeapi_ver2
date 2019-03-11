@app.route('/posts', methods=['GET'])

@app.route('/post/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])

@app.route('/post/search/<int:id>', methods=['GET'])

@app.route('/post/like/<int:id>', methods=['GET','POST'])