const multiSelectWithoutCtrl = ( elemSelector ) => {

  let options = document.querySelectorAll(`${elemSelector} option`);

  options.forEach(function (element) {
      element.addEventListener("mousedown",
          function (e) {
              e.preventDefault();
              element.parentElement.focus();
              this.selected = !this.selected;
              return false;
          }, false );
  });

}


multiSelectWithoutCtrl('.genres-option')