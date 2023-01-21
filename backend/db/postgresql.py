from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL = "postgresql://아이디:비밀번호@서버주소/DB이름"
engine = create_engine(URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
