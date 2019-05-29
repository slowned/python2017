# Compilación de sistemas con Buildroot

1. Clonar Buildroot desde su repositorio usando git.

  ```console
  git clone --depth=1 --branch=2018.08 git://git.busybox.net/buildroot
  cd buildroot
  make menuconfig
  ```
  - Al hacer *_make menuconfig_* por primera vez fallo, por faltas de dependencias, lo solucione instalas via *_apt-get install_*

>   **Buildroot configuration**
> - Target options --->
> -   Target Architecture (i386)
> - Build options ---> 
> - Toolchain --->
> -   Compile and install uClibc utilities # defaul
> - Sustem configuration --->
> -   Enable root login with password # defaul
> -   Run aa getty (login prompt) after boot # defaul
> -   Purge unwanted locales # ya estaba
> - Kernel --->
> -   Linux Kernel (lastest version (3.17))
> -   Custom Kernel patches 
> -   Kernel configuration
> -      () Using an in-tree defconfig file
> -      () Use the arcitecture default configuration
> -      (X) Using a custom (def)config file
> -      ($(TOPDIR)/boards/qemu/x86/linux.config)
> - Target packages --->
> - Filesystem images --->
> -   cipio the root filesystem
> -     Compression method (xz)
> -   ext2/3/4 root filesystem
> -      (X) ext2 (rev0)
> -      (X) ext4
> -
> - Bootloaders --->
> -   syslinux (mbr)
> 
> - Host utilities --->
> - Legacy config options --->

Save and Exit!

  Compilar la imagen (puede tomar su tiempo)  

```console
make
```
  Una ves creada la imagen, tiene que aparecer los siguientes archivos:

> output/images/rootfs.cpio.gz
> output/images/rootfs.tar


#### **Make** prueba uno: Error!

```console
nux/linux.mk:511: *** No kernel defconfig name specified, check your BR2_LINUX_KERNEL_DEFCONFIG setting.  Stop.
Makefile:79: recipe for target '_all' failed
make: *** [_all] Error 2
```
* **Solucion:**
    Abrir el menu de configuraciones de buildroot acceder al a las configuraciones del Kernel, ahi vi que en la opcion de arquitectura estaba seleccionada la opcion *_Using an in-tree defconfig file_* 

    () Using an in-tree defconfig file
    (X) Use the arcitecture default configuration
    () Using a custom (def)config file

Guardar y generar la imagen.


#### **Make** prueba dos: Error!

```console
mkdir -p /home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/host/bin
/usr/bin/install -c pkgconf /home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/host/bin/pkgconf
/usr/bin/install: cannot create regular file '/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/host/bin/pkgconf': Permission denied
Makefile:33: recipe for target 'install' failed
make[2]: *** [install] Error 1
package/pkg-generic.mk:239: recipe for target '/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/build/host-pkgconf-0.9.12/.stamp_host_installed' failed
make[1]: *** [/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/build/host-pkgconf-0.9.12/.stamp_host_installed] Error 2
Makefile:79: recipe for target '_all' failed
make: *** [_all] Error 2
```
* **Solucion:**
```console
sudo make
```

#### **Make** prueba tres: Error!

```console
linux 4.17.19 Patching
if [ -f /home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/build/linux-4.17.19/tools/perf/Documentation/Makefile ]; then printf "%%:\n\t@:\n" >/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/build/linux-4.17.19/tools/perf/Documentation/GNUmakefile; fi
for p in /home/ma/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/board/qemu/x86 ; do if test -d $p ; then PATH=/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/host/bin:$PATH support/scripts/apply-patches.sh  /home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/build/linux-4.17.19 $p \*.patch || exit 1 ; else PATH=/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/host/bin:$PATH support/scripts/apply-patches.sh  /home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/build/linux-4.17.19 `dirname $p` `basename $p` || exit 1; fi done
Aborting.  '/home/ma/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/board/qemu' is not a directory.
package/pkg-generic.mk:193: recipe for target '/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/build/linux-4.17.19/.stamp_patched' failed
make: *** [/home/mariano/Documents/UNLP/SO/ENTREGABLE_1/buildroot/output/build/linux-4.17.19/.stamp_patched] Error 1
```

* **Solucion:**
    El problema fue que se in gresaron las configuraciones de linux en un lugar incorrecto.
    Entrar al menu de configuraciones del buildroot, ir a las opciones de configuracion de Kernel seleccionar (def)config y agregar el path del archivo __linux.config__

> - Kernel --->
> -   Linux Kernel (lastest version (3.17))
> -   Custom Kernel patches 
> -   Kernel configuration
> -      () Using an in-tree defconfig file
> -      () Use the arcitecture default configuration
> -      (X) Using a custom (def)config file
> -      ($(TOPDIR)/boards/qemu/x86/linux.config)

