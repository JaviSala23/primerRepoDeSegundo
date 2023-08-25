mover=100
function alerta(){
    alert("Hizo click")
    boton1=document.getElementById("boton1")
    boton1.style.backgroundColor = "red";
    movido=mover.toString()+"px"
    boton1.style.fontSize="12px"
    boton1.style.width="100px"
    boton1.style.marginLeft=movido
    mover=mover+100
}