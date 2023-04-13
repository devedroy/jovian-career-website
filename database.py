from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://xln9lx06htcggqzy9kfd:pscale_pw_sP3g1tVFFqfBOKFuuR9Ux6SxQIUtq8qtyYDv2rHqbsP@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"
engine = create_engine(
  db_connection_string,
  connect_args= {
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

with engine.connect() as conn:
  result = conn.execute(text('SELECT * FROM jobs'))
  print("type(result): ",type(result))
  result_all = result.all()
  print("type(result_all): ",type(result_all))
  print("result_all: ",result_all)
  first_result = result_all[0]
  print("type(first_result): ",type(first_result))
  print("first_result: ", first_result)
  first_result_dict = dict(result_all[0])
  print("type(first_result_dict): ", type(first_result_dict))