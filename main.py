from website import create_app

app = create_app()

ENV ='prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/sra'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://aleptntliotjbk:be95b5bdbb6c0881b7eb77bbfb1d37637407324f75bd5bc69eeb464118f3f6ee@ec2-3-223-39-179.compute-1.amazonaws.com:5432/d4j80rtrsg22raPS?sslmode=require'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    app.run(debug=True)