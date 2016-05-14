<?php
$message = $_GET["message"];
$con=mysqli_connect("localhost","username","password","sensordata");
if (mysqli_connect_errno())
		  {
		  echo "Failed to connect to MySQL: " . mysqli_connect_error();
		  }
mysqli_query($con, "INSERT INTO sensordata(message) VALUES('$message')");
$result = mysqli_query($con, "SELECT * FROM sensordata ORDER BY id ASC");
while($row=mysqli_fetch_array($result)){
echo "<div class='comments_content'>";

echo "<h1>" . $row['message'] . "</h1>";
echo "<h2>" . $row['date_publish'] . "</h2></br></br>";

echo "</div>";
}

mysqli_close($con);
?>


