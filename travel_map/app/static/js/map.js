function initMap(){
    var opts = {
        zoom: 15,
        center: new google.maps.LatLng(35.709984,139.810703)
    };
    var map = new google.maps.Map(document.getElementById("map"), opts);

    map.addListener('click', function(e){
        var marker = new google.maps.Marker({
            position: e.latLng,
            map: map,
            title: e.latLng.toString(),
            animation: google.maps.Animation.DROP
        });
    });
}