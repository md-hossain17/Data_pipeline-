from dataclasses import dataclass

@dataclass
class Item:
    separator:","
    name: str
    value: float
    catagory: str
    weight: float

    @staticmethod
    def deserialise(row: str) -> 'Item':
        colums = row.split(Item.separator)
        item =item(
            name=colums[0],
            value=float(colums[1]),
            catagory=colums[2],
            weight=float(colums[3]),
        )
        return item
    def display_price(self):
        print(f'{self.name} costs {self.value} euros')
        return
