# Команды командной строки
# 1) Загрузить из (Формат: pb_import --format path/file.name)  formats = [txt, csv, json, xml]
# ???1.1) на будущее отлавливать если файла не существует (писать ошибку)???
# 2) Выгрузить из (Формат: pb_export --format path/file.name)  formats = [txt, csv, json, xml]
# Выходные данные из 1 и 2: data = (imp or exp, format, path)
# 3) Добавить новую запись (Формат: pb_add Фамилия Имя Телефон Описание )
# Выходные данные как: date = (add, (фамилия, имя, телефон, описание))
# 4) Удалить запись "по фамилии" (Формат: pb_remove Фамилия) - удаляется первое вхождение
# Выходные данные как: date (remove, фамилия)
# 5) Показать data в консоли (модуль принимает data, выдает print в консоли)

# Данные справочника в системе выглядят как: data = [[Фамилия, Имя, Телефон, Описание],[Фамилия, Имя, Телефон...], ...]

