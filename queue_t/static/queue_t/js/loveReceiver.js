// set uid if none exists
var myUID = Cookies.get("myUID");
if (!myUID) {
  var myUID = Date.now() % 10000;
  Cookies.set('myUID', myUID, { SameSite: 'Lax' });
}

// setup websocket

var socket = new WebSocket('ws://' + window.location.host + '/ws/queue_t');

// handle received websockets
// store info in cookies
// love may not be eternal
// but your love data is!
 socket.onmessage = function(receivedMessage) {
   console.log(receivedMessage.data);
   var received = JSON.parse(receivedMessage.data);
   // console.log();
   if (received.uid != myUID) {
     // info for lovetracker
     if (received.ahead) {
       // let ahead = Cookies.get("ahead");
       let ahead = getCookie("ahead");
       if (received.ahead && ahead) {
         let lc = Cookies.get("latestCommon1");
         Cookies.set('ahead', false, { SameSite: 'Lax' });
         Cookies.set('otherAhead', false, { SameSite: 'Lax' });
         Cookies.set("latestCommon1", parseInt(lc) + 1, { SameSite: 'Lax' });
         // createCookie("ahead", false);
         // createCookie("otherAhead", false);
         // createCookie("latestCommon", parseInt(lc) + 1);
       } else if (received.ahead && !ahead) {
         // Cookies.set('otherAhead', true, { SameSite: 'Lax' });
         createCookie("otherAhead", true);
       }
     }
     // info for special days
     // overwrite the event list
     if (received.eventList) {
       // Cookies.set("event_list", JSON.parse(received.eventList));
       console.log(received.eventList)
       let el = received.eventList;
       createCookie('event_list', JSON.stringify(el));
     }
     // the event infos
     if (received.eventData) {
       let eventData = received.eventData;
       for (var a in eventData) {
         createCookie(a, JSON.stringify(eventData[a]));
       }
     }
     // info for activities
     if (received.completedActivities) {
       let ca = received.completedActivities;
       Cookies.set('completedActivities', JSON.stringify(ca), { SameSite: 'Lax' });
       Cookies.set('numCompleted', ca.length, { SameSite: 'Lax' });
     }

     // update pages live
     // update special days page
     if (typeof rebuildPage === "function") {
       rebuildPage();
     }

     // update activities page
     if (typeof updateActivityColors === "function") {
       updateActivityColors();
     }

     // if (typeof rebuildTracker === "function") {
     //   rebuildTracker();
     // }
     if (typeof updateTrackerColors === "function") {
       updateTrackerColors();
     }

   }
 }


// helper cookie functions from days.html(drew inspiration from stackoverflow)
  function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
      }
      return null;
  }
  function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
  }
