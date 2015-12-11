<?php
//Connecting to sql db.
$connect = mysqli_connect("0.0.0","gameTimeDatabase.db");
//Sending form data to sql db.
mysqli_query($connect,"INSERT INTO times (name, time)
VALUES ('$_POST[]', '$_POST[time]')";
?>