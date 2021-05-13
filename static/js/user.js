function formatCreditCard() {
    var x = document.getElementById("credit-card");
    var index = x.value.lastIndexOf('-');
    var test = x.value.substr(index + 1);
    if (test.length === 4){
       x.value = x.value + '-';
    }
}