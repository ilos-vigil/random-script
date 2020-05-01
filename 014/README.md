# Assembly script collection

Some assembly script for Intel 8086. Tested with EMU8086 software.

## 01.asm

Calculate your final score and grade by inputting the score. Ignoring floating point.

* Formula

$$
\text{NA} = (N_{h1} + N_{h2} + N_{h3}) * 0.1 + N_{\text{UTS}} * 0.3 + N_{\text{UAS}} * 0.4
$$

* Grade table

| NA       | Grade       |
| -------- | ----------- |
| 80 - 100 | A           |
| 75 - 79  | B+          |
| 70 - 74  | B           |
| 65 - 69  | C+          |
| 60 - 64  | C           |
| 0 - 59   | TIDAK LULUS |

* Result

![Result](./img/01.asm.png)

## 02.asm

Read input, then store the input on text file `textfile.txt` in overwrite mode.

## 03.asm

Read text file `textfile.txt`, then print the read text

## 04.asm

Print a character multiple times with background

![Result](./img/04.asm.png)

## 05.asm

Print characters B-Z, each with width 25, then shift up some printed characters.

![Printed characters](img/05-1.asm.png)
![Shifted characters](img/05-2.asm.png)