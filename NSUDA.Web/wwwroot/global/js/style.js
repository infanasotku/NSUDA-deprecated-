const headerSection = document.querySelector(".header_section");
const headWrapper  = document. querySelector(".head_wrapper");

function scaleFunction()
{
	const height = headerSection.offsetHeight;
  headWrapper.style.marginTop = height - 1 + "px"
  headWrapper.style.minHeight = Math.max(headerSection.offsetWidth / 1.96, 725) + "px";
  console.log(headWrapper.style.minHeight);
}

scaleFunction();

var scaleFuncs = [];
scaleFuncs.push(scaleFunction);

window.onzoom = function(e) {
  console.log(scaleFuncs);
  scaleFuncs.forEach(element => {
    element();
  });
}


function startListen() {
	var oldresize = window.onresize;
	window.onresize = function(e) {
      var event = window.event || e;
      if(typeof(oldresize) === 'function' && !oldresize.call(window, event)) {
        return false;
      }
      if(typeof(window.onzoom) === 'function') {
        return window.onzoom.call(window, event);
      }
  }
};

startListen();