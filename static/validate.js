function validate() {
    

    var pwd = document.getElementById("passwordid").value;
    var conpwd = document.getElementById("conpasswordid").value;

    if (pwd != conpwd)
    {
      alert("Password and Confirm password are not same");
      return false;
      
    }
    return true;
  }

  function myFunction() {
    var x = document.getElementById("EditQuery");
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }