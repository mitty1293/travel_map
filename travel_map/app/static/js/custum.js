function addCategory() {
    var select = document.getElementById("categoryselect");
    var option = document.createElement("option");
    var added_category = document.getElementById("added_category").value;
    option.text = added_category;
    option.value = added_category;
    select.appendChild(option);
    $('#msg').html('<div class="alert alert-success fade in"><button type="button" class="close close-alert" data-dismiss="alert" aria-hidden="true">×</button>This is a success message</div>');
}