function addCategory() {
    var select = document.getElementById("categoryselect");
    var option = document.createElement("option");
    var added_category = document.getElementById("added_category").value;
    option.text = added_category;
    option.value = added_category;
    select.appendChild(option);
    select.value = added_category;
}