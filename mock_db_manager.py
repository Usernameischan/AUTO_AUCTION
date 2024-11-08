from datetime import datetime

def get_auction_data(auction_no):
    # AUCTION 테이블 mock 데이터
    auction_data = {
        'auction_no': int(auction_no),  # int(11)
        'auction_name': '경기주택도시공사 채권경매',  # varchar(100)
        'num_bonds': 2,  # int(11)
        'total_auc_amt': 200000,  # int(11) - 총 경매액 합(단위 고려)
        'mbs_no': 0,  # int(11) - MBS 번호가 아닌 경우 0
        'mbs_trench_no': 0,  # int(11) - MBS Trench 번호가 아닌 경우 0
        'issuer_id': 'gghc123',  # varchar(45)
        'issue_company_no': 1001,  # int(11)
        'auc_date': '20241024',  # char(8) - YYYYMMDD
        'auc_time': '093000',  # char(6) - HHMMSS
        'pre_date': '20241024',  # char(8) - YYYYMMDD
        'pre_time': '090000',  # char(6) - HHMMSS
        'notice_date': '20241010',  # char(8) - YYYYMMDD
        'auc_type': 10,  # int(11)
        'auc_present': 1,  # int(11)
        'underwriter_rule': 0,  # int(11)
        'underwriter_price': None,  # int(11) or None
        'underwriter_ids': 'test1, test2',  # varchar(100)
        'pre_round_has_price_limit': 1,  # int(11)
        'pre_round_has_amt_limit': 1,  # int(11)
        'perm_rule_effective_round': 1,  # int(11)
        'first_perm_rule_multiple': 20,  # int(11)
        'next_perm_rule_multiple': 15,  # int(11)
        'first_round_interval': '001000',  # char(6) - HHMMSS
        'next_round_interval': '000200',  # char(6) - HHMMSS
        'max_round': 2,  # int(11)
        'not_full_option': 1,  # int(11)
        'attachlink1': 'http://example.com/attachment1.pdf',  # mediumtext
        'attachlink2': 'http://example.com/attachment2.pdf',  # mediumtext
        'notice_msg': '이 경매는 예시입니다.',  # mediumtext
        'caution_msg': '경매 주의 사항 예시입니다.',  # mediumtext
        'valid': 1,  # tinyint(1)
        'test': 0,  # tinyint(1)
        'created_date': datetime(2024, 10, 1, 9, 0, 0),  # timestamp
        'repurchase_auc_no': None,  # int(11)
        'amt_enable': 1,  # int(11)
        'suc_bidder_auth': None,  # int(11)
        'spec_bidder_auth': None,  # int(11)
        'num_spec_bidder_auth': None,  # int(11)
    }

    # BOND 테이블 mock 데이터 (다중 채권 종목 추가)
    bond_data = [
        {
            'bond_no': 1,
            'auction_no': int(auction_no),
            'issuer_id': 'gghc123',
            'company_no': 1001,
            'kr_code': 'KR123456',
            'exp_original': '0300000',
            'exp_left': '0299000',
            'amt_unit': 100,
            'amt_scale': '억',
            'price_form': 0,
            'price_frac': -2,
            'price_unit': 30,
            'price_base': 1,
            'price_limit_rel': None,
            'price_floor_rel': None,
            'bond_nm': '경기주택도시공사 제24-10-83회(지)',
            'issuegb': 0,
            'underwriter_comp': '미정',
            'clwb': None,
            'suc_status': None,
            'suc_amt': None,
            'total_bid_num': None,
            'total_bid_amt': None,
            'min_price': 100,
            'max_price': None,
            'suc_type': None,
            'suc_price': None,
            'firstcut_price': None,
            'min_suc_price': None,
            'max_suc_price': None,
            'avg_weighted_price': None,
            'avg_weighted_suc_price': None,
            'secondary_price': None,
            'secondaty_amt': None,
            'compete_rate': None,
            'last_bid_time': None,
            'last_bid_auc_time': None,
            'last_bid_price': None,
            'reference_price': None,
            'reference_name': '민평',
            'inttypestring': '3개월 후급',
            'redmmthd': 0,
            'bond_type': 2,
            'issue_date': '20241025',
            'consolidate_issue_date': None,
            'issue_amt': 1000,
            'issue_amt_min': None,
            'issue_amt_max': None,
            'original_amt': None,
            'exp_date': '20271025',
            'gurtgb': 3,
            'creditgrdhgp': 'AAA(민평, NICE)',
            'creditgrdhsp': 1,
            'creditgrdhsj': 1,
            'creditgrdssp': None,
            'mbs_call_option1': None,
            'mbs_call_option2': None,
            'mbs_etc': None,
            'coupon_rate': None,
            'created_date': datetime(2024, 10, 1, 9, 0, 0),
            'sirial_num': None,
            'repurchase_auc_no': None,
            'spec_bidder_auth': None,
            'spec_auth_sirial_num_start': None,
            'spec_auth_sirial_num_end': None,
            'closecheck': 0,
        },
        {
            'bond_no': 2,
            'auction_no': int(auction_no),
            'issuer_id': 'gghc123',
            'company_no': 1001,
            'kr_code': 'KR123457',
            'exp_original': '0500000',
            'exp_left': '0499000',
            'amt_unit': 100,
            'amt_scale': '억',
            'price_form': 0,
            'price_frac': -2,
            'price_unit': 30,
            'price_base': 1,
            'price_limit_rel': None,
            'price_floor_rel': None,
            'bond_nm': '경기주택도시공사 제24-10-84회',
            'issuegb': 0,
            'underwriter_comp': '미정',
            'clwb': None,
            'suc_status': None,
            'suc_amt': None,
            'total_bid_num': None,
            'total_bid_amt': None,
            'min_price': 100,
            'max_price': None,
            'suc_type': None,
            'suc_price': None,
            'firstcut_price': None,
            'min_suc_price': None,
            'max_suc_price': None,
            'avg_weighted_price': None,
            'avg_weighted_suc_price': None,
            'secondary_price': None,
            'secondaty_amt': None,
            'compete_rate': None,
            'last_bid_time': None,
            'last_bid_auc_time': None,
            'last_bid_price': None,
            'reference_price': None,
            'reference_name': '민평',
            'inttypestring': '3개월 후급',
            'redmmthd': 0,
            'bond_type': 2,
            'issue_date': '20241025',
            'consolidate_issue_date': None,
            'issue_amt': 1000,
            'issue_amt_min': None,
            'issue_amt_max': None,
            'original_amt': None,
            'exp_date': '20291025',
            'gurtgb': 3,
            'creditgrdhgp': 'AAA(민평, NICE)',
            'creditgrdhsp': 1,
            'creditgrdhsj': 1,
            'creditgrdssp': None,
            'mbs_call_option1': None,
            'mbs_call_option2': None,
            'mbs_etc': None,
            'coupon_rate': None,
            'created_date': datetime(2024, 10, 1, 9, 0, 0),
            'sirial_num': None,
            'repurchase_auc_no': None,
            'spec_bidder_auth': None,
            'spec_auth_sirial_num_start': None,
            'spec_auth_sirial_num_end': None,
            'closecheck': 0,
        }
    ]

    # ISSUE_COMPANY 테이블 mock 데이터
    issuer_data = {
        'issue_company_no': 1001,
        'name': '경기주택도시공사',
        'business_reg_id': '123-45-67890',
        'company_reg_id': '1234567890123',
        'company_code': '04130',
        'enterprise_type': '공기업',
        'rep_name': '홍길동',
        'rep_pid': '850101-1234567',
        'can_take_over': '가능',
        'company_zip': '12345',
        'company_address1': '서울특별시 중구 세종대로 110',
        'company_address2': '광화문빌딩 20층',
        'reference_person': '재무관리처(031-220-7218)',
        'created_date': datetime(2024, 10, 1, 9, 0, 0),
    }

    return auction_data, bond_data, issuer_data
