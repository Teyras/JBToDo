from JBToDo import app

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')
