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