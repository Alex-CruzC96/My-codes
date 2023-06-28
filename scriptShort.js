//script para el menu desplegado

//variable activadora
var evento0=document.getElementById("foot");

//variables a activar
var despliegue_1=document.getElementById("menuAmpliado");
var despliegue_2=document.getElementById("userBar");

//variable global
var active=null;

//funcion
function getUserBar(){
    if(active==null){
        despliegue_1.classList.add("desplegado");
        despliegue_2.classList.add("desplegado");
        active=evento0;
    }
    else{
        despliegue_1.classList.remove("desplegado");
        despliegue_2.classList.remove("desplegado");
        active=null;
    }
}
evento0.addEventListener('click',getUserBar);
//script para las sublistas

//variables activadoras
var evento1=document.getElementById("cie");
var evento2=document.getElementById("historial");
var evento3=document.getElementById("bajas");
var evento4=document.getElementById("reinscripcion");

//variables a activar
var innerListOne=document.getElementById("despliegue");
var innerListTwo=document.getElementById("despliegue2");
var innerListThree=document.getElementById("despliegue3");
var innerListFour=document.getElementById("despliegue4");

//funcion

//variable global
var globalVar=false;
//variable auxiliar
var aux=null;
var aux2=null;
//funcion general
function deployment(object, evento){
    //valora si ya hay algo activo
    if(globalVar){
        //si la hay valora si el nuevo evento es el mismo al ya activado
        if(object==aux){
            //de serlo elimina las clases al evento nuevo que es el mismo al viejo y la globalVar se niega
            object.classList.remove("desplegado");
            evento.classList.remove("desplegado");
            globalVar=false;
        }
        else{
            //de no serlo se eliminan las clases al evento viejo almacenado en los auxiliares
            aux.classList.remove("desplegado");
            aux2.classList.remove("desplegado");
            //agrega las clases al nuevo evento
            object.classList.add("desplegado");
            evento.classList.add("desplegado");
        }
    }
    else{
        //de no haber nada activo la globalVar se valora como cierta y se agregan las clases a los eventos
        globalVar=true;
        object.classList.add("desplegado");
        evento.classList.add("desplegado");
    }
    //se almacenan los eventos que acaban de ocurrir
    aux=object;
    aux2=evento;
}

evento1.addEventListener('click',function(){deployment(innerListOne,evento1);});
evento2.addEventListener('click',function(){deployment(innerListTwo,evento2);});
evento3.addEventListener('click',function(){deployment(innerListThree,evento3);});
evento4.addEventListener('click',function(){deployment(innerListFour,evento4);});

