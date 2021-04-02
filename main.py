from models.hockeygoods import HockeyGoods
from models.manage import HockeyClubManage
from models.enums.type import Type 
from models.enums.country import Country
from models.enums.sort import SortOrder
from models.skates import Skates
from models.stick import Stick
from models.protectiveequipment import ProtectiveEquipment, Protection


def main():
   
    skates = Skates ("Skates", 1500, 1148, "TECNOPRO", "China", "black", 2, "pvc leather", 2, 39)
    stick = Stick ("Stick", 1752, 500, "FISHER", "Germany", "yellow", 2, "carbon fiber, fiberglass", 166, 85, 135)
    helmet = ProtectiveEquipment("Helmet", 1248, 600, "Bauer", "Poland", "white", 1, "plastic", "Adult", 1)
 
    manage = HockeyClubManage([skates, stick, helmet])

    manage.search_by_type(Type.FIELD_PLAYER)
    print("\nSorting goods by price:")
    manage.sort_by_price(SortOrder.DESC)
    print("\nSorting goods by country:")
    manage.sort_by_country(SortOrder.ASC)

if __name__ == "__main__":
    main()