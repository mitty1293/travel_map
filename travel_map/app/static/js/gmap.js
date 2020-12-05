var map;
var initMarker =null;
var clickMarker = null;
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

// マーカーの初期表示用
function showInitMarker(){
    initMarker = new google.maps.Marker({
        
    });
}

// mapクリック時にマーカーと情報ウインドウを設置する
function addClickMarker(lat_lng, map){
    // 既設のマーカーがある場合削除
    if(clickMarker != null){
        clickMarker.setMap(null);
    }
    clickMarker = null;
    // 新規にマーカーを設置
    clickMarker = new google.maps.Marker({
        position: lat_lng,
        map: map,
        title: lat_lng.toString()
    });
    // マーカーの位置へ情報ウインドウを表示
    infoWindow = new google.maps.InfoWindow({
        content: `<p>${lat_lng.toString()}</p><p><a href="/entry?lat=${lat_lng.lat()}&lng=${lat_lng.lng()}">登録</a></p>`
    });
    infoWindow.open(map, clickMarker);
    // 座標の中心をマーカーの位置へずらす
    map.panTo(lat_lng);
}
