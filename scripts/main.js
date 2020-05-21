istoggled=false;



function myFunction() {

  
  var node=document.getElementById("dropf-menu");

  node.style.display="block";

  if (istoggled) 
      node.style.display="none";
  else
      node.style.display="block";
  istoggled=!istoggled;

}