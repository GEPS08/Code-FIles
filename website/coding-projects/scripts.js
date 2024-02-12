let hamanimtog = true;

function menu (x) {
  hamanim(x);

  if (hamanimtog){
    closeMenu();
    console.log("closing menu")
  } else {
    openMenu();
    console.log("opening menu")
  }
}

function hamanim(x) {
  x.classList.toggle("change");
  hamanimtog = hamanimtog !== true;
}

function openMenu() {
  document.getElementById("menu").style.height = "100%";
}

function closeMenu() {
  document.getElementById("menu").style.height = "0%";
}