function UpdateDetailsvalidateForm() {

    let pas = document.forms["UpdateDetails"]["password"].value;
    if (pas.length>0){
        if (pas.length < 4) {
            alert("The password is too short");
            return false;
        }
        let pas2 = document.forms["UpdateDetails"]["password2"].value;
        if (pas != pas2) {
            alert("your passwords are not equal");
            return false;
        }
    }

    let email = document.forms["UpdateDetails"]["email"].value;
    if (email.length>0){
        let atposition=email.indexOf("@");
        let dotposition=email.lastIndexOf(".");
        if (atposition<1 || dotposition<atposition+2 || dotposition+2>=email.length) {
            alert("un-valid email");
            return false;
        }
    }
    let phone = document.forms["UpdateDetails"]["phone"].value;
    if (phone.length>0) {
        if (phone.length != 10) {
            alert(" phone is invalid must contain 10 digits");
            return false;
        }
    }

    let address = document.forms["UpdateDetails"]["address"].value;
    if (address.length>0) {
        if (address.length < 5) {
            alert("address is invalid");
            return false;
        }
    }
}

