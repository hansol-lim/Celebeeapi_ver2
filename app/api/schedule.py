@app.route('/sc', methods=['GET'])

@app.route('/sc/<int:date>', methods=['GET'])

@app.route('/sc/search', methods=['GET'])

@app.route('/sc/like/<int:id>', methods=['GET'])

@app.route('/sc/page/<int:page>', methods=['GET'])

