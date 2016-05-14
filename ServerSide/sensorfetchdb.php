<?php
header('Access-Control-Allow-Origin: *');
#EReplace username and password with username and password of phpmyadmin
$con=mysqli_connect("localhost","username","password","sensordata");

$result = mysqli_query($con, "SELECT * FROM sensordata ORDER BY id DESC");
while($row=mysqli_fetch_array($result)){
echo "<div class='comments_content'>";

echo "<h1>" . $row['message'] . "</h1>";
echo "<h2>" . $row['date_publish'] . "</h2></br></br>";

echo "</div>";
}
mysqli_close($con);

?>
