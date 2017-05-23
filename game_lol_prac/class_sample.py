class LOL:
    """이 클래스는 리그 오브 레전드의 캐릭터 클래스입니다."""
    shop_list = {
        "도란 검" : 450,
        "피바라기" : 2400,
        "몰락한 왕의 검" : 1500,
        "삼위일체" : 3333,
        "마나무네" : 860,
    }

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.gold = 500
        self.exp = 0
        self.damage = 10
        self.hp = 100
        self.max_hp = 100
        self.item_list = []

    def game_start(self):
        print("==소환사의 협곡에 오신 것을 환영합니다.==")
        while(True):
            print("----------")
            choice = input("1: 상점, 2: 전투, 3: 챔피언 상태, 4: 회복, 0: 종료\n입력 : ")

            if choice == "0":
                break
            elif choice == "1":
                self.shop()
            elif choice == "2":
                self.battle()
            elif choice == "3":
                self.print_status()
            elif choice == "4":
                print("회복 되었습니다.")
                self.hp = self.max_hp
            else:
                print("올바른 값을 입력해 주세요.")

    def battle(self):
        while(True):
            print("----------")
            print("1: 미니언. 2: 레드. 3: 용. 4: 바론. 0: 전투 종료")
            choice = input("상대할 적을 고르시오: ")
            if choice == "0":
                break
            elif choice == "1":
                self.battle_scene("미니언", 10, 50, 50, 100)

            elif choice == "2":
                self.battle_scene("레드", 40, 500, 200, 400)

            elif choice == "3":
                self.battle_scene("용", 60, 1000, 400, 1500)
            elif choice == "4":
                self.battle_scene("바론", 100, 10000, 1000, 10000)

    def battle_scene(self, mob_name, mob_dmg, mob_hp, mob_exp, mob_gold):
        print("{}와 전투를 시작합니다.".format(mob_name))
        while(True):
            if self.hp == 0:
                print("사망하셨습니다. 경험치와 골드를 잃어버립니다.")
                self.exp = 0
                self.gold = 0
                break
            if mob_hp > 0:
                print("----------")
                print("{}, 공격력: {}, 남은 체력: {}".format(mob_name, mob_dmg, mob_hp))
                choice = input("0: 도주, 1: 공격, 2: 방어\n입력: ")
                if choice == '0':
                    print("도망쳤습니다.")
                    break
                elif choice == '1':
                    mob_hp -= self.damage
                    print("{}의 공격! {}에게 {}의 데미지를 입혔다.".format(self.name, mob_name, self.damage))
                    self.hp -= mob_dmg
                    print("{}의 공격! {}의 데미지를 입었다. 남은 쳬력: {}".format(mob_name, mob_dmg, self.hp))
                elif choice == '2':
                    print("{}의 공격! 하지만 버텨냈다. 남은 쳬력: {}".format(mob_name, mob_dmg, self.hp))
                else:
                    print("잘못된 입력.")
            else:
                print("{}님이 {}를 처치했습니다. 경험치 {}과 골드 {} 획득.".format(self.name, mob_name, mob_exp, mob_gold))
                self.increase_exp(mob_exp)
                self.increase_gold(mob_gold)
                break

    def shop(self):
        while(True):
            print("----------")
            print("0: 상점 나가기, 1: 아이템 목록, 구매할 아이템의 이름을 입력하면 구매됩니다.")
            choice = input("입력: ")
            if choice == "0":
                break
            elif choice == "1":
                self.print_shop_list()
            else:
                buy = self.shop_list[choice]
                if buy:
                    self.buy_item(choice, buy)
                else:
                    print("올바른 아이템 명을 입력하세요.")


    def buy_item(self, item_name, gold):
        if item_name in self.item_list:
            print("***이미 구매한 아이템입니다.***")
        else:
            if self.gold < gold:
                print("***금이 부족합니다.***")
            else:
                print("***{} 구매 완료***".format(item_name))
                self.gold -= gold
                self.item_list.append(item_name)
                if item_name == "Doran's Blade":
                    self.damage += 5
                elif item_name == "Manamune":
                    self.damage += 25
                elif item_name == "Blade of the Ruined King":
                    self.damage += 60
                elif item_name == "The Bloodthirster":
                    self.damage += 100
                elif item_name == "Trinity Force":
                    self.damage += 333

    #private 메서드
    def level_up(self):
        self.level += 1
        self.max_hp += 200
        self.hp = self.max_hp
        self.damage += 20

    def increase_gold(self, gold):
        self.gold += gold

    def increase_exp(self, exp):
        self.exp += exp
        if self.exp >= 100:
            self.level_up()
            self.exp -= 100

    #public 메서드
    def print_status(self):
        print("----------")
        print("챔피언 명 : {}\n레벨 : {}\n공격력 : {}\n체력 : {}\n골드 : {}\n아이템 리스트"
              .format(self.name, self.level, self.damage,
                      self.hp, self.gold), self.item_list)

    def print_shop_list(self):
        print("----------")
        for name, price in self.shop_list.items():
            print("-{} {}gold".format(name, price))
        print("----------")