* Ahora si! una vez que solucione los errores generamos la imagen.

```console
sudo make
> /buildroot/output/images/rootfs.cpio.xz
> /buildroot/output/images/rootfs.ext4
```
Se generaron 2 files nuevos

### Comprobacion de Archivos 
Pararnos sobre __/buildroot/output/images__ y ejecutar los siguientes comandos


* Para probar que la imagen rootfs.cpio.xz se generó adecuadamente, se puede utilizar
el siguiente comando de KVM/Qemu:

```console
sudo kvm -m 512 -kernel bzImage
-initrd rootfs.cpio.xz
```

* Para probar que la imagen rootfs.ext4 se generó adecuadamente se puede utilizar el 
siguiente comando de KVM/Qemu que hace que la imagen se vea en el sistema guest como
un disco:

```console
kvm -m 512 -kernel bzImage rootfs.ext4
```
Al ejecutar estos comandos se abre una consola Qemu indicandonos que las imagenes se generaron
sin errores

* Finalmente para completar el trabajo haciendo que rootfs.cpio.xz se comporte como un
initramfs u rootfs.ext4 bootee imprimiendo el mensaje "Hola...":

```console
kvm -m 512 -kernel bzImage -initrd rootfs.cpio.xz\
-append root=/dev/sda rootfs.ext4
```

Para hacer este ultimo paso hice lo siguiente

* **Extraer el archivo cpio.xz:**
  El archivo “cpio.xz” es un archivo empaquetado y comprimido de forma análoga a “tar.xz”.
Por lo cuál puede ser manipulado con las herramientas __xz__

**extraer como usuario root**

```console
unxz rootfs.cpio.xz
mkdir miinit && cd miinit
sudo cpio -i < ../rootfs.cpio
> root.cpio
rm sbin/init
```

***darles permisos de ejecucion***

```console
chmod +x init (script de saludo)
```

```console
sudo mount -o loop=rootfs.ext4 mnt/
mnt/etc/init.d >> ahi estan los scripts de inicio
```

**El mount de /dev que estaba acá no es necesario**
/bin/mount -t proc proc /proc

* Pasar el control del initramfs al filesystem almacenado en disco (rootfs.ext4) se puede resumir
en una breve serie de pasos:
  * Extraer el path al filesystem desde /proc/cmdline (opción root).
  * Montar el filesystem en una carpeta, por ejemplo /mnt
  * Hacer que ese sea el nuevo root y pasar el control al init almacenado en el filesystem con switch_root.

```bash
#!/bin/sh
/bin/mount -t proc proc /proc
/bin/mount -o remount,rw /
/bin/mkdir -p /dev/pts /dev/shm
/bin/mount -a
/sbin/swapon -a
/bin/ln -sf /proc/self/fd /dev/fd
/bin/ln -sf /proc/self/fd/0 /dev/stdin
/bin/ln -sf /proc/self/fd/1 /dev/stdout
/bin/ln -sf /proc/self/fd/2 /dev/stderr
/bin/hostname -F /etc/hostname

# Código de ustedes...
IFS="=";
aux=""
directory=""
for param in $@; do
  IFS=" ";
  for prm in $param; do
    if [ "$prm" == "root" ]; then
      aux=$prm;
    elif [ "$aux" == "root" ]; then
      directory=$prm;
      unset aux;
      aux=" fasdfsdf ";
    fi
  done
done

# Montar el rootfs...

#mount --move $M /mnt/rootfs 

#$ #(switch_root /mnt/rootfs)
```

volver a comprimir
```console
sudo su
find .| cpio -H newc -o | sudo xz --check=crc32 > ../miinit.cpio.xz
```




```console
sudo cpio rootfs.cpio /proc/cmdline
```


proc/cmdline dice donde esta montado el /ext4

----------------------------------------
## Comandos utiles
#### CPIO
  * sirve para copiar archivos entre archivos y directorios, soporta varios formatos (binario, varios formatos tar, etc).

#### MOUNT
  * Monta un filesystem

  ```console
  mount -t type divice dir
  ```
  - Esto le dice al kernet que asocie el filesystem que se encuentra en divice (que es del tipo de type) en el directorio dir.
  La opcion -t type es opcional.


  * Lista filesystems montados (de un type)

  ```console
  mount [-l] [-t type]
  ```

#### SWITCH_ROOR
  * Mueve las particiones montadas existentes a una nueva raiz y hace de esta la nueva raiz inicial del filesystem y junto con sus procesos de inicio **init**

  ```console
  switch_root newroot init [args..]
  ```

#### xz
  * Es una erramienta de compresion y descompresion de archivos con una sintaxis similar a las de __gzip__.
-----------------------------------------
