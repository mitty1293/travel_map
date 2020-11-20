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
        addClickInfo(e.latLng.toString(), map, marker)
    });
}

function addClickMarker(lat_lng, map){
    // 既設のマーカーがある場合削除
    if(marker != null){
        marker.setMap(null);
    }
    marker = null;
    // 新規にマーカーを設置
    marker = new google.maps.Marker({
        position: lat_lng,
        map: map,
        title: lat_lng.toString(),
    });
    // 座標の中心をマーカーの位置へずらす
    map.panTo(lat_lng);
}

function addClickInfo(msg, map, marker){
    var infoWindow = new google.maps.InfoWindow({
        content: msg
    });
    infoWindow.open(map, marker);
}