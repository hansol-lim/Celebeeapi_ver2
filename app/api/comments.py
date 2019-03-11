@app.route('/comment', methods=['POST', 'DELETE'])

@app.route('/comment/like/<int:id>', methods=['POST','GET'])