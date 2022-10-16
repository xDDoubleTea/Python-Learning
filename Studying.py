class no_effort_has_been_made(Exception):
    def __init__(self):
        super().__init__()

class not_enough_perseverant(Exception):
    def __init__(self):
        super().__init__()

class is_not_suitable_for_studying(Exception):
    def __init__(self):
        super().__init__()

def exam(perseverance, effort, talent):
    if perseverance + effort + talent >= 100:
        pass
    elif effort < 40:
        raise no_effort_has_been_made
    elif perseverance < 40:
        raise not_enough_perseverant
    else:
        raise is_not_suitable_for_studying

my_perseverance = input('堅持程度')
my_effort = input('努力程度')
my_talent = input('天賦')

try:
    exam(perseverance = float(my_perseverance), effort = float(my_effort), talent = float(my_talent))
    print('Pass')
except no_effort_has_been_made:
    print('多努力點')
except not_enough_perseverant:
    print('堅持下去')
except is_not_suitable_for_studying:
    print('你可能不適合念書')
except TypeError:
    print('你根本搞不清楚狀況吧??叫你輸入數值你給我輸入文字??')
