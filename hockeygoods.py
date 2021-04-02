from models.enums.country import Country
from models.enums.type import Type

class HockeyGoods:
    def __init__ (self, name: str, price: float, weight_in_grams: int, brand: str, origin_country: Country, color: str, type: Type, material: str):
        self.name=name
        self.price = price
        self.weight_in_grams = weight_in_grams
        self.brand = brand
        self.origin_country = origin_country
        self.color = color
        self.type = type
        self.material = material