After installation, go to the terminal (su/password) and run initrd-builder.
The result is located in the ~/initrd-builder folder. Copy the initrd.gz and vmlinuz
files to the /boot folder on the MgaRemix flash drive.
Additional command that frees up space on the VM disk: /usr/bin/compact
...
More information: /usr/share/doc/package_name/repack.txt


Начиная с initrd-builder-v2.3-0 добавлен сервис DrakXbootPatch.service, устраняющий проблему обновления при установке с LiveUSB.

Тема:
---
Live-ISO Mageia (Plasma, XFCE, GNOME; x86_64/i586): Ошибка обновления ядра после установки с флешки в режиме BIOS (не EFI).

Описание проблемы:
---
После записи любых LiveDVD Mageia (?,8,9) на USB-drive установка в режиме BIOS (НЕ EFI) с них происходит неверно! Ошибка делает невозможным дальнейшее обновление ядра в установленной системе! Ядро всё время будет старым!

Объяснение и простейший пример:
---
Запишите любой Live-образ Mageia на флешку (isodumper, RosaImageWriter, dd, etc). Загрузитесь с флешки в режиме BIOS (НЕ EFI).

После загрузки с флешки в режиме BIOS (НЕ EFI), флешка становится /dev/sda.

Запускаем draklive-install... Установка происходит на диск /dev/sdb, о чем свидетельствуют записи в /etc/fstab в уже установленной системе.

Извлекаем флешку, перезагружаем систему; она успешно загружается, поскольку в /etc/fstab обращения к разделам по UUID. 

Пробуем обновить ядро в установленной системе:
---
> urpmi.update -a && urpmi --auto kernel-desktop
medium "Core Release" is up-to-date
medium "Core Updates" is up-to-date
medium "Nonfree Release" is up-to-date
    $MIRRORLIST: media/nonfree/updates/media_info/20230911-130132-synthesis.hdlist.cz
updated medium "Nonfree Updates"                                                                         

    $MIRRORLIST: media/core/updates/kernel-desktop-6.5.13-6.mga9.i586.rpm
installing kernel-desktop-6.5.13-6.mga9.i586.rpm from /var/cache/urpmi/rpms                                               
Preparing...                     ########################################################################################
      1/1: kernel-desktop        ########################################################################################
INTERNAL ERROR: unknown device sdb
MDK::Common::Various::internal_error() called from /usr/lib/libDrakX/devices.pm:131
devices::entry() called from /usr/lib/libDrakX/devices.pm:146
devices::make() called from /usr/lib/libDrakX/partition_table/raw.pm:60
partition_table::raw::typeOfMBR() called from /usr/lib/libDrakX/bootloader.pm:316
bootloader::read() called from /sbin/bootloader-config:64

Причина ошибки:
---
draklive-install/DrakX записывает в /boot/grub2/install.sh команду:
grub2-install /dev/sdb

Однако, основной диск после установки с флешки уже не /dev/sdb, а /dev/sda! GRUB располагается на /dev/sda, а не на /dev/sdb!

Решение:
---
Исправляем букву диска в файле /boot/grub2/install.sh
grub2-install /dev/sda

...и пробуем повторно обновить ядро

> urpme kernel-desktop-6.5.13-6.mga9.i586
removing kernel-desktop-6.5.13-6.mga9.i586
removing package kernel-desktop-6.5.13-6.mga9.i586
      1/1: removing kernel-desktop-6.5.13-6.mga9.i586
                                 ########################################################################################
> urpmi --auto kernel-desktop

    $MIRRORLIST: media/core/updates/kernel-desktop-6.5.13-6.mga9.i586.rpm
installing kernel-desktop-6.5.13-6.mga9.i586.rpm from /var/cache/urpmi/rpms                                               
Preparing...                     ########################################################################################
      1/1: kernel-desktop        ########################################################################################
remove-boot-splash: Format of /boot/initrd-6.5.13-desktop-6.mga9.img not recognized
You should restart your computer for kernel-desktop


* В режиме установки EFI в /boot/grub2/install.sh диск не пишется, только команда:
grub2-install
