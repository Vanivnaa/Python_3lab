from models.enums.type import Type
from models.enums.sort import SortOrder
from models.hockeygoods import HockeyGoods, Type
from operator import attrgetter


class HockeyClubManage:
    def __init__(self, goods: []):
        self.goods = goods
     
    def search_by_type(self, type: Type):
        new_list = []
        if type == Type.FIELD_PLAYER:
            print("\n\tGoods for field hockey players \n")
        if type == Type.GOALKEEPER:
            print("\n\tGoods for goalkeeping hockey players\n")
  

    def sort_by_price(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            s = sorted(self.goods, key=attrgetter('price'))
            for x in range(len(s)):
                print("\t", s[x].name, "-", s[x].price, "$")
        if  sort_order == SortOrder.DESC:
            s = sorted(self.goods, key=attrgetter('price'), reverse=True)
            for x in range(len(s)):
                print("\t", s[x].name, "-", s[x].price, "$")

    def sort_by_country(self, sort_order: SortOrder):
        if sort_order == SortOrder.ASC:
            s = sorted(self.goods, key=attrgetter('origin_country'))
            for x in range(len(s)):
                print("\t", s[x].name, "-", s[x].origin_country)
        if  sort_order == SortOrder.DESC:
            s = sorted(self.goods, key=attrgetter('origin_country'), reverse=True)
            for x in range(len(s)):
                print("\t", s[x].name, "-", s[x].origin_country)

