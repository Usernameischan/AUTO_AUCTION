from jinja2 import Environment, FileSystemLoader
from mock_db_manager import get_auction_data
from datetime import datetime, timedelta
import locale
import os
import codecs
import chardet

# 한국어 설정
try:
    locale.setlocale(locale.LC_TIME, 'ko_KR.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'Korean_Korea.949')
    except:
        pass

# Helper functions for data formatting

def format_exp_original(value):
    if value == "0300000":
        return "3년"
    elif value == "0500000":
        return "5년"
    return value

def format_issuegb(value):
    return "신규발행" if value == 0 else "통합발행"

def format_bond_type(value):
    types = ["국채", "지방채", "특수채", "외국채", "회사채", "전단채/CP"]
    return types[value] if 0 <= value < len(types) else value

def format_gurtgb(value):
    types = ["보증", "부분보증", "담보부", "무보증", "정부보증"]
    return types[value] if 0 <= value < len(types) else value

def format_redmmthd(value):
    return "만기일시상환" if value == 0 else "분할상환"

def format_date(value, format="%Y년 %m월 %d일"):
    if isinstance(value, str) and len(value) == 8:
        date_obj = datetime.strptime(value, "%Y%m%d")
    elif isinstance(value, datetime):
        date_obj = value
    else:
        return value
    return date_obj.strftime(format)

'''
def format_datetime_for_payment(date):
    if isinstance(date, str) and len(date) == 8:
        date_obj = datetime.strptime(date, "%Y%m%d")
        return f"{date_obj.strftime('%Y년 %m월 %d일')} 14:00 까지"
    return date
'''


def map_price_base(value):
    price_mapping = {
        -1: "기준없음", 0: "추후공지", 7: "국고3사평균", 8: "국고4사평균",
        1: "민평3사평균", 2: "민평4사평균", -3: "특수채 AAA 3사평균", -4: "특수채 AAA 4사평균",
        -5: "특수채 AA+ 3사평균", -6: "특수채 AA+ 4사평균", -7: "회사채 AA- 3사평균",
        -8: "회사채 AA- 4사평균", 9: "정부보증채 민평 3사평균", 6: "국고 6M", 
        12: "국고 1Y", 24: "국고 2Y", 360: "국고 30Y"
    }
    return price_mapping.get(value, "기준없음")

def format_bid_time(auc_date, auc_time):
    date_part = format_date(auc_date)
    start_time = datetime.strptime(auc_time, "%H%M%S")
    end_time = (start_time + timedelta(minutes=30)).strftime("%H시 %M분")
    start_time = start_time.strftime("%H시 %M분")
    return f"{date_part} {start_time} ~ {end_time}"

def generate_html(auction_no):
    auction_data, bond_data, issuer_data = get_auction_data(auction_no)
    
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True
    )
    
    # 필터 설정
    env.filters['date'] = format_date
    env.filters['exp_original'] = format_exp_original
    env.filters['issuegb'] = format_issuegb
    env.filters['bond_type'] = format_bond_type
    env.filters['gurtgb'] = format_gurtgb
    env.filters['redmmthd'] = format_redmmthd
    env.filters['price_base'] = map_price_base
    env.filters['bid_time'] = format_bid_time

    templates = [
        ('bond_template_multiple_items.html', f'auction_{auction_no}.html'),
        ('20241024_detail.html', f'{auction_no}_detail.html'),
        ('20241024_detail_2.html', f'{auction_no}_detail_2.html')
    ]

    generated_files = []
    
    for template_name, output_filename in templates:
        try:
            template_path = os.path.join(template_dir, template_name)
            
            # UTF-8로 템플릿 읽기 시도
            try:
                with open(template_path, 'r', encoding='utf-8') as f:
                    template_str = f.read()
            except UnicodeDecodeError:
                # UTF-8 실패시 EUC-KR로 시도
                with open(template_path, 'r', encoding='euc-kr') as f:
                    template_str = f.read()
            
            template = env.from_string(template_str)
            output = template.render(
                auction_data=auction_data,
                bond_data=bond_data,
                issuer_data=issuer_data
            )

            output_dir = "D:/김찬/경매/자동화/auto_auction/test"
            os.makedirs(output_dir, exist_ok=True)
            file_path = os.path.join(output_dir, output_filename)
            
            # UTF-8로 저장
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(output)
                
            generated_files.append(file_path)
            
        except Exception as e:
            print(f"Error processing template {template_name}: {str(e)}")
            print(f"Current encoding for {template_name}: {chardet.detect(open(template_path, 'rb').read())}")
            raise

    return generated_files
