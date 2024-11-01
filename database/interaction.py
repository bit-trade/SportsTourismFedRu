from sqlalchemy import insert
from connect import engine
# from models import pereval_added
#
#
# with engine.connect() as conn:
#     stmt = insert(pereval_added).values(
#         [
#             {'': ''},
#             {'': ''},
#         ]
#     )
#
#     # res = conn.execute(text("SELECT VERSION()"))
#     # print(f'{res=}')
#     conn.execute(stmt)
#     conn.commit()