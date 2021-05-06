
function validateForm() {
	var errorsHtml = "";

	var firstname = document.getElementById("FirstName").value;
	if (firstname == null || firstname == "") {
		errorsHtml += "FirstName is mandatory!<br/>"
	}

	var lastname = document.getElementById("LastName").value;
	if (lastname == null || lastname == "") {
		errorsHtml += "LastName is mandatory!<br/>"
	}
	var email = document.getElementById("Email").value;
	if (email == null || email == "") {
		errorsHtml += "Email is mandatory!<br/>"
	}
	
	var username = document.getElementById("UserName").value;
	if (username == null || username == "") {
		errorsHtml += "UserName is mandatory!<br/>"
	}
	
	var password = document.getElementById("Password").value;
	if (password == null || password == "") {
		errorsHtml += "Password is mandatory!<br/>"
	}
	var cpassword = document.getElementById("CPassword").value;
	if (cpassword == null || cpassword == "") {
		errorsHtml += "Confirm Password is mandatory!<br/>"
	}
	var uploadfile = document.getElementById("file").value;
	if (uploadfile == null || uploadfile == "") {
		errorsHtml += "File insertion is mandatory!<br/>"
	}
	var aboutyou = document.getElementById("AboutYou").value;
	if (aboutyou == null || aboutyou == "") {
		errorsHtml += "A short description about you is mandatory !<br/>"
	}
	
	if (errorsHtml !== ""){
		errorsHtml = "Found Errors:<br/>" + errorsHtml;
	}
	
	document.getElementById("errors").innerHTML = errorsHtml;
}