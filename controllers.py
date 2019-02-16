from sqlalchemy import create_engine
#import recommendation

CONNECTION

def get_connection():
    POSTGRES_URL = get_env_variable("POSTGRES_URL")
	POSTGRES_USER = get_env_variable("POSTGRES_USER")
	POSTGRES_PW = get_env_variable("POSTGRES_PW")
	POSTGRES_DB = get_env_variable("POSTGRES_DB")

	DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
	CONNECTION = engine.connect()


def get_recommendation(user_id : int):
    pass


class User(object):
    def get(self, id : int):
		sql = "Select user from users where user_id = %s;"
		data = (id)
		result = CONNECTION.execute(sql, data)
		print(result)


class Recommendation(object):
    def get(self, id : int):
		sql = "Select * from settings;"
		data = (id)
		result = CONNECTION.execute(sql, data)
		print(result)


