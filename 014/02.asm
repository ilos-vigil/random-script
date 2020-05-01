; open and write a file

mov ah, 3dh ; pakai 3ch untuk overwrite file
mov dx, offset filename
mov al, 2h
int 21h
mov filehandle, ax

jc errmsg

mov ah, 0ah
mov dx, offset inputan
int 21h

mov ah, 40h
mov bx, filehandle
mov dx, offset inputan + 2
mov ch, 0
mov cl, inputan + 1
int 21h

jmp exit

errmsg:
    mov ah, 9h
    mov dx, offset errmessage
    int 21h

exit:
    int 20h


filehandle dw 0
filename db 'textfile.txt', 0
errmessage db 'ERROR, GAGAL BUKA FILE $'
inputan db 100, 0, 30 dup(0)