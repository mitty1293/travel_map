var map;
var initMarker =null;
var clickMarker = null;
var infoWindow = null;
var init_marker_results = {{init_marker_results|tojson}}

function initMap(){
    var opts = {
        zoom: 15,
        center: new google.maps.LatLng(35.709984,139.810703)
    };
    map = new google.maps.Map(document.getElementById("gmap"), opts);
    // クリックイベント追加
    map.addListener('click', function(e){
        addMarker(e.latLng, map);
    });
    // マーカーの初期表示
    showInitMarker(init_marker_results, map);
}

// マーカーの初期表示用
function showInitMarker(init_marker_data, map){
    for (var i=0; i<init_marker_data.length; i++){
        var row = init_marker_data[i];
        initMarker[i] = new google.maps.Marker({
            position: row[1],
            map: map
        });
    }
}

// mapクリック時にマーカーと情報ウインドウを設置する
function addMarker(lat_lng, map){
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

// 現在地にマーカーと情報ウインドウを設置する
function getCurrentPosition(){
    //ブラウザが Geolocation に対応しているかを判定
    infoWindow = new google.maps.InfoWindow;
    if(!navigator.geolocation){
        //情報ウィンドウの位置をマップの中心位置に指定
        infoWindow.setPosition(map.getCenter());
        //情報ウィンドウのコンテンツを設定
        infoWindow.setContent('Geolocation に対応していません。');
        //情報ウィンドウを表示
        infoWindow.open(map);
    }
    //  現在地情報の取得と情報ウインドウ設置
    navigator.geolocation.getCurrentPosition(function(position){
        var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        addMarker(pos, map);
    }, function(){ //位置情報の取得をユーザーがブロックした場合のコールバック
        infoWindow.setPosition(map.getCenter());
        infoWindow.setContent('Error: Geolocation が無効です。');
        infoWindow.open(map);
    });
}
