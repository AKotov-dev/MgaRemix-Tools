Instructions for assembling the MgaRemix flash drive
---

The entire procedure for assembling a bootable MgaRemix flash drive can be divided into 5 steps:

1. Creating an empty bootable USB flash drive
2. Installing and configuring Mageia Linux in VirtualBox
3. Creating special `vmlinuz` and `initrd.gz` inside the guest OS with using the `initrd-builder` script
4. Convert a VM file to a `*.sqfs` file in the main OS using the `vdi-to-sqfs-converter' converter
5. Copy the resulting file `distrib-lzma.sqfs` to the `/loopbacks` folder on the flash drive

**Actions on items:**

- Take a flash drive with a FAT32 file system (native FS for flash drives) with a size of 4 GB or more
- Download the archive `MgaRemix-LiveUSB-Loader-xx.zip` and unzip it to the root of the flash drive. On the flash drive, you should get a directory structure:

>/boot  
>/EFI  
>/loopbacks

- Make the flash drive bootable. To do this, run the script `Flash_drive/boot/syslinux/BootInstall.bat` (su/password on Linux or under Administrator on Windows) and press Enter. After installing the bootloader, the label of the flash drive will change to 'MGAREMIX'.
- Installing Mageia Linux in a Virtual Box is not considered in this manual, since starting to create a flash drive MgaRemix implies that the user knows how to do it. The settings of the virtual system depend only on the imagination of the collector. Disk layout – root + swap.
- While in the VM, download the package 'initrd-builder-2.1-1. mrxX.noarch` rpm' and install it. We give the command ` 'initrd-builder'. At the end of the operation, the files `~/initrd-buider` will be created in the `~/initrd-buider` directory `initrd.gz` and `vmlinuz`. Connect the previously created bootable flash drive to the VM and copy these files to the `/boot` directory on it. Remove the flash drive (right mouse button – "Extract") and disconnect it from the virtual machine via the VirtualBox menu. Turn off the VM and switch to the main OS.
- While in the main system, download the file `vdi-to-sqfs-converter.tar.gz`. Go to the terminal (su/password). Unpack the downloaded converter archive and throw a virtual machine file with the extension `*.vdi` into its directory. Run the script `converter.sh` and convert the VM to the `*.sqfs` format. Those working in Windows should keep another virtual machine for converting.

- Transfer the resulting file `distrib-lzma.sqfs` to the flash drive in the directory `/loopbacks`. This completes the creation of the flash drive.

MgaRemix is able to work with saving. To do this, it is enough to unpack one of the archives containing the image of the "save disk" in the size of 1,2,3 or 4GB into the root of the flash drive. You can download it from the `persistence-images` directory.

Important! In the save mode, you should use fast flash drives with a write speed of 8 MB/sec. The quality of the flash drive in Linux can be checked by the program f3 or KDiskMark.

**Additional recommendations:**

After the installation and final configuration of the guest OS, you can optimize and clean up the system: clean up unnecessary packages and cores using the program 'SCleaner', remove the packages `iptables, msec, shorewall-core, mgaonline, mageiawelcome` so as not to have problems with the connection and not load the system at the first start.

To reduce the size of the final `distrib-lzma. sqfs` in the guest OS, you need to run the command from root:
`dd if=/dev/zero of=/zerofile bs=4096 status=progress; rm -f /zerofile`
(we ignore the message about the lack of disk space)

After that, you need to turn off the VM and compress `*.vdi` of the virtual machine. On Windows, you can use the `CloneVDI` graphical utility to compress VDI. Before compressing, the "Keep Old UUID" and "Compact drive while copying" checkboxes must be set. To compress `*.vdi` on Linux, use the VDIComp graphical utility.

After compressing the file `*.vdi` is sent to the `vdi-to-sqfs-converter`.

**Possible problems:**

If you previously installed GRUB on the flash drive, you will need to delete all the partitions on it and restore the MBR. On Linux, you can use Gparted. In Windows, you can delete flash drive partitions using ROSA ImageWriter or Image Tool. After deleting the partitions, you will need to reformat (FAT32).

The entire MgaRemix project: https://cloud.mail.ru/public/59BZ/3Nev2XbrV



Инструкция по cборке флешки MgaRemix
---

Всю процедуру сборки загрузочной флешки MgaRemix можно разделить на 5 шагов:

