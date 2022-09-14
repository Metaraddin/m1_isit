from apriori_python import apriori
from efficient_apriori import apriori as eff_apriori
from fpgrowth_py import fpgrowth


transactions = [['Стиральная машина', 'Телевизор'],
                ['Духовой шкаф', 'Микроволновая печь', 'Сушильная машина'],
                ['Телевизор', 'Ноутбук'],
                ['Тостер', 'Холодильник', 'Морозильник'],
                ['Тостер', 'Телевизор'],
                ['Духовой шкаф', 'Телевизор'],
                ['Стиральная машина', 'Сушильная машина', 'Тостер', 'Духовой шкаф'],
                ['Ноутбук', 'Тостер'],
                ['Телевизор', 'Холодильник', 'Морозильник'],
                ['Стиральная машина', 'Тостер'],
                ['Ноутбук', 'Сушильная машина', 'Телевизор', 'Тостер'],
                ['Духовой шкаф', 'Сушильная машина'],
                ['Морозильник', 'Холодильник', 'Телевизор'],
                ['Стиральная машина', 'Сушильная машина'],
                ['Тостер', 'Ноутбук'],
                ['Холодильник', 'Духовой шкаф', 'Ноутбук', 'Телевизор'],
                ['Ноутбук', 'Стиральная машина', 'Тостер', 'Духовой шкаф'],
                ['Телевизор', 'Ноутбук', 'Морозильник'],
                ['Ноутбук', 'Стиральная машина'],
                ['Тостер', 'Духовой шкаф']]


def apriori_alg(data):
    freq_item_set, rules = apriori(data, minSup=0.2, minConf=0.2)
    print(rules)


def efficient_apriori_alg(data):
    freq_item_set, rules = eff_apriori(data, min_support=0.5, min_confidence=0.5)
    print(rules, '\n')
    rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
    for rule in sorted(rules_rhs, key=lambda rule: rule.confidence):
        print(rule)


def fpgrowth_alg(data):
    try:
        freq_item_set, rules = fpgrowth(data, minSupRatio=0.5, minConf=0.5)
        print(rules)
    except TypeError:
        pass


# apriori_alg(transactions)
# efficient_apriori_alg(transactions)
# fpgrowth_alg(transactions)
