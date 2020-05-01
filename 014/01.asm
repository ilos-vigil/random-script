; --- PRINT INFO
mov ah, 9
mov dx, offset info
int 21h
; --- END PRINT INFO




; --- INPUT NRP
; print carriage return & new line
mov ah, 2
mov dl, 10
int 21h
mov ah, 2
mov dl, 13
int 21h
; print string
mov ah, 9
mov dx, offset minta_nrp
int 21h
; input
mov ah, 0ah
mov dx, offset nrp
int 21h
; --- END INPUT NRP




; --- INPUT NILAI HARIAN 1
; print carriage return & new line
mov ah, 2
mov dl, 10
int 21h
mov ah, 2
mov dl, 13
int 21h
; print string
mov ah, 9
mov dx, offset minta_nh1
int 21h

; --- INPUT NILAI HARIAN 1 DIGIT 1
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; kali 10
mov bx, 10
mul bx
; push stack
push ax
; --- END NILAI HARIAN 1 DIGIT 1
; --- INPUT NILAI HARIAN 1 DIGIT 2
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; push stack
push ax
; --- END NILAI HARIAN 1 DIGIT 2
; --- END INPUT NILAI HARIAN 1




; --- INPUT NILAI HARIAN 2
; print carriage return & new line
mov ah, 2
mov dl, 10
int 21h
mov ah, 2
mov dl, 13
int 21h
; print string
mov ah, 9
mov dx, offset minta_nh2
int 21h

; --- INPUT NILAI HARIAN 2 DIGIT 1
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; kali 10
mov bx, 10
mul bx
; push stack
push ax
; --- END NILAI HARIAN 2 DIGIT 1
; --- INPUT NILAI HARIAN 2 DIGIT 2
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; push stack
push ax
; --- END NILAI HARIAN 2 DIGIT 2
; --- END INPUT NILAI HARIAN 2




; --- INPUT NILAI HARIAN 3
; print carriage return & new line
mov ah, 2
mov dl, 10
int 21h
mov ah, 2
mov dl, 13
int 21h
; print string
mov ah, 9
mov dx, offset minta_nh3
int 21h

; --- INPUT NILAI HARIAN 3 DIGIT 1
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; kali 10
mov bx, 10
mul bx
; push stack
push ax
; --- END NILAI HARIAN 3 DIGIT 1
; --- INPUT NILAI HARIAN 3 DIGIT 2
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; push stack
push ax
; --- END NILAI HARIAN 3 DIGIT 2
; --- END INPUT NILAI HARIAN 3




; --- INPUT NILAI UTS
; print carriage return & new line
mov ah, 2
mov dl, 10
int 21h
mov ah, 2
mov dl, 13
int 21h
; print string
mov ah, 9
mov dx, offset minta_nuts
int 21h

; --- INPUT NILAI UTS DIGIT 1
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; kali 10
mov bx, 10
mul bx
; push stack
push ax
; --- END NILAI UTS DIGIT 1
; --- INPUT NILAI UTS DIGIT 2
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; push stack
push ax
; --- END NILAI UTS DIGIT 2
; --- END INPUT NILAI UTS




; --- INPUT NILAI UAS
; print carriage return & new line
mov ah, 2
mov dl, 10
int 21h
mov ah, 2
mov dl, 13
int 21h
; print string
mov ah, 9
mov dx, offset minta_nuas
int 21h

; --- INPUT NILAI UAS DIGIT 1
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; kali 10
mov bx, 10
mul bx
; push stack
push ax
; --- END NILAI UAS DIGIT 1
; --- INPUT NILAI UAS DIGIT 2
; input
mov ah, 1
int 21h
; get real number
mov ah, 0
sub ax, 30h
; push stack
push ax
; --- END NILAI UAS DIGIT 2
; --- END INPUT NILAI UAS




; --- HITUNG NILAI UAS
mov ax, 0

pop bx
add ax, bx
pop bx
add ax, bx
; --- END HITUNG NILAI UAS




; --- HITUNG NILAI UTS
mov bx, 0

pop cx
add bx, cx
pop cx
add bx, cx
; --- END HITUNG NILAI UTS




; --- HITUNG NILAI HARIAN
mov cx, 0

; HARIAN 3
pop dx
add cx, dx
pop dx
add cx, dx
; HARIAN 2
pop dx
add cx, dx
pop dx
add cx, dx
; HARIAN 1
pop dx
add cx, dx
pop dx
add cx, dx
; --- END HITUNG NILAI HARIAN




