var map;
var initMarker = [];
var clickMarker = null;
var initinfoWindow = [];
var clickinfoWindow = null;
var currentinfoWindow = null;

function initMap(){
    var opts = {
        zoom: 15,
        center: new google.maps.LatLng(35.709984,139.810703)
    };
    map = new google.maps.Map(document.getElementById("gmap"), opts);
    var geocoder = new google.maps.Geocoder();
    // クリックイベント追加
    map.addListener('click', function(e){
        geocoder.geocode({location: e.latLng}, function(results, status){
            addMarker(e.latLng, results[0].formatted_address, map);
        });
    });

    // マーカーの初期表示
    showInitMarker(init_marker_json, map);

    searchAddress(map);
}

// マーカーの初期表示用
function showInitMarker(marker_data, map){
    for (var i=0; i<marker_data.length; i++){
        var row = marker_data[i];
        var markerLatlng = new google.maps.LatLng({lat: row['lat'], lng: row['lng']});
        initMarker[i] = new google.maps.Marker({
            position: markerLatlng,
            map: map,
            icon: 'https://maps.google.com/mapfiles/ms/icons/green-dot.png'
        });
        initinfoWindow[i] = new google.maps.InfoWindow({
            content: `<p>${row['spot_name']}</p><p><a href="/show/${row['id']}">詳細を確認</a></p>`
        });
        showInitInfoWindow(i);
    }
}

// 初期表示マーカークリック時に情報ウインドウを表示
// クリックイベントはイベント追加時とクリック時に変数iの値が変わってしまうため別関数とする
function showInitInfoWindow(i){
    initMarker[i].addListener('click', function(){
        initinfoWindow[i].open(map, initMarker[i]);
    });
}

// mapクリック時にマーカーと情報ウインドウを設置する
function addMarker(lat_lng, address, map){
    // 既設のマーカーがある場合削除
    if(clickMarker != null){
        clickMarker.setMap(null);
    }
    clickMarker = null;
    // 新規にマーカーを設置
    clickMarker = new google.maps.Marker({
        position: lat_lng,
        map: map
    });
    // マーカーの位置へ情報ウインドウを表示
    clickinfoWindow = new google.maps.InfoWindow({
        content: `<p>${address}</p><p><a href="/entry?lat=${lat_lng.lat()}&lng=${lat_lng.lng()}">この場所を登録</a></p>`
    });
    clickinfoWindow.open(map, clickMarker);
    // 座標の中心をマーカーの位置へずらす
    map.panTo(lat_lng);
}

// 現在地にマーカーと情報ウインドウを設置する
function getCurrentPosition(){
    //ブラウザが Geolocation に対応しているかを判定
    currentinfoWindow = new google.maps.InfoWindow;
    if(!navigator.geolocation){
        //情報ウィンドウの位置をマップの中心位置に指定
        currentinfoWindow.setPosition(map.getCenter());
        //情報ウィンドウのコンテンツを設定
        currentinfoWindow.setContent('Geolocation に対応していません。');
        //情報ウィンドウを表示
        currentinfoWindow.open(map);
    }
    //  現在地情報の取得と情報ウインドウ設置
    navigator.geolocation.getCurrentPosition(function(position){
        var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };
        addMarker(pos, map);
    }, function(){ //位置情報の取得をユーザーがブロックした場合のコールバック
        currentinfoWindow.setPosition(map.getCenter());
        currentinfoWindow.setContent('Error: Geolocation が無効です。');
        currentinfoWindow.open(map);
    });
}

// 住所検索用
function searchAddress(map){
    var query = document.getElementById("id_address").value;
    console.log(query);
    // プレイス検索
    var service = new google.maps.places.PlacesService(map);
    console.log('1');
    var request = {
        location: new google.maps.LatLng(35.709984,139.810703),
        radius: '500',
        query: query
    };
    console.log('2');
    service.textSearch(request, callback);
    console.log('3');
}
// 検索結果の処理
function callback(results, status){
    console.log('4');
    if (status === google.maps.places.PlacesServiceStatus.OK){
        console.log('5');
        for (var i=0; i<results.length; i++){
            console.log(results[i].name);
            console.log(results[i].geometry.location);
        }
    }else{
        console.log('6');
    }
}
