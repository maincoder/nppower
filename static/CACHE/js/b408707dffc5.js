;var searchvisible=0;$("#search-menu").click(function(e){e.preventDefault();var val=$('#search-icon');if(val.hasClass('ion-ios-search-strong')){val.addClass('ion-ios-close-empty');val.removeClass('ion-ios-search-strong');}
else{val.removeClass('ion-ios-close-empty');val.addClass('ion-ios-search-strong');}
if(searchvisible===0){$("#search-form").slideDown(200);$("#s").focus();searchvisible=1;}
else{$("#search-form").slideUp(200);searchvisible=0;}});/*!
 * classie - class helper functions
 * from bonzo https://github.com/ded/bonzo
 * 
 * classie.has( elem, 'my-class' ) -> true/false
 * classie.add( elem, 'my-new-class' )
 * classie.remove( elem, 'my-unwanted-class' )
 * classie.toggle( elem, 'my-class' )
 */(function(window){'use strict';function classReg(className){return new RegExp("(^|\\s+)"+className+"(\\s+|$)");}
var hasClass,addClass,removeClass;if('classList'in document.documentElement){hasClass=function(elem,c){return elem.classList.contains(c);};addClass=function(elem,c){elem.classList.add(c);};removeClass=function(elem,c){elem.classList.remove(c);};}
else{hasClass=function(elem,c){return classReg(c).test(elem.className);};addClass=function(elem,c){if(!hasClass(elem,c)){elem.className=elem.className+' '+c;}};removeClass=function(elem,c){elem.className=elem.className.replace(classReg(c),' ');};}
function toggleClass(elem,c){var fn=hasClass(elem,c)?removeClass:addClass;fn(elem,c);}
var classie={hasClass:hasClass,addClass:addClass,removeClass:removeClass,toggleClass:toggleClass,has:hasClass,add:addClass,remove:removeClass,toggle:toggleClass};if(typeof define==='function'&&define.amd){define(classie);}else{window.classie=classie;}})(window);(function(){var triggerBttn=document.getElementById('trigger-overlay'),overlay=document.querySelector('div.overlay'),closeBttn=overlay.querySelector('button.overlay-close');transEndEventNames={'WebkitTransition':'webkitTransitionEnd','MozTransition':'transitionend','OTransition':'oTransitionEnd','msTransition':'MSTransitionEnd','transition':'transitionend'},transEndEventName=transEndEventNames[Modernizr.prefixed('transition')],support={transitions:Modernizr.csstransitions};function toggleOverlay(){if(classie.has(overlay,'open')){classie.remove(overlay,'open');classie.add(overlay,'close');var onEndTransitionFn=function(ev){if(support.transitions){if(ev.propertyName!=='visibility')return;this.removeEventListener(transEndEventName,onEndTransitionFn);}
classie.remove(overlay,'close');};if(support.transitions){overlay.addEventListener(transEndEventName,onEndTransitionFn);}
else{onEndTransitionFn();}}
else if(!classie.has(overlay,'close')){classie.add(overlay,'open');}}
triggerBttn.addEventListener('click',toggleOverlay);closeBttn.addEventListener('click',toggleOverlay);})();