; --- HITUNG PRESENTASE NILAI HARIAN
; push nilai UTS dan UAS ke stack, pindah nilai harian ke AX
push ax ; nilai uas
push bx ; nilai uts
mov ax, cx

; kali 1
mov bx, 1
mul bx
; bagi 10
mov bx, 10
div bx

; push presentase nilai harian
push ax
; --- END HITUNG PRESENTASE NILAI HARIAN




; --- HITUNG PRESENTASE NILAI UTS
; swap posisi stack
pop ax ; presentasi nilai harian
pop bx ; nilai uts
pop cx ; nilai uas
push ax ; presentasi nilai harian
push cx ; nilai uas
mov ax, bx


; kali 3
mov bx, 3
mul bx
; bagi 10
mov bx, 10
div bx

; push presentase nilai UTS
push ax
; --- END HITUNG PRESENTASE NILAI UTS




; --- HITUNG PRESENTASE NILAI UAS
; swap posisi stack
pop ax ; presentase nilai uts
pop bx ; nilai uas
pop cx ; presentasi nilai harian
push cx ; presentasi nilai harian
push ax ; presentasi nilai uts
mov ax, bx

; kali 4
mov bx, 4
mul bx
; bagi 10
mov bx, 10
div bx

; push presentasi nilai UAS
push ax
; --- END HITUNG PRESENTASE NILAI UAS




; --- HITUNG NILAI AKHIR
mov ax, 0

pop bx
add ax, bx
pop bx
add ax, bx
pop bx
add ax, bx

; push nilai akhir
push ax
; --- END HITUNG NILAI AKHIR




; --- PRINT OUTPUT
; print carriage return & new line
mov ah, 2
mov dl, 10
int 21h
mov ah, 2
mov dl, 13
int 21h

; print output1
mov ah, 9
mov dx, offset output1
int 21h

; print nrp
mov ah, 9
mov dx, offset nrp
int 21h

; print carriage return & new line
mov ah, 2
mov dl, 10
int 21h
mov ah, 2
mov dl, 13
int 21h

; print output2
mov ah, 9
mov dx, offset output2
int 21h

; --- PRINT NILAI AKHIR
; ambil nilai akhir dari stack
pop ax
push ax

mov bl, 10
div bl ; al : puluhan, ah : satuan

; pindah satuan ke CL
mov cx, 0
mov cl, ah

; print puluhan
mov dx, 0
mov dl, al
add dl, 30h
mov ah, 2
int 21h

; print satuan
mov dx, 0
mov dl, cl
add dl, 30h
mov ah, 2
int 21h
; --- END PRINT NILAI AKHIR

; print output3
mov ah, 9
mov dx, offset output3
int 21h
; --- END PRINT OUTPUT


; --- CARI GRADE
; pop nilai akhir ke CX
pop cx
; set print librar
mov ah, 2

; cari grade
cmp cx, 59
jle tidak_lulus
cmp cx, 64
jle grade_c
cmp cx, 69
jle grade_c_plus
cmp cx, 74
jle grade_b
cmp cx, 79
jle grade_b_plus
jg grade_a
; --- END




; --- PRINT GRADE
tidak_lulus:
    mov ah, 9
    mov dx, offset output_tidak_lulus
    int 21h
grade_c:
    mov dl, 'C'
    int 21h
    jmp exit
grade_c_plus:
    mov dl, 'C'
    int 21h
    mov dl, '+'
    int 21h
    jmp exit
grade_b:
    mov dl, 'B'
    int 21h
    jmp exit
grade_b_plus:
    mov dl, 'B'
    int 21h
    mov dl, '+'
    int 21h
    jmp exit
grade_a:
    mov dl, 'A'
    int 21h
    jmp exit
; --- END PRINT GRADE




; --- EXIT
exit:
    int 20h



; --- VARIABLE
info db 'Input nilai 2 digit$'
nrp db 10, ?, 10 dup(0), '$'
minta_nrp db 'NRP : $'
minta_nh1 db 'Nilai harian 1 : $'
minta_nh2 db 'Nilai harian 2 : $'
minta_nh3 db 'Nilai harian 3 : $'
minta_nuts db 'Nilai UTS : $'
minta_nuas db 'Nilai UAS : $'

output1 db 'NRP dengan $'
output2 db ' mendapatkan nilai mata kuliah dengan nilai akhir $'
output3 db ' dan grade $'
output_tidak_lulus db 'TIDAK LULUS$'