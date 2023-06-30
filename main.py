# __init__.py allow us to import the folder 'website' as a package
from website import create_app

app = create_app()

# debug=True : Anytime there's a change of the code, it'll rerun the webserver
# use_reloader=False --> avoid the SystemExist Error when debug=True
if __name__ == '__main__' :
    app.run(port=4000,debug=True,use_reloader=False,static_files={'/static':'static'}) 