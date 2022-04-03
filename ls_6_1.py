# 1. Не используя библиотеки для парсинга,
# распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# log_list = open('nginx_logs.txt', 'r', encoding='utf-8')
# for line in log_list:
#     line_list =[]
#     line_list.append(line[0:11])
#
# print(line_list)

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    log_list = []
    for line in f:
        splitted = line.split()
        log_list.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
print(log_list)



#         line_splited = line.split()
#         log_list.append(line_splited[0], line_splited[5].replace('"', ''), line_splited[6])
# print(log_list)

