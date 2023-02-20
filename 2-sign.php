<?php  
ob_start();
require("utility.php"); ?>

<?php
$u_name=$_POST['uname'];
$f_name=$_POST['fname'];
$pwd=$_POST['pws'];
$e_mail=$_POST['email'];
$cou=$_POST['county'];
$phone=$_POST['phone'];




//$image = chunk_split(base64_encode(file_get_contents( $imup )));


$sql=" INSERT INTO user (username,fullname,password,e_mail,user_type,county,phone) values ('$u_name','$f_name','$pwd','$e_mail', default,'$cou','$phone)";

$result=ExecuteNonQuery ($sql);

if($result)
{
	header("location:login.html");
}
else
{
		header("location:sign.html");
}
?> 	
