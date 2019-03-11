@app.route('/newstab', methods=['GET'])

@app.route('/newstab/<int: id>', methods=['GET'])

@app.route('/newstab/like/<int: id>', methods=['GET','POST'])