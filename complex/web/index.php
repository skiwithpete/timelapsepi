<html>
<head>
<meta charset="UTF-8" />
  <link rel="stylesheet" type="text/css" href="css/style.css">
</head>


<?php
if (isset($_POST['testimage']))
{
exec("sudo python /home/pi/timelapse/testimage.py");
}
if (isset($_POST['timelapse1']))
{
exec("sudo python /home/pi/timelapse/timelapse1.py");
}
if (isset($_POST['timelapse2']))
{
exec("sudo python /home/pi/timelapse/timelapse2.py");
}
if (isset($_POST['timelapse3']))
{
exec("sudo python /home/pi/timelapse/timelapse3.py");
}
if (isset($_POST['timelapsecasey']))
{
exec("sudo python /home/pi/timelapse/timelapsecasey.py");
}
?>
<font size="6">
<form method="post">
<button class="classname" name="testimage">Test Image</button>&nbsp;
<button class="classname" name="timelapse1">timelapse 1</button>&nbsp;
<button class="classname" name="timelapse2">timelapse 2</button>&nbsp;
<button class="classname" name="timelapse2">timelapse 3</button>&nbsp;
<button class="classname" name="timelapsecasey">timelapse Casey</button>&nbsp;<br><br>

</form> 
</font>
<img src="imagetest.jpeg">

</html>
