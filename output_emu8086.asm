; Código Ensamblador generado por el compilador (emu8086)
#make_bin

.model small
.stack 100h

; === SECCIÓN DE DATOS (.data) ===
.data


; === SECCIÓN DE CÓDIGO (.code) ===
.code
main proc
    mov ax, @data
    mov ds, ax ; Establecer el segmento de datos

    ; Código del programa (instrucciones)
    
    ; Terminar el programa
    mov ah, 4ch
    int 21h
main endp
end main
