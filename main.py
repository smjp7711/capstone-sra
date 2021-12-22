from website import create_app

app = create_app()


ENV ='prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/sra'
else:
    app.debug = False
    app.config['SQLACHEMY_DATABASE_URI'] = 'postgres://mhgqtisxrnhajo:47830ca44a024943e000deda5eb86a37b84fb1e4dd79bec1cc233702ce32a99e@ec2-3-225-132-26.compute-1.amazonaws.com:5433/d3m22ojr7fksk2'
    

if __name__ == '__main__':
    app.run(debug=True)