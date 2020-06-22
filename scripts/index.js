let signup_button=document.getElementById('signupContainer').onclick = function signup_scroll() {

  let form_container=document.getElementById('email_form');
  let svs=document.getElementById('video');
  let svs1=document.getElementById('shop');
  let svs2=document.getElementById('signupButton');
 
  if(form_container.style.opacity==0) {

  form_container.style.opacity=1;
  form_container.style.transform="translateY(-100%)";
  svs.style.transform="translateY(-130px)";
  svs1.style.transform="translateY(-130px)";
  svs2.style.transform="translateY(-130px)";

  }

  else  {

    form_container.style.opacity=0;
    form_container.style.transform="translateY(100%)";
    svs.style.transform="translateY(.5px)";
    svs1.style.transform="translateY(.5px)";
    svs2.style.transform="translateY(1px)";
  
  

  }
  
 }