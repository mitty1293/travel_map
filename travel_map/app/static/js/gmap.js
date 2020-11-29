var map;
var marker = null;
var infoWindow = null;
var entry_link = '<a href="javascript:postLatLng(${lat_lng});">登録</a>';

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

// mapクリック時にマーカーと情報ウインドウを設置する
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
        title: lat_lng.toString()
    });
    // マーカーの位置へ情報ウインドウを表示
    infoWindow = new google.maps.InfoWindow({
        content: `<p>${lat_lng.toString()}</p><p><a href="/entry?lat_lng=${lat_lng.toString()}">登録</a></p>`
    });
    infoWindow.open(map, marker);
    // 座標の中心をマーカーの位置へずらす
    map.panTo(lat_lng);
}
