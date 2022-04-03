# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным
# файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    log_list = []
    spam = {}
    for line in f:
        splitted = line.split()
        log_list.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam.setdefault(splitted[0], 0)
        spam[splitted[0]] += 1

spam = sorted(spam.items(), key=lambda s: s[1], reverse=True)
print(spam[:5])
#print(log_list)