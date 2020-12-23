with open('/var/www/html/app/register_db_test.txt', mode="w", encoding='shift_jis') as f:
        f.write(str(type(data)))
        f.write('\n')
        for key,value in data.items():
            f.write(str(type(value)))
            f.write(f'{key}:{value}\n')
        f.write(",".join(map(str,list(data.values()))))

with open('/var/www/html/app/entry_test.txt', mode="w", encoding='shift_jis') as f:
    f.write(str(type(lat)))
    f.write(str(type(lng)))
    f.write(str(type(address)))
    f.write('\n')
    f.write(f'{lat}\n')
    f.write(f'{lng}\n')
    f.write(f'{address}\n')

with open('/var/www/html/app/search_db_test3.txt', mode="w", encoding='shift_jis') as f:
    f.write(str(type(search_results)))
    f.write('\n')
    for result in search_results:
        f.write(str(type(result)))
        f.write(f'{result}\n')

テーマ
訪れた日
訪れた年月日
スポット名
スポットの名前