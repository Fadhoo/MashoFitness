document.getElementById("dateofbirth").onchange = function () {
    var Bdate = this.value;
    var Bday = +new Date(Bdate);
    document.getElementById('emp-age').value = ~~((Date.now() - Bday) / (31557600000));
}