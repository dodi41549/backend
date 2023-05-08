<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $message = "Hello, " . $name . "! Welcome to my app!";
    echo $message;
}
?>