1. Создание пустой загрузочной флешки
2. Установка и настройка Mageia Linux в VirtualBox
3. Создание внутри гостевой ОС специальных `vmlinuz` и `initrd.gz` с помощью скрипта `initrd-builder`
4. Конвертирование в основной ОС файла виртуальной машины в файл `*.sqfs` с помощью конвертера `vdi-to-sqfs-converter`
5. Копирование полученного файла `distrib-lzma.sqfs` в папку `/loopbacks` на флешке

**Действия по пунктам:**

- Возьмите флешку с файловой системой FAT32 (родная ФС для флешек) размером от 4 ГБ
- Скачайте архив `MgaRemix-LiveUSB-Loader-xx.zip` и распакуйте его в корень флешки. На флешке должна получиться структура каталогов:

>/boot  
>/EFI  
>/loopbacks

- Сделайте флешку загрузочной. Для этого запустите скрипт `Флешка/boot/syslinux/BootInstall.bat` (su/password в Linux или под Администратором в Windows) и нажмите Enter. После установки загрузчика метка флешки изменится на `MGAREMIX`.
- Установка Mageia Linux в Virtual Box в этой инструкции не рассматривается, поскольку приступая к созданию флешки MgaRemix подразумевается, что пользователь умеет это делать. Настройки виртуальной системы зависят только от фантазии сборщика. Разметка диска – корень + своп.
- Находясь в виртуальной машине, скачиваем пакет `initrd-builder-2.1-1.mrxX.noarch.rpm` и устанавливаем его. Даём команду: `initrd-builder`. По окончанию операции в каталоге `~/initrd-buider` будут созданы файлы `initrd.gz` и `vmlinuz`. Подключаем созданную ранее загрузочную флешку к виртуальной машине и копируем эти файлы в каталог `/boot` на ней. Извлекаем флешку (правая кнопка мыши – «Извлечь») и отключаем её от виртуальной машины через меню VirtualBox. Выключаем виртуальную машину и переходим в основную ОС.
- Находясь в основной системе скачиваем файл `vdi-to-sqfs-converter.tar.gz`. Заходим в терминал (su/пароль). Распаковываем скачанный архив конвертера и закидываем к нему в каталог файл виртуальной машины с расширением `*.vdi`. Запускаем скрипт `converter.sh` и конвертируем виртуальную машину в формат `*.sqfs`. Работающим в Windows следует держать ещё одну виртуалку для конвертирования.

- Переносим полученный файл `distrib-lzma.sqfs` на флешку в каталог `/loopbacks`. На этом создание флешки завершено.

МgaRemix умеет работать с сохранением. Для этого достаточно распаковать в корень флешки один из архивов, содержащий образ «диска сохранения» размером 1,2,3 или 4GB. Скачать можно из каталога `persistence-images`. 

Важно! В режиме с сохранением, следует использовать быстрые флешки со скоростью записи от 8МБ/Сек.  Качество флешки в Linux можно проверить программой f3 или KDiskMark.

**Дополнительные рекомендации:**

После установки и окончательной настройки гостевой ОС, можно оптимизировать и прибрать систему: очистить от ненужных пакетов и ядер с помощью программы `SCleaner`, удалить пакеты `iptables, msec, shorewall-core, mgaonline, mageiawelcome` чтобы не иметь проблем с коннектом и не нагружать систему при первом старте.

Для уменьшения размера финального `distrib-lzma.sqfs`  в гостевой ОС нужно выполнить от root команду:
`dd if=/dev/zero of=/zerofile bs=4096 status=progress; rm -f /zerofile`
(сообщение о нехватке места на диске игнорируем)

После этого нужно выключить виртуальную машину и в основной ОС сжать `*.vdi` виртуальной машины. В Windows для сжатия VDI можно использовать графическую утилиту `CloneVDI`. Перед сжатием галки «Keep Old UUID» и «Compact drive while copying» должны быть установлены. Для сжатия `*.vdi` в Linux используйте графическую утилиту VDIComp.

После сжатия файл `*.vdi` отправляется в конвертер `vdi-to-sqfs-converter`.

**Возможные проблемы:**

Если ранее на флешку ставился GRUB, потребуется удалить на ней все разделы и восстановить MBR. В Linux можно воспользоваться Gparted. В Windows можно удалить разделы флешки с помощью ROSA ImageWriter или Image Tool. После удаления разделов потребуется переформатирование (FAT32).

Весь проект MgaRemix: https://cloud.mail.ru/public/59BZ/3Nev2XbrV

