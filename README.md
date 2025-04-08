Herramienta de postexplotación para enumerar binarios con capabilities y permisos SUID de manera automatizada.

## Uso

1 - Compartir el comprimido a la máquina víctima

2 - Descomprimir el .zip y ejecutarlo

```bash
unzip binEnums.zip
cd enumSUID
chmod +x enumSUID.py
./enumSUID.py -sc
```
[Opciones]

-c: Enumerar binarios con capabilities vulnerables
-s: Enumerar binarios con permiso SUID vulnerables
-sc: Ambas

Ejemplo:

![2025-04-08_08-54](https://github.com/user-attachments/assets/e348c3da-5718-4482-9db7-9f03680176e1)
