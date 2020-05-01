; loop untuk mencetak 25 karakter dengan jumlah masing-masing 80

mov ah, 0
mov al, 3
int 10h

mov al, 'A'
mov bh, 0
mov bl, 0
mov cx, 80

mov dh, 0
mov dl, 0

mov cl, 25
A1:
    push cx
    mov ah, 9
    inc bl
    inc al
    mov cx, 80
    int 10h
    mov ah, 2
    inc dh
    int 10h
    pop cx
loop A1

; scroll atas
mov ah, 6 ; pilih library scroll
mov al, 1 ; naik berapa baris
mov bh, 01100000b ; mengisi daerah yang kosong (setelah scroll) dengan warna tertentu
mov ch, 1 ; index start (vertical) ???
mov cl, 2 ; index start (horizontal) ???
mov dh, 20 ; jumlah karakter (width/horizontal) yang kena scroll
mov dl, 30; jumlah karakter (height/vertical) yang kena scroll)

int 10h ; execute scroll