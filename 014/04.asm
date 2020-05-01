; text with color (bertumpukan)

mov ah, 0
mov al, 3
int 10h

mov ah, 9
mov al, 'a'
mov bh, 0
mov bl, 00101100b ; set warna
mov cx, 10 ; jumlah karakter 'a' yg dicetak
int 10h

mov ah, 9
mov al, 'b'
mov bh, 1
mov bl, 01001001b
mov cx, 10
int 10h

mov ah, 5
mov al, 1
int 10h