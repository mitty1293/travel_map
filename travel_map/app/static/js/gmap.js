var map;
var marker = null;
function initMap(){
    var opts = {
        zoom: 15,
        center: new google.maps.LatLng(35.709984,139.810703)
    };
    map = new google.maps.Map(document.getElementById("gmap"), opts);

    // クリックイベント追加
    map.addListener('click', function(e){
        addClickMarker(e.latLng, map);
    });
}

function create_marker(options){
    var m =  new google.maps.Marker(options);
    return m;
}

function addClickMarker(lat_lng, map){
    if(marker != null){
        marker.setMap(null);
    }
    marker = null;
    // マーカー設置
    marker = create_marker({
        position: lat_lng,
        map: map,
        title: lat_lng.toString(),
    });
    // 座標の中心をマーカーの位置へずらす
    map.panTo(lat_lng);
}