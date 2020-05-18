# 定义表示银行卡和ATM（自动柜员机）的类，要求ATM可以实现读卡、存钱、取钱、转账的功能。

class AccountCard:
    def __init__(self, card_no, expiry_date, card_type='储蓄卡'):
        self.card_no = card_no
        self.expiry_date = expiry_date
        self.card_type = card_type

    def __repr__(self):
        return f'卡号：{self.card_no}\n' \
               f'有效期:{self.expiry_date}\n' \
               f'类型:{self.card_type}'


class ATM:
    def __init__(self):
        self.accounts = {
            '1122334455667788': {'password': '123321', 'balance': 1200.0, 'valid': True},
            '1122334455667789': {'password': '123456', 'balance': 54321.0, 'valid': True},
            '1122334455667790': {'password': '147258', 'balance': 0.0, 'valid': False}
        }
        self.current_card = None
        self.current_account = None

    def read_card(self, card):
        """读卡"""
        if card.card_no in self.accounts:
            self.current_account = self.accounts[card.card_no]
            for _ in range(3):
                password = input('请输入密码：')
                if self.current_account['password'] != password:
                    print('密码错误')
                else:
                    self.current_card = card
                    return True
                print('卡被回收，请联系工作人员或拨打123-456-789')
                self.current_card = None
                self.current_account = None
        else:
            print('无效的银行卡，请取回')
        return  False

    def show_balance(self):
        """查询余额"""
        if self.current_account:
            print(f'账户余额:{self.current_account["balance"]}元')

    def deposit(self, money):
        """存钱"""

        if self.current_account and money > 0:
            self.current_account['balance'] += money
            print('存款成功余额为：', money)
            return True
        return False

    def withdraw(self, money):
        """取钱"""

        if self.current_account and money <= self.current_account['balance']:
            self.current_account['balance'] -= money
            return True
        else:
            print('余额不足')
            return False

    # def tranfer(self, other_crad_no, money):
    #     """转账"""
    #     if other_crad_no in self.accounts:
    #         other_crad = self.accounts[other_crad_no]
    #         if money <= self.current_account['balance']:
    #             self.current_account['balance'] -= money
    #             other_crad['balance'] += money
    #             print('转账成功')
    #             return True
    #         else:
    #             print('无效的转出账户')
    #         return False
    def transfer(self, other_card_no, money):
        """转账"""
        if other_card_no in self.accounts:
            other_account = self.accounts[other_card_no]
            if money <= self.current_account['balance']:
                self.current_account['balance'] -= money
                other_account['balance'] += money
                print('转账成功')
                return True
        else:
            print('无效的转出账户')
        return False

    def retrieve(self):
        """取卡"""

        self.current_card = None
        self.current_account = None
        print('请取走您的卡')


def main():
    my_crad = AccountCard('1122334455667788', '2020-12-18')
    print(my_crad)
    atm = ATM()
    # print(atm.read_card(my_crad))
    if atm.read_card(my_crad):
        while True:
            # 等待用户操作
            option = input('请输入您的操作：')
            if option == '1':
                """存钱"""
                deposit_money = float(input('请输入要存的金额:'))
                atm.deposit(money=deposit_money)
                #print(atm.deposit())
            elif option == '2':
                """取钱"""
                withdraw_money = float(input('请输入要取的金额:'))
                atm.withdraw(money=withdraw_money)
            elif option == '3':
                """查询余额"""
                atm.show_balance()
            elif option == '4':
                """转账"""
                user_name = input('请输入转账的用户名:')
                tranfer_money = float(input('请输入转账的金额:'))
                atm.tranfer(other_crad_no=user_name,money=tranfer_money)
            elif option == '5':
                """退卡"""
                atm.retrieve()
                break
            else:
                print('输入错误')






if __name__ == '__main__':
    main()