from website import create_app
import os
import psycopg2
import dj_database_url

app = create_app()

DATABASE_URL = os.environ['postgres://mhgqtisxrnhajo:47830ca44a024943e000deda5eb86a37b84fb1e4dd79bec1cc233702ce32a99e@ec2-3-225-132-26.compute-1.amazonaws.com:5432/d3m22ojr7fksk2']



ENV ='prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/sra'
else:
    app.debug = False
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)



if __name__ == '__main__':
    app.run(debug=True)