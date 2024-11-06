# db_manager.py
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://username:password@localhost:3306/db_name"
engine = db.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_auction_data(auction_no):
    # 세션을 함수 내에서 생성하고, 사용 후 닫음
    with Session() as session:
        # auction, bond, issue_company 테이블에서 데이터 가져오기
        auction_data = session.execute("SELECT * FROM auction WHERE auction_no = :auction_no", {"auction_no": auction_no}).fetchone()
        
        # auction_data가 None일 경우를 대비한 검증
        if auction_data is None:
            raise ValueError(f"No auction data found for auction_no {auction_no}")
        
        bond_data = session.execute("SELECT * FROM bond WHERE auction_no = :auction_no", {"auction_no": auction_no}).fetchall()
        issuer_data = session.execute("SELECT * FROM issue_company WHERE issue_company_no = :issue_company_no", {"issue_company_no": auction_data['issue_company_no']}).fetchone()
        
        # issuer_data가 None일 경우 예외 발생
        if issuer_data is None:
            raise ValueError(f"No issuer data found for issue_company_no {auction_data['issue_company_no']}")
        
        return auction_data, bond_data, issuer_data
