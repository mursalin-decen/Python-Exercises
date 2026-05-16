from typing import List , Tuple ,Dict, Union
number: List[int] = [1,2,3,4,5]

person :Tuple[ str, int] = ("zamn", 10)

scores : Dict [str , int] = {"Zam" : 10, "Shi": 19}


identifier : Union [str, int] = "Id123"

identifier = 12345  #also valid

n: int =5


name: str = "zam"


def sum(a:int , b:int) -> int:
    return a+b


print(sum(3,5))

