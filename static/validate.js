function validate() {
    

    var pwd = document.getElementById("passwordid").value;
    var conpwd = document.getElementById("conpasswordid").value;

    if (pwd != conpwd)
    {
      alert("pwd conpwd not same");
      return false;
      
    }
    return true;
  }