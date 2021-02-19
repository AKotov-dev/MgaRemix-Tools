The document is currently being translated...


Инструкция по cборке флешки MgaRemix
---

Всю процедуру сборки загрузочной флешки MgaRemix можно разделить на 5 шагов:

1. Создание пустой загрузочной флешки
2. Установка и настройка Mageia Linux в VirtualBox
3. Создание внутри гостевой ОС специальных `vmlinuz` и `initrd.gz` для загрузки с флешки с помощью скрипта `initrd-builder`
4. Конвертирование в основной ОС файла виртуальной машины в файл `*.sqfs` с помощью конвертера `vdi-to-sqfs-converter`
5. Копирование полученного файла `distrib-lzma.sqfs` в папку `/loopbacks` на флешке

**Действия по пунктам:**

- Возьмите флешку с файловой системой FAT32 (родная ФС для флешек) размером от 4 ГБ:

> Скачайте архив `MgaRemix-LiveUSB-Loader-xx.zip` и распакуйте его в корень флешки. На флешке должна получиться структура каталогов:

/boot
/EFI
/loopbacks

Сделайте флешку загрузочной. Для этого запустите скрипт `Флешка/boot/syslinux/BootInstall.bat` (su/password в Linux или под Администратором в Windows) и нажмите Enter. После установки загрузчика метка флешки изменится на `MGAREMIX`.
- Установка Mageia Linux в Virtual Box в этой инструкции не рассматривается, поскольку приступая к созданию флешки MgaRemix подразумевается, что пользователь умеет это делать. Настройки виртуальной системы зависят только от фантазии сборщика. Разметка диска – корень + своп.
- Находясь в виртуальной машине, скачиваем пакет `initrd-builder-2.1-1.mrxX.noarch.rpm` и устанавливаем его. Даём команду: `initrd-builder`. По окончанию операции в каталоге `~/initrd-buider` будут созданы файлы `initrd.gz` и `vmlinuz`. Подключаем созданную ранее загрузочную флешку к виртуальной машине и копируем эти файлы в каталог `/boot` на ней. Извлекаем флешку (правая кнопка мыши – «Извлечь») и отключаем её от виртуальной машины через меню VirtualBox. Выключаем виртуальную машину и переходим в основную ОС.
- Находясь в основной системе скачиваем файл `vdi-to-sqfs-converter.tar.gz`. Заходим в терминал (su/пароль). Распаковываем скачанный архив конвертера и закидываем к нему в каталог файл виртуальной машины с расширением `*.vdi`. Запускаем скрипт `converter.sh` и конвертируем виртуальную машину в формат `*.sqfs`.

Примечание: работающим в Windows следует держать ещё одну виртуалку для конвертирования.

- Переносим полученный файл `distrib-lzma.sqfs` на флешку в каталог `/loopbacks`. На этом создание флешки завершено.

МgaRemix умеет работать с сохранением. Для этого достаточно распаковать в корень флешки один из архивов, содержащий образ «диска сохранения» размером 1,2,3 или 4GB. Скачать можно из каталога `persistence-images`. 

Важно! В режиме с сохранением, следует использовать быстрые флешки со скоростью записи от 8МБ/Сек.  Качество флешки в Linux можно проверить программой f3 или KSiskMark.

**Дополнительные рекомендации:**

После установки и окончательной настройки гостевой ОС, можно оптимизировать и прибрать систему: очистить от ненужных пакетов и ядер с помощью программы `SCleaner`, удалить пакеты `iptables, msec, shorewall-core, mgaonline, mageiawelcome` чтобы не иметь проблем с коннектом и не нагружать систему при первом старте.

Для уменьшения размера финального distrib-lzma.sqfs  в гостевой ОС нужно выполнить от root команду:
`dd if=/dev/zero of=/zerofile bs=4096 status=progress; rm -f /zerofile`
(сообщение о нехватке места на диске игнорируем)

После этого нужно выключить виртуальную машину и в основной ОС сжать `*.vdi` виртуальной машины. В Windows для сжатия VDI можно использовать графическую утилиту `CloneVDI`. Перед сжатием галки «Keep Old UUID» и «Compact drive while copying» должны быть установлены. Для сжатия `*.vdi` в Linux используйте графическую утилиту VDIComp.

После сжатия файл `*.vdi` отправляется в конвертер `vdi-to-sqfs-converter`.


Весь проект MgaRemix: https://cloud.mail.ru/public/59BZ/3Nev2XbrV

