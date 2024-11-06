# main.py
from html_generator import generate_html

def main(auction_no):
    try:
        # HTML 파일들 생성
        html_paths = generate_html(auction_no)
        
        # 생성된 HTML 파일 경로들 출력
        print(f"Auction {auction_no} HTML files generated at:")
        for path in html_paths:
            print(f"- {path}")
            
    except ValueError as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"Unexpected error in processing auction {auction_no}: {e}")

if __name__ == "__main__":
    auction_number = 20241024  # 테스트용 경매 번호
    main(auction_number)
