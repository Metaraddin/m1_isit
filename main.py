from apriori_python import apriori
from efficient_apriori import apriori as eff_apriori
from fpgrowth_py import fpgrowth
from PyARMViz import PyARMViz
import timeit


transactions = [['Стиральная машина', 'Сушильная машина', 'Духовой шкаф', 'Телевизор', 'Ноутбук'],
                ['Микроволновая печь', 'Ноутбук', 'Стиральная машина', 'Сушильная машина'],
                ['Стиральная машина', 'Сушильная машина', 'Микроволновая печь', 'Холодильник'],
                ['Морозильник', 'Духовой шкаф', 'Тостер', 'Стиральная машина'],
                ['Стиральная машина', 'Сушильная машина', 'Ноутбук', 'Микроволновая печь', 'Чайник'],
                ['Чайник', 'Морозильник', 'Тостер', 'Духовой шкаф'],
                ['Морозильник', 'Духовой шкаф', 'Стиральная машина', 'Сушильная машина', 'Ноутбук'],
                ['Стиральная машина', 'Сушильная машина', 'Телевизор'],
                ['Ноутбук', 'Микроволновая печь', 'Холодильник', 'Сушильная машина'],
                ['Сушильная машина', 'Стиральная машина', 'Ноутбук', 'Холодильник', 'Чайник'],
                ['Телевизор', 'Стиральная машина', 'Сушильная машина', 'Ноутбук'],
                ['Холодильник', 'Сушильная машина', 'Ноутбук', 'Стиральная машина'],
                ['Микроволновая печь', 'Холодильник', 'Сушильная машина'],
                ['Микроволновая печь', 'Духовой шкаф', 'Телевизор'],
                ['Духовой шкаф', 'Ноутбук', 'Стиральная машина', 'Сушильная машина'],
                ['Стиральная машина', 'Сушильная машина', 'Микроволновая печь', 'Ноутбук', 'Телевизор'],
                ['Морозильник', 'Тостер', 'Духовой шкаф', 'Сушильная машина'],
                ['Стиральная машина', 'Морозильник', 'Духовой шкаф', 'Сушильная машина'],
                ['Холодильник', 'Телевизор'],
                ['Стиральная машина', 'Микроволновая печь', 'Ноутбук', 'Сушильная машина']]

# stat = {}
#
# for transaction in transactions:
#     for item in transaction:
#         try:
#             stat[item] += 1
#         except KeyError:
#             stat[item] = 1
#
# sort_transactions = []
# for transaction in transactions:
#     sort_transaction = {}
#     for item in transaction:
#         sort_transaction[item] = stat[item]
#     sort_transactions.append(dict(sorted(sort_transaction.items(), key=lambda item: item[1], reverse=True)))
#
# for sort_transaction in sort_transactions:
#     print(sort_transaction)


# print('Apriori: ', timeit.timeit('lambda: apriori(data, minSup=0.5, minConf=0.8)', number=1000))
# print('Efficient Apriori: ', timeit.timeit('lambda: eff_apriori(data, min_support=0.5, min_confidence=0.8)', number=1000))
# print('FPGrowth: ', timeit.timeit('lambda: fpgrowth(data, minSupRatio=0.5, minConf=0.8)', number=1000))

rules = apriori(transactions, minSup=0.5, minConf=0.8)[1]
print('\nApriori:')
for rule in rules:
    print(rule)

rules = eff_apriori(transactions, min_support=0.5, min_confidence=0.8)[1]
print('\nEfficient Apriori:')
rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
for rule in sorted(rules_rhs, key=lambda rule: rule.confidence):
    print(rule)
PyARMViz.adjacency_graph_plotly(rules)

rules = fpgrowth(transactions, minSupRatio=0.5, minConf=0.8)[1]
print('\nFPGrowth:')
for rule in rules:
    print(rule)
