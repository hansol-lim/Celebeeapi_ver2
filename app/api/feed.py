@app.route('/feed/news', methods=['GET'])

@app.route('/feed/news/<int: id>', methods=['GET'])

@app.route('/feed/news/like/<int: id>', methods=['GET','POST'])

@app.route('/feed/video', methods=['GET'])

@app.route('/feed/video/<int: id>', methods=['GET'])

@app.route('/feed/video/like/<int: id>', methods=['GET','POST'])