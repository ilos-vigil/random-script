; open and read a file

mov ah, 3dh
mov dx, offset filename
mov al, 2h
int 21h
mov filehandle, ax

jc errmsg

mov ah, 3fh
mov bx, filehandle
mov dx, offset isifile
mov cx, 100
int 21h

mov ah, 9h
mov dx, offset isifile
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
isifile db 100 dup('$')