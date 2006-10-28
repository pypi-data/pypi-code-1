#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytils

# простая траслитерация/детранслитерация
# обратите внимание на то, что при транслитерации вход - unicode,
# выход - str, а в детранслитерации -- наоборот
#

print pytils.translit.translify(u"Это тест и ничего более")
#-> Eto test i nichego bolee

print pytils.translit.translify(u"Традиционно сложные для транслитерации буквы - подъезд, щука")
#-> Traditsionno slozhnyie dlya transliteratsii bukvyi - pod`ezd, schuka

# и теперь пытаемся вернуть назад... (понятно, что Э и Е получаются одинаково)
print pytils.translit.detranslify("Eto test i nichego bolee")
#-> Ето тест и ничего более

print pytils.translit.detranslify("Traditsionno slozhnyie dlya transliteratsii bukvyi - pod`ezd, schuka")
#-> Традиционно сложные для транслитерации буквы - подъезд, щука


# и пригодные для url и названий каталогов/файлов транслиты
# dirify и slugify -- синонимы, действия абсолютно идентичны
print pytils.translit.slugify(u"Традиционно сложные для транслитерации буквы - подъезд, щука")
#-> traditsionno-slozhnyie-dlya-transliteratsii-bukvyi-podezd-schuka

# обратного преобразования, понятно, нет :)
